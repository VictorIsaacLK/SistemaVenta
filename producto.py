import lista

class Producto(lista.Lista):
    def __init__(self, nombre = "", codigo = "", descripcion = "", precio = 0.0):
        self._nombre = nombre
        self._codigo = codigo
        self._descripcion = descripcion
        self._precio = precio
        super().__init__()
        
        
    #-------------------------PROPIEDADES------------------------------#
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def set_nombre(self, valor):
        self._nombre = valor
    
    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def set_codigo(self, valor):
        self._codigo = valor
    
    @property
    def descripcion(self):
        return self._descripcion
    @descripcion.setter
    def set_descripcion(self, valor):
        self._descripcion = valor
    
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def set_precio(self, valor):
        self._precio = valor
        
    #-------------------------------------------------------------------#
    
    #-------------------------------STR---------------------------------#
    
    def __str__(self):
        return "Nombre: " + self._nombre + "\nCodigo: " + self._codigo + "\nDescripcion: " + self._descripcion + "\nPrecio: " + str(self._precio)

    
    #-------------------------------------------------------------------#
    
    #----------------------------METODOS--------------------------------#
    
    def agregarProductoLista(self, objeto):
        super().agregarObjeto(objeto)
    
    def mostrarListaDeProductos(self):
        lista = super().devolverLista()
        if len(lista) > 0:
            print(lista)
        else:
            print("No hay productos en la lista")
        
    # def convertirListaProductos_A_Diccionario(self):
    #     return super().convertirProductoADiccionario()
    
    #Este metodo se usa para convertir a diccionario la lista, el metodo de arriba no funciono debido a que se trato de realizar dentro de la lista, sin tener una lista   
    def diccionario(self):
        return super().enviarListaADiccionarioObjetos(super().devolverLista())
    
    def mostrarDiccionario(self):
        diccionarioProductos = self.diccionario()
        print(diccionarioProductos)
    
    def conversionAJson(self):
        diccionarioProductos = self.diccionario()
        super().enviarDiccionarioYAlmacenamientoJson("productos.json", diccionarioProductos)
        
    def traerJson(self):
      if super().cargarListaJson("productos.json") == False:
            print("No existe ningun producto actualmente")
      else:
          return super().cargarListaJson("productos.json")
  
        
        
    def cargarListaJson(self):
        if super().cargarListaJson("productos.json") == False:
            print("No existe ningun producto actualmente")
        else:
            nuevaLista = super().cargarListaJson("productos.json")
            for productoIndividual in nuevaLista:   
                nombre = productoIndividual["_nombre"]
                codigo = productoIndividual["_codigo"]
                descripcion = productoIndividual["_descripcion"]
                precio = productoIndividual["_precio"]
                producto = Producto(nombre, codigo, descripcion, precio)
                self.agregarProductoLista(producto)
    
    def cargarListaJsonTemporal(self, lista):
        listaola = []
        for productoIndividual in lista:   
            nombre = productoIndividual["_nombre"]
            codigo = productoIndividual["_codigo"]
            descripcion = productoIndividual["_descripcion"]
            precio = productoIndividual["_precio"]
            producto = Producto(nombre, codigo, descripcion, precio)
            listaola.append(producto)
            print(producto)  
        listaoli= super().enviarListaADiccionarioObjetos(listaola)
        # print(listaoli)
        super().enviarDiccionarioYAlmacenamientoJson("productos.json", listaoli)
        return listaoli      
            
    def cambiarPropiedad(self, valorAntiguo, nuevoValor):
        lista = super().devolverLista()
        for productoIndividual in lista:
            if productoIndividual._nombre == valorAntiguo:
                print("primer If nombre")
                productoIndividual._nombre = nuevoValor
            elif productoIndividual._codigo == valorAntiguo:
                print("segundo If codigo")
                productoIndividual._codigo = nuevoValor
            elif productoIndividual._descripcion == valorAntiguo:
                print("tercer If descripcion")
                productoIndividual._descripcion = nuevoValor
            elif productoIndividual._precio == valorAntiguo:
                print("cuarto If precio")
                productoIndividual._precio = nuevoValor
        print("Se ha realizado de manera adecuada el proceso")
        self.diccionario()
        
    def eliminarProducto(self, valor):
        lista = super().devolverLista()
        lista[:] = [producto for producto in lista if producto._nombre != valor]
        self.diccionario()
        
    def enviarLista(self):
        return super().devolverLista()
        
        
    #-------------------------------------------------------------------#