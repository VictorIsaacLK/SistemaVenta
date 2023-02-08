import lista

class Cliente(lista.Lista):
    def __init__(self, nombre = "", rfc = "", telefono = ""):
        self.nombre = nombre
        self.rfc = rfc
        self.telefono = telefono
        super().__init__()
        
    
    #----------------------------METODOS--------------------------------#
    
    def agregarClienteLista(self, objeto):
        super().agregarObjeto(objeto)
        
    def mostrarListaDeClientes(self):
        lista = super().devolverLista()
        if len(lista) > 0:
            print(lista)
        else:
            print("No hay Clientes en la lista")
    
    def diccionario(self):
        return super().enviarListaADiccionarioClientes(super().devolverLista())
    
    def mostrarDiccionario(self):
        diccionarioClientes = self.diccionario()
        print(diccionarioClientes)
    
    def conversionAJson(self):
        diccionarioClientes = self.diccionario()
        super().enviarDiccionarioYAlmacenamientoJson("clientes.json", diccionarioClientes)
        
    def cargarListaClientes(self):
        if super().cargarListaJson("clientes.json") == False:
            print("No existen clientes actualmente")
        else:
            nuevaLista = super().cargarListaJson("clientes.json")
            for clienteIndividual in nuevaLista:   
                nombre = clienteIndividual["nombre"]
                rfc = clienteIndividual["rfc"]
                telefono = clienteIndividual["telefono"]
                cliente = Cliente(nombre, rfc, telefono)
                self.agregarClienteLista(cliente)
    
    def cargarListaJsonTemporal(self, lista):
        listaNuevaDondeGuardamos = []
        for clienteIndividual in lista:   
            nombre = clienteIndividual["nombre"]
            rfc = clienteIndividual["rfc"]
            telefono = clienteIndividual["telefono"]
            cliente = Cliente(nombre, rfc, telefono)
            listaNuevaDondeGuardamos.append(cliente)
        listaoli= super().enviarListaADiccionarioClientes(listaNuevaDondeGuardamos)
        super().enviarDiccionarioYAlmacenamientoJson("clientes.json", listaoli)
        return listaoli 
            
    def cambiarNombreCliente(self, nombre, nuevoNombre):
        lista = super().devolverLista()
        for cliente in lista:
            if cliente.nombre == nombre:
                print("Primer If nombre")
                cliente.nombre = nuevoNombre
                return True
        return False
    
    def cambiarRfcCliente(self, rfc, nuevoRfc):
        lista = super().devolverLista()
        for cliente in lista:
            if cliente.rfc == rfc:
                print("Primer If rfc")
                cliente.rfc = nuevoRfc
                return True
        return False
    
    def cambiarTelefonoCliente(self, telefono, nuevoTelefono):
        lista = super().devolverLista()
        for cliente in lista:
            if cliente.telefono == telefono:
                print("Primer If telefono")
                cliente.telefono = nuevoTelefono
                return True
        return False
    
    
    def eliminarCliente(self, valor):
        lista = super().devolverLista()
        lista[:] = [cliente for cliente in lista if cliente.nombre != valor]
        self.diccionario()
        
    def buscarCliente(self, valor):
        lista = super().devolverLista()
        for cliente in lista:
            if cliente.nombre == valor:
                print("Nombre del Cliente:", cliente.nombre)
                print("RFC del Cliente:", cliente.rfc)
                print("Telefono del Cliente:", cliente.telefono)
                return True
        return False
    
    def enviarLista(self):
        return super().devolverLista()
        
        
    #-------------------------------------------------------------------#
