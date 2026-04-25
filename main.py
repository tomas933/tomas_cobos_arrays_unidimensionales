from funciones import productos_en_comun, productos_exclusivos, catalogo_total, recomendar
from validaciones import cargar_lista


def main():
    opcion = ""

    while opcion != "1" and opcion != "2":
        print("1. Usar datos de prueba")
        print("2. Ingresar productos manualmente")
        opcion = input("Selecciones una opcion: ")

    match opcion:
        case "1":
        # LISTAS PREDEFINIDAS
            usuario_1 = ["mouse", "teclado", "monitor", "parlantes"]
            usuario_2 = ["monitor", "auriculares", "mousepad", "teclado"]

        case "2":
            print("=== CARGA USUARIO 1 ===")
            usuario_1 = cargar_lista()

            print("=== CARGA USUARIO 2 ===")
            usuario_2 = cargar_lista()

    comun = productos_en_comun(usuario_1, usuario_2)

    exclusivos_usuario1 = productos_exclusivos(usuario_1, usuario_2)
    exclusivos_usuario2 = productos_exclusivos(usuario_2, usuario_1)

    catalogo = catalogo_total(usuario_1, usuario_2)

    recomendacion_usuario1 = recomendar(exclusivos_usuario2)
    recomendacion_usuario2 = recomendar(exclusivos_usuario1)

    print("\n--- RESULTADOS ---")
    print(f"Productos en común: {comun}")
    print(f"Exclusivos usuario 1: {exclusivos_usuario1}")
    print(f"Exclusivos usuario 2: {exclusivos_usuario2}")
    print(f"Catálogo total:{catalogo}")
    print(f"Recomendaciones para usuario 1: {recomendacion_usuario1}")
    print(f"Recomendaciones para usuario 2: {recomendacion_usuario2}")

if __name__ == "__main__":
    main()