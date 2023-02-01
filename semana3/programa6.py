"""
    Programa6 -
    Nombre:Cesar Ivan Bustamante 
    Herrera
    Fecha:31/01/2023
    Descripcion; Calcular el area de 
    un circulo
"""
print("--------AREA DEL CIRCULO----------")# Este es un separador para que el resultado no se vea  junto

pi=(3.1416)
radio=float(input("Escribe el valor del radio"))

area_circulo=pi*(radio ** 2)
print("El area del circulo con un radio de:{} es {}".format(radio, area_circulo))

print("--------PERIMETRO DEL CIRCULO----------")# Este es un separador para que el resultado no se vea junto

diametro=float(input("Escribe el diamtero"))
perimetro=(diametro * pi)
print("El perimetro del circulo es:", perimetro)



print("-----------AREA DEL CUADRADO----------------")# Este es un separador parea que el resultado no se vea todo junto

lado=float(input("Ingresa el lado ")) # Esta es otra forma con la funcion input, que te permite ingresar datos desde el teclado y ponerlas en uso ya que almacena y guarda los datos en la misma,  de primero se ingresa el : nombre de la variable = tipo de dato (input ("la indicacion")) 



print( " El area es de: " , lado * lado ) # Aqui estamos imprimiendo y ejecutanto el valor de lo que queremos saber, en este caso el area 
