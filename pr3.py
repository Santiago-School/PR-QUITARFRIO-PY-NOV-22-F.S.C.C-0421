print(" Fco. Santiago. Car. Cor")
print(" ")

def filtrarpalabras(listapalabras, n):
    palabrasfiltradas = [palabra for palabra in listapalabras if len(palabra) > n]
    print(f"las palabras que tienen mas de {n} caracteres son: {palabrasfiltradas}")
    return palabrasfiltradas

# Asignando valores
palabras = ["manzana", "platano", "uva", "sandia"]
filtrarpalabras(palabras, 6)

