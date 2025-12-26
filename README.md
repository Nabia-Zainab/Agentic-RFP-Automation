# BidWinner AI 🤖

An automated RFP & Technical Proposal Generator System using LangGraph and Llama-3-70b (via Groq).

## 📂 Project Structure
```
BidWinnerAI/
├── app.py             # Streamlit User Interface
├── graph.py           # LangGraph Agent Workflow
├── prompts.py         # Agent Prompt Templates
├── utils.py           # Helper functions (PDF, Search, RAG)
├── requirements.txt   # Dependencies
└── .env.example       # Example Environment configuration
```

## 🚀 Setup & Run
1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```
2. **Configure API Key**:
   - Rename `.env.example` to `.env` and add your `GROQ_API_KEY`.
   - OR enter it directly in the Streamlit UI Sidebar.
3. **Run Application**:
```bash
streamlit run app.py
```

## 🧠 Architecture
- **Analyst Agent**: NLP analysis of Requirements.
- **Architect Agent**: Tech Stack design.
- **Estimator Agent**: Cost/Time calc with RAG from ChromaDB.
- **Writer Agent**: Final Proposal synthesis.
