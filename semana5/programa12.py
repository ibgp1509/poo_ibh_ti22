 """
    Programa12 -
    Nombre:Cesar Ivan Bustamante 
    Herrera
    Fecha:14/02/2023
    Descripcion; Herencia
  
"""
class Persona: # Se esta creando la clase Persona
    __nombre = None # Definiendo la variable privada nombre
    def __init__(self): 
     print("Persona") # Se imprimira el texto en comillas

class Alumno (Persona): # Se esta definiendo la clase Alumno
   def __init__(self):
      super().__init__() # Variable que tomara el valor de la varibale 
      print("Alumno") # Imprimira lo que esta dentro de las comillas

objeto_persona=Persona() #Se esta creando el objeto persona
objeto_alumno=Alumno() # Se esta creando el objeto alumno

objeto_persona.nombre="Dejah" # Se esta definiendo y dando valor al obejeto dependiendo la variable
print(objeto_persona.nombre)

objeto_alumno.nombre="John Carter" # Se le esta dando vallr al objeto respecto a la variable
print(objeto_alumno.nombre) # Se imprimira el valor dentro del print

objeto_alumno.email="john@utectulancingo.edu.mx"
print(objeto_alumno.email)