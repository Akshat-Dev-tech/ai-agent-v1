from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_ollama import OllamaLLM
load_dotenv()

#gpt model
# llm1 = ChatOpenAI(model="gpt-3.5-turbo")
# response = llm1.invoke("What is the capital of France?")
# print("OpenAI Response:", response)

# Use the correct Claude model name
# llm2 = ChatAnthropic(model="claude-3-sonnet-20240229")
# response = llm2.invoke("What is the capital of France?")
# print(response)


# llm_ollama = OllamaLLM(model="llama2")
# response = llm_ollama.invoke("What is the capital of France?")
# print("Ollama Response:", response)



