"""
    Programa15 -
    Nombre:Cesar Ivan Bustamante 
    Herrera
    Fecha:15/02/2023
    Descripcion; Importar clase
"""
from persona import Persona  # importa la clase persona 

class Profesor(Persona): #Crea la clase profesor que hereda de la clase persona
   def __init__(self) -> None:

    super().__init() # Llama al contructor de la clase persona
   print ("Profesor") # Impriome el texto de las comillas

objeto_profesor=Profesor() #Crea un onjetop de la clase profesor