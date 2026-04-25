def productos_en_comun(lista_1: list, lista_2: list) -> list:
    """
    Obtiene los productos que están presentes en ambas listas sin repetir.

    PARÁMETROS:
    lista_1 (list): lista de productos del primer usuario
    lista_2 (list): lista de productos del segundo usuario

    RETORNO:
    list: lista con los productos en común entre ambas listas
    """
    comun = []

    for primer_producto_comun in range(len(lista_1)):
        for segundo_producto_comun in range(len(lista_2)):
            if lista_1[primer_producto_comun] == lista_2[segundo_producto_comun]:

                existe = False
                for comun_2 in range(len(comun)):
                    if comun[comun_2] == lista_1[primer_producto_comun]:
                        existe = True

                if existe == False:
                    comun += [lista_1[primer_producto_comun]]

    return comun


def productos_exclusivos(lista_1: list, lista_2: list) -> list:
    """
    Obtiene los productos que están en la primera lista pero no en la segunda.

    PARÁMETROS:
    lista_1 (list): lista de productos del primer usuario
    lista_2 (list): lista de productos del segundo usuario

    RETORNO:
    list: lista con los productos exclusivos de lista_1
    """
    exclusivos = []

    for producto_exclusivo in range(len(lista_1)):
        encontrado = False

        for producto_exclusivo_2 in range(len(lista_2)):
            if lista_1[producto_exclusivo] == lista_2[producto_exclusivo_2]:
                encontrado = True

        if encontrado == False:
            exclusivos += [lista_1[producto_exclusivo]]

    return exclusivos


def catalogo_total(lista_1: list, lista_2: list) -> list:
    """
    Genera una lista con todos los productos de ambas listas sin repetir.

    PARÁMETROS:
    lista_1 (list): lista de productos del primer usuario
    lista_2 (list): lista de productos del segundo usuario

    RETORNO:
    list: lista con todos los productos sin duplicados
    """
    total = []

    # copiar lista1
    for catalogo in range(len(lista_1)):
        total += [lista_1[catalogo]]

    # agregar lista2 sin repetir
    for catalogo in range(len(lista_2)):
        existe = False

        for segundo_catalago in range(len(total)):
            if lista_2[catalogo] == total[segundo_catalago]:
                existe = True

        if existe == False:
            total += [lista_2[catalogo]]

    return total


def recomendar(exclusivos_otro: list) -> list:
    """
    Genera una lista de recomendaciones basada en los productos exclusivos de otro usuario.

    PARÁMETROS:
    exclusivos_otro (list): lista de productos que el otro usuario tiene y este no

    RETORNO:
    list: lista de productos recomendados
    """
    recomendaciones = []

    for recomendacion_usuario in range(len(exclusivos_otro)):
        recomendaciones += [exclusivos_otro[recomendacion_usuario]]

    return recomendaciones