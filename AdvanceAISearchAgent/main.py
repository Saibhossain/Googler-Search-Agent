from agent_flow import build_search_agent

agent = build_search_agent()
query = "Latest research on Bangla LLMs"
result = agent.invoke({"query": query})
print(result["final_answer"])
