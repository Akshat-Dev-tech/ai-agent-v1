from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime


# This code is essentially giving your AI agent the ability to:
# Search the web using DuckDuckGo's search engine
# Get real-time information from the internet
# Return those results to answer questions that require current/live data
# Inbuilt tool
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information",
)

