from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

class Prompt_03:
    def __init__(self):
        modelo = ChatOllama(
            model="qwen2.5:3b", 
            temperature=0
        )
    