# main.py
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, save_tool

load_dotenv()

# Response schema
class Response(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Initialize tool-capable LLM
llm = ChatOllama(model="llama3.1:8b", temperature=0)
parser = PydanticOutputParser(pydantic_object=Response)

# Agent prompt with explicit instructions
prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a research assistant. "
        "When asked, use **search** to fetch info and **save_text_to_file** to save your summary. "
        "Output must be JSON matching the schema:\n{format_instructions}"
    )),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions())

# Build agent
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=[search_tool, save_tool])
executor = AgentExecutor(agent=agent, tools=[search_tool, save_tool], verbose=True)

# Run the agent
response = executor.invoke({
    "query": "Tell me about sharks and save the data.",
    "chat_history": []
})
print("Agent Response:\n", response)
