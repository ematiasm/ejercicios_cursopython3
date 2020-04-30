class Fichero:
    def __init__(self, nombre):
        self.nombre = nombre
    #Grabar un fichero
    def grabar_fichero(self, texto):
        fichero = open(self.nombre, "wt")
        fichero.write(texto)
        fichero.close()
    #agrega texto a un fichero
    def agregar_fichero(self, texto):
        fichero = open(self.nombre, "at")
        fichero.write(texto)
        fichero.close()
    #lee un fichero
    def leer_fichero(self):
        fichero = open(self.nombre, "rt")
        texto = fichero.read()
        return texto
