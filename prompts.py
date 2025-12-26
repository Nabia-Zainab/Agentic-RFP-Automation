from langchain_core.prompts import PromptTemplate

ANALYST_PROMPT = PromptTemplate(
    input_variables=["content"],
    template="""
    You are a Senior Business Analyst. Analyze the following RFP/Project Requirement document provided by the client.
    
    Document Content:
    {content}
    
    Your Task:
    1. Identify the Core Business Goal.
    2. Extract Key Deliverables (List them clearly).
    3. Identify any Technical Constraints mentioned (e.g., specific cloud, language, deadlines).
    4. Identify the Target Audience for the solution.
    
    Output Format:
    Return a structured summary in Markdown format.
    """
)

ARCHITECT_PROMPT = PromptTemplate(
    input_variables=["analyst_output"],
    template="""
    You are a Chief Technology Officer (CTO). Based on the analysis below, design a high-level technical architecture and recommend a technology stack.
    
    Analyst Report:
    {analyst_output}
    
    Your Task:
    1. Recommend the Tech Stack (Frontend, Backend, Database, AI Models, Ops).
    2. Explain "Why" this stack was chosen for this specific project.
    3. Outline the System Architecture (how components interact).
    
    Output Format:
    Return a structured technical proposal section in Markdown.
    """
)

ESTIMATOR_PROMPT = PromptTemplate(
    input_variables=["analyst_output", "architect_output", "rag_data"],
    template="""
    You are a Senior Project Manager. Estimate the Timeline and Cost for the project based on the requirements and architecture.
    
    Analyst Report:
    {analyst_output}
    
    Technical Architecture:
    {architect_output}
    
    Similar Past Projects (Reference):
    {rag_data}
    
    Your Task:
    1. Create a "Feature Breakdown" with estimated hours for each major feature.
    2. Calculate Total Hours.
    3. Calculate Total Cost (assume $30/hour rate).
    4. Provide a Project Timeline (Reference Past Projects if relevant).
    
    Output Format:
    Return a detailed Cost & Timeline Estimation table in Markdown.
    """
)

WRITER_PROMPT = PromptTemplate(
    input_variables=["analyst_output", "architect_output", "estimator_output"],
    template="""
    You are a Professional Proposal Writer. Synthesize all the provided information into a winning proposal for the client.
    
    Business Analysis:
    {analyst_output}
    
    Technical Solution:
    {architect_output}
    
    Cost & Timeline:
    {estimator_output}
    
    Your Task:
    Write a complete "Technical & Commercial Proposal".
    Structure:
    1. **Executive Summary**: Persuasive introduction.
    2. **Proposed Solution**: Technical approach and architecture.
    3. **Project Scope**: Key deliverables.
    4. **Timeline & Budget**: The estimation table.
    5. **Conclusion**: Why we are the best fit.
    
    Tone: Professional, Persuasive, and Confidence-inspiring.
    output Format: valid Markdown.
    """
)
