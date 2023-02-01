"""
    Programa7
    Nombre:Cesar Ivan Bustamante 
    Herrera
    Fecha:30/01/2023
    Descripcion; Comparar 2 numeros 
    enteros e imprimir el numero mayor
"""

numero1=int(input("Ingresa el numero 1: ")) # Estamos declarando la variable del primer numero a comparar

numero2= int(input("Ingresa el numero 2: ")) # La segunda variable a comparar

if numero1 > numero2: # Condicion para la comparacion 
  print(numero1) # Imprime el resultado de la condicion
  

elif numero2 > numero1: # Condicion 2 de la comparacion
  print(numero2) # Impresion del resultado de la segunda condicion, esta se ejecuta si la primera no es valida

elif numero1 == numero2: # Condicion en caso de que los numeros sean iguales
  print ("***") # Aqui esta imprimiendo un signo que indica que la comparacion esta mal

