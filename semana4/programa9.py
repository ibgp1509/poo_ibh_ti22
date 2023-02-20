"""
    Programa9 -
    Nombre:Cesar Ivan Bustamante 
    Herrera
    Fecha:08/02/2023
    Descripcion; Numero mayor por medio del def
"""
def mayor(numero1,numero2): #Definimos el mayor de los numeros
  if numero1 > numero2: # Se esta realizando una comparacion con numero1 y numero2
   print(numero1) # Va a imprimir el valor de la variable
  elif numero2 >  numero1:  #Se esta realizando una comparacion con numero1 y numero2
      print(numero2) 
  else:
   print(None)

mayor(3,2) # Resultado de cada una de las comparaciones
mayor(2,3) # Resultado de cada una de las comparaciones
mayor(3,3) # Resultado de cada una de las comparaciones
 
# Opcion 2

def mayor(numero1:int, numero2:int)->int: #Definimos el mayor de los numeros
    mayor = None
    if  numero1 > numero2:
         mayor = numero1
    elif  numero2 > numero1:
     else:
        mayor = None
  return mayor

print(mayor(3,2)) # Resultado de cada una de las comparaciones
print(mayor(2,3)) # Resultado de cada una de las comparaciones
print(mayor(3,3)) # Resultado de cada una de las comparaciones
    