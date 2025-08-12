

# Esto es un comentario
""" 
comentario 
multilinea
"""

saludo:str = "Hola Mundo"
numero:int = 23 
nota:float = 4.5
estaActivo: bool = True

respuesta = "Hola" 
num2 = 34
grados = 28.9
presente = False

#Listas , tuplas , diccionarios , conjuntos

lista = ["Hola", 34 , 28.9 , False] # Son dinámicas, son mutables 

tupla = ("Amarillo","Azul","rojo") # no es mutable

print(tupla)

diccionario = {"Saludo":"Hola Mundo", "Grados Celcius": 21.3 , "Turno" : 30 , "Disponible": False}

conjunto = { 0,1,2,3,4,5,6,7,8,9}


print(type(conjunto))

#Casting de variables 

numero = "23" 

print(type(numero)) # casting de variables 

numero = int("23")

print(type(numero))

lista_tupla = list(tupla)

print(type(lista_tupla))

print(lista_tupla)


nombre = input("Escriba su nombre: ")

edad = int(input("Ingrese edad"))

print("Nombre: ", nombre) # concatenación

print("Nombre: " + nombre) #solo para string 

print(f"Edad: {edad}") # Formato

## Crear un formulario de registro productos, clientes , cursoc, al menos 7 variables