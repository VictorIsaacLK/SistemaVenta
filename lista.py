import diccionario

class Lista(diccionario.Diccionario):
    def __init__(self):
        self.listaObjetos = []
        super().__init__()     
    
    #------------------------------METODOS-------------------------------#
    
    def agregarObjeto(self, objeto):
        self.listaObjetos.append(objeto)
    
    def devolverLista(self):
        return self.listaObjetos
    
    def enviarListaADiccionarioObjetos(self, objetoList):
        return super().convertirProductoADiccionario(objetoList)
    
    def enviarListaADiccionarioClientes(self, objetoList):
        return super().convertirClienteADiccionario(objetoList)
    
    def enviarListaADiccionarioVentas(self, objetoList):
        return super().convertirVentaADiccionario(objetoList)
    
    def enviarDiccionarioYAlmacenamientoJson(self, almacenamiento, diccionario):
        super().convertirDiccionario_A_Json(almacenamiento, diccionario)
        

    #-------------------------------------------------------------------#
       
    