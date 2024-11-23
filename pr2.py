print(" Fco. Santiago. Car. Cor")
print(" ")

def maslarga(listadepalabraas):
    palabralarga = listadepalabraas[0]
    for palabra in listadepalabraas:
        if len(palabra) > len(palabralarga):
            palabralarga = palabra
    print(f"La palabra mas larga en la lista es: '{palabralarga}'")
    return palabralarga

# asignando valores
palabras = ["manzana", "platano", "uva", "sandia"]
maslarga(palabras)

