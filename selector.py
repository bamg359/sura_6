



# Civica 1. viajero frecuente  viajes >=  3 veces a la semana
# Civica 2. Ocasional viajes < 3 
# Civica 3. Estudiante 
# Civica 4. Tercera Edad
# Civica 5. Eventual
# Civica default Caso no valido


option = int(input("Caso"))

match option:
    case 1:
        print("Viajero frecuente")
    case 2:
        print("Viajero Ocasional")
    case 3:
        print("Estudiante")
    case 4:
        print("Tercera Edad")
    case 5:
        print("Viajero Eventual")      
    case _:
        print("Ingrese un case valido")         
