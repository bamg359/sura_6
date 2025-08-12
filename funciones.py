


## Funciones son bloques de codigo que encapsulan funcionalidades y luego nos permites
# usarlas , solo llamando la funcion , en cualquier parte que la necesitemos.







# Funciones sin retorno , sin argumentos
def imprimir_usuario():
    list_usuario = ["andres", "juan", "Maria"]
    print(list_usuario)


imprimir_usuario()
print("------------------")
print("------------------")
imprimir_usuario() 
print("------------------")
print("------------------")
print("------------------")
imprimir_usuario()  

# Funciones sin retorno , con argumentos

list_saldo_usuarios = [5000, -3000, 0]

def imprimir_saldos_usuario(list_saldo):
    print(list_saldo)

imprimir_saldos_usuario(list_saldo_usuarios)

# Funciones con retorno , sin argumentos


def calcular_saldo():
    saldo = 5000
    viaje = 3400
    saldo -= viaje 
    return saldo 

print(calcular_saldo())
nuevo_saldo = calcular_saldo()
print(nuevo_saldo)

# Funciones con retorno , con argumentos

saldo = 10000
viaje = 3400

def calcular_saldo(saldo, viaje):
    saldo -= viaje 
    return saldo 



print(calcular_saldo(saldo , viaje))
nuevo_saldo = calcular_saldo(saldo , viaje)
print(nuevo_saldo)