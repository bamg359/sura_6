


## queremos que la maquina de consulta funcione para que distintos clientes al ingresar la tarjeta le 
## diga el tipo de viajero que es


init = int(input("1. iniciar maquina 0. apagar"))

while init != 0:

    opt = int(input("Seleccione 1. validar tipo viajero 2. pagar pasaje 3. salir"))

    match opt:
        case 1:
            print("Validar tipo viajero")

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
        case 2:
            print("Cerrar Sistema")
            init = 0 
        case _:
            print("Ingrese una opción valida") 
            init = 0        




        
    
                            
