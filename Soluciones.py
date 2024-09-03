def esPrimo(numero):
    # Un número primo solo es divisible por 1 y por el mismo
    # si hacemos un rango que vaya de 2 a mi numero menos 1 y
    # encontramos un divisor, significa que el número no es primo.
    for num in range(2, numero):
        if (numero % num) == 0:
            return False
    return True

def numHermano(numero):
    if not isinstance(numero, int):
        return "Error: el numero debe ser entero"
    
    contador = 0
    for num in range(1, numero+1):
        if (numero % num) == 0:
            if esPrimo(num):
                contador += 1
    
    if contador >= 2:
        return True
    
    return False