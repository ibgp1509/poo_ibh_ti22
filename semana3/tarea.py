"""
    Programa1
    Nombre:Cesar Ivan Bustamante Herrera
    Fecha:30/01/2023
    Descripcion; Calcular el area de un triangulo
    """

base= 10   # Esta es una variable de tipo entera con valor definido
altura= 20 # Esta es otra variable conj valor definido
print("La base es de :{} la altura de :{} , el area se calcula como BASE * ALTURA /2, lo cual el area del triangulo es de : {}".format(base, altura,((base * altura)/2)))     # De esta manera  es con el format, donde los corchetes muestran en pantalla el valor que se les de a las variables, en el lugar que acomodes las variables, seran el valor que te muestran

print("---------------------------------------------")# Este es un sepoarador parea que el resultado no se vea todo junto

b=int(input("Ingresa la base ")) # Esta es otra forma con la funcion input, que te permite ingresar datos desde el teclado y ponerlas en uso ya que almacena y guarda los datos en la misma,  de primero se ingresa el : nombre de la variable = tipo de dato (input ("la indicacion")) 

a=int(input("Ingresa la altura ")) # Esta es la misma forma con el input solo que aqui esta pidiendo otro dato

print( " El area es de: " , b *a/2 ) # Aqui estamos imprimiendo y ejecutanto el valor de lo que queremos saber, en este caso el area 