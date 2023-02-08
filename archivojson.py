import json

class ArchivoJson():
    
    #----------------------------METODOS--------------------------------#
    
    def guardarListaEnJson(self, almacenamiento, diccionario):
        with open(almacenamiento, 'w') as archivo:
            json.dump(diccionario, archivo, indent=4)
            
    def cargarListaJson(self, almacenamiento):
        try:
            with open(almacenamiento, 'r') as archivo:
                data = json.load(archivo)
            #dataDiccionario = json.loads(data)
            #listaDeDatos = list(dataDiccionario.values())
            return data
        except:
            return False
    #--------------------------------------------------------------------#   