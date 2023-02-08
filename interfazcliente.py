import cliente, time, mongo
from termcolor import colored

class InterfazCliente():
    def __init__(self, clienteInstancia = cliente.Cliente(), mongoInstancia = mongo.MongoDB()):
        self.clienteInstancia = clienteInstancia
        self.mongoInstancia = mongoInstancia
        self.clienteInstancia.cargarListaClientes()
    
    def menuClientes(self):
        opcion = 0
        while opcion!= 9:
            print("---------------------------------------------------------------")
            print("[1] Ingresar Cliente\n[2] Ver Clientes Existentes\n[3] Cambiar valor de un Cliente\n[4] Eliminar Cliente\n[5] Buscar Cliente\n[6] Mongo\n[9] Salida")
            print("---------------------------------------------------------------")
            try:
                opcion = int(input("Opcion: "))
            except ValueError:
                print("Opcion no valida")
            print("---------------------------------------------------------------")
            if opcion == 1:
                self.ingresarCliente()
                opcion = 0
            if opcion == 2:
                self.mostrarListadoDeClientes()
                self.detente(1)
                opcion = 0
            if opcion == 3:
                self.cambiarPropiedadCliente()
                opcion = 0
            if opcion == 4:
                self.eliminarCliente()
                opcion = 0
            if opcion == 5:
                self.buscarCliente()
                self.detente(1)
                opcion = 0
            elif opcion == 6:
                self.mongoMenu()
                opcion = 0
    


    #-------------------------------CLIENTE----------------------------------------#

    def ingresarCliente(self):
        clienteObjeto = self.crearCliente()
        self.clienteInstancia.agregarClienteLista(clienteObjeto)
        self.clienteInstancia.conversionAJson()
        

    def crearCliente(self):
        nombre = str(input("Ingresar el nombre del Cliente: "))
        rfc = str(input("Ingresar el RFC del Cliente: "))
        descripcion = str(input("Ingresar el telefono del CLiente: "))
        clie = cliente.Cliente(nombre, rfc, descripcion)
        return clie
        
    def mostrarListadoDeClientes(self):
        try:
            diccionarioClientes = self.clienteInstancia.diccionario()
            nombre_max_len = max([len(cn['nombre']) for cn in diccionarioClientes])
            rfc_max_len = max([len(cr['rfc']) for cr in diccionarioClientes])
            telefono_max_len = max([len(ct['telefono']) for ct in diccionarioClientes])
            
            print('-' * (nombre_max_len + rfc_max_len + telefono_max_len + 10))
            print(colored('| {0:^{1}} | {2:^{3}} | {4:^{5}} |'.format('Nombre', nombre_max_len, 'RFC', rfc_max_len, 'Telefono', telefono_max_len), "yellow"))
            print('-' * (nombre_max_len + rfc_max_len + telefono_max_len + 10))
            
            for cliente in diccionarioClientes:
                print('| {0:^{1}} | {2:^{3}} | {4:^{5}} |'.format(cliente['nombre'], nombre_max_len, cliente['rfc'], rfc_max_len, cliente['telefono'], telefono_max_len))
                print('-' * (nombre_max_len + rfc_max_len + telefono_max_len + 10))
        except:
            print("No hay clientes registrados")
        
    def cambiarPropiedadCliente(self):
        opcion = 0
        while opcion != 9:
            print("---------------------------------------------------------------")
            print("Seleccione el campo que va a cambiar")
            print("[1] Nombre\n[2] RFC\n[3] Telefono\n[9] Salir")
            try:
                opcion = int(input("Opcion: "))
            except ValueError:
                print("Opcion no valida")
            print("---------------------------------------------------------------")
            if opcion == 1:
                nombre = str(input("Ingrese el nombre de la persona que va a modificar: "))
                nuevoNombre = str(input("Seleccione el nuevo nombre de la persona: "))
                cambio = self.clienteInstancia.cambiarNombreCliente(nombre, nuevoNombre)
                if cambio == True:
                    print("El cambio fue realizado con exito!")
                elif cambio == False:
                    print("No existe un cliente con ese nombre")
                opcion = 0
            if opcion == 2:
                rfc = str(input("Ingrese el RFC de la persona que va a modificar: "))
                nuevoRfc = str(input("Ingrese el nuevo RFC de la persona: "))
                cambio2 = self.clienteInstancia.cambiarRfcCliente(rfc, nuevoRfc)
                if cambio2 == True:
                    print("El cambio fue realizado con exito!")
                elif cambio2 == False:
                    print("No existe un cliente con ese RFC")
                opcion = 0
            if opcion == 3:
                telefono = str(input("Ingrese el telefono del Cliente que va a modificar: "))
                nuevoTelefono = str(input("Ingrese el nuevo telefono del Cliente: "))
                cambio3 = self.clienteInstancia.cambiarTelefonoCliente(telefono, nuevoTelefono)
                if cambio3 == True:
                    print("El cambio fue realizado con exito!")
                elif cambio3 == False:
                    print("No existe un cliente con ese telefono")
            self.clienteInstancia.conversionAJson()
            opcion = 0
                    
    def eliminarCliente(self):
        print("---------------------------------------------------------------")
        nombre = str(input("Ingrese el nombre del Cliente a eliminar: "))
        print("---------------------------------------------------------------")
        self.clienteInstancia.eliminarCliente(nombre)
        self.clienteInstancia.conversionAJson()
        
    def buscarCliente(self):
        print("---------------------------------------------------------------")
        nombre = str(input("Ingrese el nombre del Cliente a buscar: "))
        print("---------------------------------------------------------------")
        client = self.clienteInstancia.buscarCliente(nombre)
        if client == False:
            print("Dicho cliente no existe")

    def devolverListaCliente(self):
        return self.clienteInstancia.enviarLista()
    
    def devolverDiccionarioCliente(self):
        return self.clienteInstancia.diccionario()
    
    def detente(self, segundos):
        time.sleep(segundos)
        
        
    #-------------------------------MONGODB----------------------------------------#
    def mongoMenu(self):
        opcion = 0
        while opcion!= 9:
            print("---------------------------------------------------------------")
            print("----------------------- MONGO INTERFAZ ------------------------")
            print(colored("[1] Conectar a Mongo\n[2] Guardar clientes\n[3] Cerrar conexion\n[9] Salida", "red"))
            print("---------------------------------------------------------------")
            try:
                opcion = int(input("Opcion: "))
            except ValueError:
                print("Opcion no valida")
            if opcion == 1:
                self.conexion()
                opcion = 0
            elif opcion == 2:
                self.guardarDatosEnMongo()
                opcion = 0
            elif opcion == 3:
                self.mongoInstancia.cerrarConexion()
        
    
    
    def conexion(self):
            conn = self.mongoInstancia.connect("conexion_base_datos")
            if conn == False:
                print("Error al conectar con la base de datos")
            else:
                print("Conectado con la base de datos")
                # self.subirMongo()
        
    def mirarMongo(self):
        self.mongoInstancia.hacerFind()
        
    def guardarDatosEnMongo(self):
        jsontemporal = self.mongoInstancia.cargarListaJson("clientesTemporales.json")
        if jsontemporal == False:
            print("No existe ningun producto temporal actualmente")
            se_guardo = self.mongoInstancia.guardarEnMongoParaTodos('Tienda', 'Clientes', self.devolverDiccionarioCliente(), 'clientes.json', 'clientesTemporales.json')
            if se_guardo == False:
                print("No existe conexion con la base de datos, se han guardado los datos de manera temporal")
                # De aqui en adelante si exite la conexion, al menos en este if, es cuando no existe ar temporal, pero si conexion            
            else:
                print("Se han guardado los datos de manera adecuada en ambos sistemas")
        else:
            nuevojsonjeje = self.clienteInstancia.cargarListaJsonTemporal(jsontemporal)
            # print(jsonTemporalConvertido)
            # el jsontemporal tiene que pasar por el convertidor, porque si no me esta jodiendo la json
            se_guardo = self.mongoInstancia.guardarEnMongoParaTodos('Tienda', 'Clientes', nuevojsonjeje, 'clientes.json', 'clientesTemporales.json')
            if se_guardo == False:
                print("Pu;etas")
            else:
                print("Se han guardado los datos de manera adecuada en ambos sistemas")
                self.mongoInstancia.borrarJson("clientesTemporales.json")
    
    #------------------------------------------------------------------------------#

