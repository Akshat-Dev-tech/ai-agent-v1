from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
# from langchain_ollama import OllamaLLM
from langchain_ollama import ChatOllama 
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
import json
load_dotenv()

#gpt model
# llm1 = ChatOpenAI(model="gpt-3.5-turbo")
# response = llm1.invoke("What is the capital of France?")
# print("OpenAI Response:", response)

# Use the correct Claude model name
# llm2 = ChatAnthropic(model="claude-3-sonnet-20240229")
# response = llm2.invoke("What is the capital of France?")
# print(response)

class Response(BaseModel):
    topic:str
    summary:str
    sources: list[str]
    tools_used: list[str]


# ollama pull llama3
# ollama run llama3
llm_ollama = ChatOllama(model="llama3")
parser=PydanticOutputParser(pydantic_object=Response)

# In format_instructions will pass the format for the output which is defined in Response class
# This will be used to format the output of the agent -> partial(format_instructions=parser.get_format_instructions())

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"), #autofill this value
        ("human", "{query}"), #passed from the user
        ("placeholder", "{agent_scratchpad}"), #autofill this value
    ]
).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(
    llm=llm_ollama,
    prompt=prompt,
    tools=[]
)

agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)
raw_query = "What is the capital of France?"
response = agent_executor.invoke({"query": raw_query, "chat_history": []})
print("Ollama Response:",response)


# response = llm_ollama.invoke("What is the capital of France?")
# print("Ollama Response:", response)

