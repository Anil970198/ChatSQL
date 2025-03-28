# 🧠 GemMath AI – Solve Math with Gemma 2 🚀

GemMath AI is an intelligent Streamlit-powered assistant that **solves numeric and symbolic math problems**, handles **logical reasoning**, and performs **real-time Wikipedia searches** — all powered by **Google Gemma 2 via Groq**, LangChain, and SymPy.

> 🔍 Built for learners, engineers, and curious minds who want clear step-by-step answers to complex math and reasoning problems — right in their browser.

---

## 🚀 Features

✅ **Numeric & Symbolic Math Solver**  
- Handles calculations like `12 + 5 * 3`  
- Supports symbolic operations: `differentiate`, `integrate`, `expand`, `solve`, `simplify`, `limit`  
- Returns LaTeX-rendered step-by-step results using `SymPy`

🧠 **Logical Reasoning Engine**  
- Multi-step reasoning for logic problems like:  
  *"John is taller than Alice. Alice is taller than Bob. Who is the tallest?"*

📚 **Wikipedia Search Agent**  
- Instant access to encyclopedic knowledge through LangChain + Wikipedia API

🌐 **Beautiful Streamlit Interface**  
- Clean and intuitive UI with tab-based navigation

🔐 **Groq API Integration**  
- Runs **Gemma 2 (Gemma2-9b-It)** blazing-fast via Groq's LLM inference

---

## 🛠️ Tech Stack

| Layer        | Tools & Frameworks                          |
|--------------|---------------------------------------------|
| 💡 LLM Agent | [LangChain](https://www.langchain.com/)     |
| ⚙️ Backend   | Python, [SymPy](https://www.sympy.org/), [Groq API](https://groq.com/) |
| 🧮 LLM Model | Google Gemma 2 (Gemma2-9b-It) via Groq      |
| 🖼️ Frontend  | [Streamlit](https://streamlit.io/)          |
| 📚 Knowledge | Wikipedia API                               |

---

## 🧪 Live Demo

**[👉 Try it on Streamlit (Demo)](https://your-app-url.streamlit.app)**  
> _(Replace with your hosted app URL)_

---

## 📸 Screenshots

| Math Solver (Symbolic) | Logical Reasoning |
|------------------------|-------------------|
| ![Math Demo](screenshots/math_solver.png) | ![Reasoning Demo](screenshots/reasoning.png) |

---

## 🧰 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/YOUR-USERNAME/GemMath-AI.git
cd GemMath-AI

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
