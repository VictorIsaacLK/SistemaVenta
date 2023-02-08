import lista, datetime, cliente, time
from termcolor import colored

class Venta(lista.Lista):
    def __init__(self, fecha = datetime.date.today()):
        self.fecha = fecha
        super().__init__()
        
    
    #----------------------------METODOS--------------------------------#
    def agregarVentaLista(self, objeto):
        super().agregarObjeto(objeto)
        
    def detente(self, segundos):
        time.sleep(segundos)
        
    def ingresarCliente(self, listaO, nombre):
        listaComenzal = listaO
        for EachComenzal in listaComenzal:
            if EachComenzal.nombre == nombre:
                diccionario = {"nombre" : EachComenzal.nombre, "rfc": EachComenzal.rfc, "telefono": EachComenzal.telefono}
                return diccionario
        return False
    
    def construirVenta(self, listaP, clienteN, productosExistentes):
        listaProductosVerificada=self.verificarExistenciaProductos(listaP, productosExistentes)
        # print(listaProductosVerificada)
        # print(listaP)
        venta = {'cliente': clienteN, 'productos': listaProductosVerificada, 'fecha': format(self.fecha)}
        print("----------------------------------------------------------------")
        self.detente(1)
        # print(colored(venta, "green"))
        self.agregarVentaLista(venta)

    #En este metodo falta la verificacion de que exista el producto, despues pensare si es necesario o no, pero creo que no, solo es necesario cuando se va a hacer la compra, no cuando ya se hizo 05/02/23
    def cargarVenta(self, listaP, clienteN, fechaV):
        venta = {'cliente': clienteN, 'productos': listaP, 'fecha': fechaV}
        # self.detente(1)
        # print(colored(venta, "green"))
        self.agregarVentaLista(venta)
    
    def cargarVentaRetornable(self, listaP, clienteN, fechaV):
        venta = {'cliente': clienteN, 'productos': listaP, 'fecha': fechaV}
        # self.detente(1)
        # print(colored(venta, "green"))
        return venta
        
    def verificarExistenciaProductos(self, listaP, listaProductosExistentes):
        listaExistencia = []
        # for EachProducto in listaProductosExistentes:
        #     if EachProducto._nombre in listaP:
        #         listaExistencia.append(EachProducto)
        for nombreProducto in listaP:
            for producto in listaProductosExistentes:
                if nombreProducto in producto['_nombre']:
                    listaExistencia.append(producto)            
        return listaExistencia      
 
    def regresarVentaLista(self):
        return super().devolverLista()    
        
    def diccionario(self):
        return super().enviarListaADiccionarioVentas(self.regresarVentaLista())

    def mostrarDiccionario(self):
            diccionarioProductos = self.diccionario()
            print(diccionarioProductos)
            
    def conversionAJson(self, diccionario):
            diccionarioVentas = diccionario
            super().enviarDiccionarioYAlmacenamientoJson("ventas.json", diccionarioVentas)
            
    
    #-------------------------------------------------------------------#
