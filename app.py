import streamlit as st
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain_groq import ChatGroq
from sqlalchemy import create_engine
from langchain.callbacks import StreamlitCallbackHandler

st.set_page_config(page_title="🔍 Chat with Your Own Database", page_icon="🧠")
st.title("🧠 Chat with Your PostgreSQL Database")

st.markdown("Enter your **PostgreSQL credentials** and your **GROQ API key** to get started.")

# Sidebar inputs
st.sidebar.header("🔑 Database Connection")
pg_host = st.sidebar.text_input("PostgreSQL Host", placeholder="ep-neon-host.neon.tech")
pg_db = st.sidebar.text_input("Database Name")
pg_user = st.sidebar.text_input("Username")
pg_password = st.sidebar.text_input("Password", type="password")
pg_port = st.sidebar.text_input("Port", value="5432")

st.sidebar.header("⚙️ LLM Settings")
api_key = st.sidebar.text_input("GROQ API Key", type="password")

access_mode = st.sidebar.radio("Access Mode", ["Read-only", "Full Access"])

# Check inputs
if not all([pg_host, pg_db, pg_user, pg_password, api_key]):
    st.info("Enter all required fields to start chatting.")
    st.stop()

# Build DB connection URI
db_uri = f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}"

# Initialize LLM (without .bind())
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="Llama3-8b-8192",
    streaming=True
)

# Create SQLDatabase
try:
    db = SQLDatabase.from_uri(db_uri)
except Exception as e:
    st.error(f"Database connection failed: {e}")
    st.stop()

# Create Agent
agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True
)

# Session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you with your database?"}]

# Display messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_query = st.chat_input("Ask your question here...")

if user_query:
    # Prepend system instruction based on access mode
    instruction = "You are a helpful assistant. "
    if access_mode == "Read-only":
        instruction += "Only read from the database. Do not modify any data.\n"
    else:
        instruction += "You may read, insert, update, or delete data from the database.\n"

    final_prompt = instruction + user_query

    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        stream_handler = StreamlitCallbackHandler(st.container())
        try:
            response = agent.run(final_prompt, callbacks=[stream_handler])
        except Exception as e:
            response = f"⚠️ Error: {str(e)}"
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
