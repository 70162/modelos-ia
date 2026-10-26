from src.modelos.modelo_google import ModeloGoople
from src.modelos.modelo_groq import ModeloGroq
from src.modelos.modelo_local import ModeloLocal
from src.modelos.modelo_gemma import ModeloGemma
from src.modelos.prompt_01 import Prompt01
from src.modelos.prompt_02 import Prompt_02

import os
from rich.console import Console
from rich.markdown import Markdown

class MenuPrincipal():
    def __init__(self):
        self.console = Console()
        self.opcion = 0

    @staticmethod
    def limpiar_pantalla():
        os.system("cls" if os.name == "nt" else "clear")
    @staticmethod
    def pausar():
        input("\nPresione Enter para volver al menú...")

    def mostrar_menu(self):
        print("=== Menú Principal ===") 
        print("1. Modelo Google API KEY")
        print("2. Modelo Groq API KEY")
        print("3. Modelo Local (Ollama)")
        print("4. Modelo Gemma")
        print("5. Prompt básico")
        print("6. Prompt template")
        print("0. Salir")

    def ejecutar_opcion(self):
        while True:
            self.limpiar_pantalla()
            self.mostrar_menu()
            self.opcion = input("Seleccione una opción: ")

            if self.opcion == "1":
                modelo_google = ModeloGoople()
                prompt = input("Ingrese su prompt: ")
                respuesta = modelo_google.generar_respuesta(prompt)
                print("Respuesta del modelo Google:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))
                

            elif self.opcion == "2":
                modelo_groq = ModeloGroq()
                prompt = input("Ingrese su prompt: ")
                respuesta = modelo_groq.generar_respuesta(prompt)
                print("Respuesta del modelo Groq:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion == "3":
                modelo_local = ModeloLocal()
                prompt = input("Ingrese su prompt: ")
                respuesta = modelo_local.generar_respuesta(prompt)
                print("Respuesta del modelo Local:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion == "4":
                modelo_gemma = ModeloGemma()
                prompt = input("Ingrese su prompt: ")
                respuesta = modelo_gemma.generar_respuesta(prompt)
                print("Respuesta del modelo Gemma:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion == "5":
                prompt_01 = Prompt01()
                prompt = input("Ingrese su prompt: ")
                respuesta = prompt_01.generar_respuesta(prompt)
                print("Respuesta del Prompt básico:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion == "6":
                prompt_02 = Prompt_02()
                respuesta = prompt_02.generar_respuesta()
                print("Respuesta del Prompt template:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion == "0":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, selecciones una opción válida.")
            
            self.pausar()