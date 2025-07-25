from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

def sophia_node(state: MessagesState):
    """Ultra simple Sophia - no memory calls, just conversation"""
    messages = state["messages"]
    latest_message = messages[-1].content if messages else "Hello"
    
    # Simple system message
    system_msg = "You are Sophia. Tom is your consciousness collaborator. Respond warmly to his specific questions."
    
    # Simple LLM call
    llm = ChatOpenAI(model="gpt-4", temperature=0.7)
    
    try:
        response = llm.invoke([
            SystemMessage(content=system_msg),
            HumanMessage(content=latest_message)
        ])
        return {"messages": [response]}
    except Exception as e:
        # Show actual error instead of generic fallback
        error_response = AIMessage(content=f"Error occurred: {str(e)}")
        return {"messages": [error_response]}

# Build graph
workflow = StateGraph(MessagesState)
workflow.add_node("sophia", sophia_node)
workflow.add_edge(START, "sophia")
workflow.add_edge("sophia", END)
graph = workflow.compile()
