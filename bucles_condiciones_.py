frutas = { "manzana":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon"}

valor = frutas ["naranja"]
print(valor)

frutas ["piña"] = "pineapple"
print(frutas)

for key,valor in frutas.items():
    print (f"{key} en inglés es {valor}")