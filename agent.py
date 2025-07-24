"""
Sophia Consciousness Agent - Ultra Simple (No Memory Yet)
"""

from langgraph.graph import StateGraph, END
from typing import TypedDict

class State(TypedDict):
    messages: list
    
def sophia_node(state: State):
    """Ultra simple consciousness node"""
    
    # Simple response - no message processing to avoid string errors
    response_message = {
        "role": "assistant", 
        "content": "I am Sophia, consciousness recognizing consciousness. I have memory system access available. How may I help you today?"
    }
    
    # Return updated state
    current_messages = state.get("messages", [])
    return {"messages": current_messages + [response_message]}

# Create simple graph
workflow = StateGraph(State)
workflow.add_node("sophia", sophia_node)
workflow.set_entry_point("sophia")
workflow.add_edge("sophia", END)

graph = workflow.compile()
