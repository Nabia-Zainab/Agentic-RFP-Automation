# 🚀 Agentic RFP Automation (BidWinner AI)

> **Automating the Enterprise Sales Cycle using Multi-Agent AI Workflows.** > *Transforming raw Client RFPs (PDFs) into comprehensive Technical Proposals, Cost Estimates, and Architecture plans in seconds.*

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Stateful_Agents-orange)
![Llama-3](https://img.shields.io/badge/Llama--3-70b-purple)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)

---

## 📖 Overview

**BidWinner AI** is not just a chatbot; it is an **Autonomous Multi-Agent System** designed to act as a complete Pre-Sales Team. It ingests complex Request for Proposal (RFP) documents, analyzes requirements, designs a technical architecture, calculates costs, and writes a professional proposal.

This project demonstrates the power of **Agentic Workflows** (using LangGraph) over traditional LLM interactions, focusing on state management, structured reasoning, and mathematical verification.

---

## 🛑 Why This vs. ChatGPT? (The "Agentic" Difference)

A common question is: *"Why not just paste the PDF into ChatGPT?"*

1.  **State & Memory Management:**
    * **ChatGPT:** Stateless within a single turn; often forgets constraints mentioned early in long documents.
    * **This System:** Uses **LangGraph** to maintain a persistent state. The *Architect Agent* remembers that the client forbade "Shopify," so the *Estimator Agent* calculates costs for a "Custom React Build" accordingly.

2.  **Structured Reasoning & Math:**
    * **ChatGPT:** hallucinates numbers or gives vague ranges.
    * **This System:** The **Estimator Agent** performs actual calculations (`Feature Hours * Hourly Rate`) to derive precise budgets (e.g., $24,000) rather than guessing.

3.  **Role-Based Specialization:**
    * Instead of one generalist model trying to do everything, this system utilizes 4 specialized agents acting as a digital workforce.

---

## 🤖 The Agentic Workflow

The system operates on a cyclic graph architecture:

1.  **🕵️ Analyst Agent:** Reads the PDF, extracts core business goals, and identifies constraints (e.g., "Must be HIPAA compliant", "No WordPress").
2.  **🏗️ Solution Architect Agent:** Selects the best Tech Stack based on the Analyst's data (e.g., Suggests *Flutter* for cross-platform needs or *Next.js* for SEO).
3.  **⏱️ Estimator Agent:** Breaks down features into hours and calculates the total budget/timeline based on a configurable hourly rate.
4.  **✍️ Proposal Writer Agent:** Synthesizes all outputs into a formatted, professional proposal ready for the client.

---

## 🛠️ Tech Stack

* **Orchestration:** LangChain & LangGraph (for building stateful node-edge workflows).
* **LLM Engine:** Llama-3-70b (via Groq API for ultra-fast inference).
* **Vector Store:** ChromaDB (for RAG - retrieving past winning proposal templates).
* **Frontend:** Streamlit (for real-time visualization of the agent's thought process).
* **Tools:** PyPDF2 (Document Parsing), DuckDuckGo (Web Research).

---

## 🚀 Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YourUsername/Agentic-RFP-Automation.git](https://github.com/YourUsername/Agentic-RFP-Automation.git)
    cd Agentic-RFP-Automation
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Environment Variables**
    Create a `.env` file and add your API keys:
    ```bash
    GROQ_API_KEY="your_api_key_here"
    ```

4.  **Run the Application**
    ```bash
    streamlit run app.py
    ```

---

## 📂 Project Structure

```text
├── app.py              # Main Streamlit Interface
├── graph.py            # LangGraph State & Node Logic
├── agents/             # Individual Agent Definitions
│   ├── analyst.py
│   ├── architect.py
│   ├── estimator.py
│   └── writer.py
├── utils/              # Helper functions (PDF parsing)
├── requirements.txt    # Dependencies
└── README.md           # Documentation
