import streamlit as st
import os
import time
from dotenv import load_dotenv
from utils import read_pdf, init_chroma, seed_database
from graph import build_graph

# Load environment variables
load_dotenv()

st.set_page_config(page_title="BidWinner AI", page_icon="📝", layout="wide")

st.title("🤖 BidWinner AI: Automated Proposal Generator")
st.markdown("Upload a client's RFP (PDF) and let the Multi-Agent System generate a winning technical proposal.")

# Sidebar Configuration
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Groq API Key", type="password", value=os.getenv("GROQ_API_KEY", ""))
    
    st.markdown("---")
    st.markdown("### System Status")
    
    # Initialize DB button (optional but good for demo)
    if st.button("Initialize/Reset Knowledge Base"):
        with st.spinner("Seeding ChromaDB..."):
            try:
                # We need to ensure we have a collection
                vectorstore = init_chroma()
                if vectorstore:
                    seed_database(vectorstore)
                    st.success("Knowledge Base Seeded!")
                else:
                    st.error("Failed to init DB.")
            except Exception as e:
                st.error(f"Error: {e}")

# Main Content
uploaded_file = st.file_uploader("Upload Request for Proposal (PDF)", type=["pdf"])

if uploaded_file and api_key:
    if st.button("Generate Proposal"):
        # 1. Read PDF
        with st.spinner("Reading Document..."):
            input_text = read_pdf(uploaded_file)
            st.info(f"Document Read: {len(input_text)} characters extracted.")

        # 2. Init Graph
        app = build_graph()
        initial_state = {"input_text": input_text, "api_key": api_key}
        
        # 3. Stream Execution
        st.markdown("### 🧠 Agent Workflow Execution")
        
        # Container for results
        analyst_expander = st.expander("🕵️ Analyst Agent (Requirements)", expanded=True)
        architect_expander = st.expander("🏗️ Architect Agent (Tech Stack)", expanded=False)
        estimator_expander = st.expander("⏱️ Estimator Agent (Cost & Time)", expanded=False)
        writer_expander = st.expander("✍️ Proposal Writer (Final)", expanded=False)
        
        final_output = None
        
        # We process the graph and update UI step by step
        # Note: app.stream(initial_state) yields events
        
        with st.spinner("Agents are working..."):
            for output in app.stream(initial_state):
                for key, value in output.items():
                    if key == "analyst":
                        analyst_expander.markdown(value.get("analyst_output"))
                    elif key == "architect":
                        architect_expander.markdown(value.get("architect_output"))
                    elif key == "estimator":
                        estimator_expander.markdown(value.get("estimator_output"))
                    elif key == "writer":
                        final_output = value.get("final_proposal")
                        writer_expander.markdown(final_output)

        # 4. Final Display
        if final_output:
            st.markdown("---")
            st.header("📄 Final Proposal")
            st.markdown(final_output)
            
            st.download_button(
                label="Download Proposal (Markdown)",
                data=final_output,
                file_name="BidWinner_Proposal.md",
                mime="text/markdown"
            )

elif not api_key:
    st.warning("Please enter your Groq API Key to proceed.")
