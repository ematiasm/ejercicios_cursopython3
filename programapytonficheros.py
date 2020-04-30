import modulosficheros

nombre_fichero = "fichero1.txt"

fichero = modulosficheros.Fichero(nombre_fichero)

texto = "Esto es la primera fila del fichero"
texto_agregado = "Esta es otra linea de texto"

fichero.grabar_fichero(texto)

fichero.agregar_fichero(texto_agregado)

texto_fichero = fichero.leer_fichero()

print(texto_fichero)
