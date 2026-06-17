from dotenv import load_dotenv
import os

load_dotenv()

from langchain_community.tools.tavily_search import TavilySearchResults

search_tool = TavilySearchResults(
    max_results=3,
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)

def web_search(query):
    results = search_tool.invoke(query)
    return str(results)