#pip install langchain_ollama
from langchain_ollama import ChatOllama

class ModeloGemma():
    def __init__(self):
        self.modelo = ChatOllama(model="gemma2:2b", temperature=0.2)

    def generar_respuesta(self,prompt):
        respuesta = self.modelo.invoke(prompt)
        return respuesta.text