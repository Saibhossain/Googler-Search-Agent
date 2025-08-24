from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from LLM import ollama_generate
from search_tool import search_duckduckgo

class AgentState(TypedDict, total=False):
    query: str
    search_results: str
    final_answer: str

def search_node(state: AgentState):
    query = state["query"]
    search_results = search_duckduckgo(query)
    state["search_results"] = search_results
    return state

def summarize_node(state: AgentState):
    query = state["query"]
    results = state["search_results"]

    prompt = f"""You are a helpful assistant.
                Search Query: {query}
                Results: {results} Summarize the findings clearly:"""
    summary = ollama_generate(prompt)
    state["final_answer"] = summary
    return state

def build_search_agent():
    graph = StateGraph(AgentState)
    graph.add_node("Search", search_node)
    graph.add_node("Summarize", summarize_node)

    graph.set_entry_point("Search")
    graph.add_edge("Search", "Summarize")
    graph.add_edge("Summarize", END)

    return graph.compile()