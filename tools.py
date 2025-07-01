# tools.py
import os
from datetime import datetime
from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun

# 1️⃣ Web search tool
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for current information."
)

# 2️⃣ Save-to-file tool
def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    try:
        filepath = os.path.join(os.getcwd(), filename)
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text = f"--- Research Output ---\nTimestamp: {ts}\n\n{data}\n\n"
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(text)
        return f"Data saved to {filepath}"
    except Exception as e:
        return f"Error saving data: {e}"

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Save research summary to a text file."
)
