# Importamos la librería para trabajar con carpetas y archivos
import os

# Función que cuenta los archivos en una ruta dada
def contar_archivos(ruta):
    total_archivos = 0
    tipos = {}

    # Recorremos todas las subcarpetas y archivos
    for carpeta_raiz, subcarpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            total_archivos += 1
            extension = os.path.splitext(archivo)[1]
            if extension in tipos:
                tipos[extension] += 1
            else:
                tipos[extension] = 1

    # Mostramos resultados
    print(f"\nTotal de archivos: {total_archivos}")
    for tipo, cantidad in tipos.items():
        print(f"Tipo {tipo}: {cantidad} archivo(s)")

# Pedimos al usuario que ingrese la ruta
if __name__ == "__main__":
    ruta_usuario = input("Ingrese la ruta de la carpeta: ")
    contar_archivos(ruta_usuario)
