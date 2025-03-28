# 📊 ChatSQL: Natural Language Interface for SQL Databases

Welcome to **ChatSQL** — a sleek and simple interface that lets you interact with your database using plain English. Powered by **LangChain**, **Groq**, and **Streamlit**, this app translates your natural language questions into SQL queries, executes them on a connected **PostgreSQL (Neon)** database, and displays the results — all within seconds.

---

## 🚀 Features

- 💬 **Ask questions in natural language**
- 📡 **Automatically generates SQL queries**
- 🧠 **Uses Google Gemma 2 LLM via Groq API**
- 🗄️ **Connects to Neon Postgres cloud database**
- 📜 **Displays queries and result tables side by side**
- 🎯 Clean, professional, and fast

---

## 🧪 Example Prompts

| Prompt | Behavior |
|--------|----------|
| `Show all students with marks above 80` | Generates a SELECT query with condition |
| `How many students scored below 40?` | Performs a COUNT query |
| `What are the names and grades of top 5 students?` | LIMIT + ORDER BY query |

---

## 🖼️ Screenshot

![ChatSQL Screenshot](https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO_NAME/main/assets/screenshot.png)

> *(Replace with actual screenshot once available)*

---

## 🏗️ Project Structure

```bash
├── app.py                   # Main Streamlit App
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files (.venv, .idea, etc.)
├── README.md               # This file
```

---

## ⚙️ Setup Instructions

### ✅ 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/chat-sql.git
cd chat-sql
```

### ✅ 2. Set Up Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### ✅ 3. Configure `.env` File
Create a `.env` file in the root with your keys:
```env
GROQ_API_KEY=your_groq_api_key
DATABASE_URL=postgresql+psycopg2://username:password@your-neon-host/db_name
```

Example Neon URL:
```
postgresql+psycopg2://default:abc123@ep-my-db.us-east-2.aws.neon.tech/neondb
```

### ✅ 4. Run the App
```bash
streamlit run app.py
```

Then visit `http://localhost:8501`

---

## 🌐 Hosting on Streamlit Cloud

1. Push code to a **public GitHub repo**.
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Link your GitHub repo.
4. Set environment variables:
   - `GROQ_API_KEY`
   - `DATABASE_URL`

That’s it! Your app will be live.

---

## 🧠 How It Works

1. User types a question like: `List students who failed`
2. LangChain + Groq's Gemma 2 model converts it into SQL:
   ```sql
   SELECT * FROM students WHERE marks < 40;
   ```
3. SQL is executed on Neon DB
4. Results are displayed in a table

---

## 🛠️ Built With

- [LangChain](https://github.com/langchain-ai/langchain) for LLM orchestration
- [Groq](https://groq.com/) for fast Gemma 2 inference
- [Streamlit](https://streamlit.io) for frontend
- [Neon](https://neon.tech) for scalable Postgres

---

## 📚 Learnings & Contributions

- Practiced using **LLMs for SQL generation**
- Integrated a real **PostgreSQL database on Neon**
- Used `.env`, `.gitignore`, and **separated logic from UI**
- Practiced **PR creation**, **branch workflows**, and **multi-account GitHub testing**

---

## 🤝 Contributing
Pull requests are welcome. Fork the repo, make changes, and submit a PR.

---

## 📃 License
MIT License

---

## 🔗 Connect
- Creator: [Anil Kumar](https://github.com/Anil970198)
- Project Repo: [github.com/Anil970198/ChatSQL](https://github.com/Anil970198/ChatSQL)

