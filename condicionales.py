

## Civica  => si el usuario tiene saldo se le permite ingresar el sistema 
# si el saldo es 0 debera recargar , pero si tiene menos de 3400 entoces puede entrar pero queda con 
# una saldo pendiente saldo negtivo
# si tiene el valor le descuenta los 3400 de la recarga 



saldo = -1400
pasaje = 3400

if saldo >= pasaje: 
    print("Bienvenido")
    #saldo = saldo - pasaje
    saldo -= pasaje
    print(f"su nuevo saldo es {saldo}")
elif saldo > 0 and saldo < pasaje:
    print("Bienvenido , Saldo pendiente") 
    saldo -= pasaje
    print(f"su nuevo saldo es {saldo}")   
else:
    print("Saldo insuficiente")    



print("tiene Saldo") if saldo > 0 else print("Saldo insufiente")


