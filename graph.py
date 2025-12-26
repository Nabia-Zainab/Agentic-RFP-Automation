import os
from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from prompts import ANALYST_PROMPT, ARCHITECT_PROMPT, ESTIMATOR_PROMPT, WRITER_PROMPT
from utils import init_chroma, seed_database

# Define the State
class AgentState(TypedDict):
    input_text: str
    analyst_output: Optional[str]
    architect_output: Optional[str]
    estimator_output: Optional[str]
    final_proposal: Optional[str]
    api_key: str

# 1. Analyst Node
def analyst_node(state: AgentState):
    print("--- NODE: Analyst ---")
    llm = ChatGroq(api_key=state['api_key'], model="llama-3.3-70b-versatile")
    chain = ANALYST_PROMPT | llm | StrOutputParser()
    response = chain.invoke({"content": state['input_text']})
    return {"analyst_output": response}

# 2. Architect Node
def architect_node(state: AgentState):
    print("--- NODE: Architect ---")
    llm = ChatGroq(api_key=state['api_key'], model="llama-3.3-70b-versatile")
    chain = ARCHITECT_PROMPT | llm | StrOutputParser()
    response = chain.invoke({"analyst_output": state['analyst_output']})
    return {"architect_output": response}

# 3. Estimator Node (with RAG)
def estimator_node(state: AgentState):
    print("--- NODE: Estimator ---")
    llm = ChatGroq(api_key=state['api_key'], model="llama-3.3-70b-versatile")
    
    # RAG: Retrieve similar proposals
    vectorstore = init_chroma()
    if vectorstore:
        # Check if we need to seed (simple check if collection is small/empty logic handled in utils/init ideally, 
        # but here we can just ensure we query)
        # Note: init_chroma returns the vectorstore.
        retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
        # For this demo, we can just query based on analysis summary
        docs = retriever.invoke(state['analyst_output'])
        rag_data = "\n\n".join([doc.page_content for doc in docs])
    else:
        rag_data = "No historical data available."

    chain = ESTIMATOR_PROMPT | llm | StrOutputParser()
    response = chain.invoke({
        "analyst_output": state['analyst_output'],
        "architect_output": state['architect_output'],
        "rag_data": rag_data
    })
    return {"estimator_output": response}

# 4. Writer Node
def writer_node(state: AgentState):
    print("--- NODE: Writer ---")
    llm = ChatGroq(api_key=state['api_key'], model="llama-3.3-70b-versatile")
    chain = WRITER_PROMPT | llm | StrOutputParser()
    response = chain.invoke({
        "analyst_output": state['analyst_output'],
        "architect_output": state['architect_output'],
        "estimator_output": state['estimator_output']
    })
    return {"final_proposal": response}

# Build the Graph
def build_graph():
    workflow = StateGraph(AgentState)

    # Add Nodes
    workflow.add_node("analyst", analyst_node)
    workflow.add_node("architect", architect_node)
    workflow.add_node("estimator", estimator_node)
    workflow.add_node("writer", writer_node)

    # Add Edges (Linear Flow)
    workflow.set_entry_point("analyst")
    workflow.add_edge("analyst", "architect")
    workflow.add_edge("architect", "estimator")
    workflow.add_edge("estimator", "writer")
    workflow.add_edge("writer", END)

    return workflow.compile()
