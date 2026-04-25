def es_letra(caracter: str) -> bool:
    """
    Verifica si un carácter es una letra del alfabeto (mayúscula o minúscula).

    PARÁMETROS:
    caracter (str): carácter a evaluar

    RETORNO:
    bool: True si es letra, False en caso contrario
    """
    es_valido = False

    if (caracter >= "a" and caracter <= "z") or (caracter >= "A" and caracter <= "Z"):
        es_valido = True

    return es_valido


def validar_cadena(cadena: str) -> str:
    """
    Valida que la cadena ingresada:
    - no esté vacía
    - contenga únicamente letras

    PARÁMETROS:
    cadena (str): texto ingresado por el usuario

    RETORNO:
    str: cadena validada si cumple las condiciones
    None: si la cadena es inválida
    """
    retorno = None

    if cadena != "":
        solo_letras = True

        for cadena_2 in range(len(cadena)):
            if es_letra(cadena[cadena_2]) == False:
                solo_letras = False

        if solo_letras == True:
            retorno = cadena

    return retorno


def pedir_producto() -> str:
    """
    Solicita al usuario el ingreso de un producto y valida que sea correcto.

    La función repite el pedido hasta que el usuario ingrese una cadena válida,
    es decir, que contenga únicamente letras y no esté vacía.

    PARÁMETROS:
    No recibe parámetros.

    RETORNO:
    str: producto ingresado y validado
    """
    producto = None

    while producto == None:
        entrada = input("Ingrese producto: ")
        validado = validar_cadena(entrada)

        if validado != None:
            producto = validado
        else:
            print("Error. Solo se permiten letras (sin números ni símbolos).")

    return producto


def cargar_lista() -> list:
    """
    Permite cargar una lista de productos ingresados por el usuario.

    La función solicita productos uno por uno utilizando la función pedir_producto()
    y los agrega a una lista. El proceso se repite mientras el usuario indique
    que desea continuar.

    PARÁMETROS:
    No recibe parámetros.

    RETORNO:
    list: lista de productos ingresados por el usuario
    """
    lista = []
    continuar = "si"

    while continuar == "si":

        producto = pedir_producto()
        lista += [producto]

        continuar = input("Desea agregar otro producto? (si/no): ")

    return lista
