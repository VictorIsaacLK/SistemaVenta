import archivojson

class Diccionario(archivojson.ArchivoJson):
    def __init__(self):
        super().__init__()
        
        
    #----------------------------METODOS--------------------------------#

    def convertirProductoADiccionario(self, lista):
        return [{'_nombre': objeto._nombre, '_codigo': objeto._codigo, '_descripcion': objeto._descripcion, '_precio': objeto._precio} for objeto in lista]
    
    def convertirClienteADiccionario(self, lista):
        return [{'nombre' : objeto.nombre, 'rfc' : objeto.rfc, 'telefono' : objeto.telefono} for objeto in lista]
    
    def convertirVentaADiccionario(self, lista):
       return [{'cliente' : objeto['cliente'], 'productos': objeto['productos'], 'fecha': objeto['fecha']} for objeto in lista]
   
    def convertirDiccionario_A_Json(self, almacenamiento, diccionario):
       super().guardarListaEnJson(almacenamiento, diccionario)
       
   #--------------------------------------------------------------------# 