# 🔎 Search & Summarize Agent (LangGraph + Ollama)

This project implements a **modular LangGraph agent** that can:
1. Take a user query.  
2. Perform a **web search** (DuckDuckGo).  
3. Summarize the findings using an **LLM (Ollama)**.  

The agent is designed to be **reusable** — it can be imported into larger agent pipelines or used as a standalone search-summarization tool.

---

## 🚀 Features
- **LangGraph-powered workflow** (state machine style execution).  
- **DuckDuckGo Search Integration** for retrieving real-time information.  
- **Ollama-based Summarization** for clean, natural summaries.  
- **Reusable Design** — exportable via `build_search_agent()` for integration into other agents.  

---

## 📂 Project Structure

    ├── LLM.py 
    ├── search_tool.py 
    ├── main.py
    ├── search_agent.py 
    └── README.md 


---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Saibhossain/Googler-Search-Agent.git
cd Googler-Search-Agent
```


### 2. Install Dependencies
Make sure you have Python 3.9+ installed.
Install required dependencies:

    pip install langgraph duckduckgo-search

Note: You also need Ollama installed and running locally.

## 🛠 Usage
Standalone Execution
Run the agent directly:
```bash
python main.py
```
This will:
> Search DuckDuckGo for "Latest research on Bangla LLMs".
Summarize the results via Ollama.
Print the final answer.