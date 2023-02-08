import venta, cliente, time, mongo
from termcolor import colored

class InterfazVenta():
    def __init__(self, listaClientes, listaProductos, diccionarioCliente, diccionarioProducto, ventaInstancia = venta.Venta(), clienteInstancia = cliente.Cliente(), mongoInstancia = mongo.MongoDB()):
        self.ventaInstancia = ventaInstancia
        self.clienteInstancia = clienteInstancia
        self.listaClientes = listaClientes
        self.listaProductos = listaProductos
        self.diccionarioCliente = diccionarioCliente
        self.diccionarioProducto = diccionarioProducto
        self.mongoInstancia = mongoInstancia
        self.cargarListaJson()
    
    #----------------------------------MENU-----------------------------------------#
    
    def detente(self, segundos):
        time.sleep(segundos)
    
    def menuVentas(self):
        opcion = 0
        while opcion!= 9:
            print("---------------------------------------------------------------")
            print("Bienvenido al sistema de Ventas, decida la opcion que necesite")
            print("[1] Agregar Venta\n[2] Ver ventas\n[3] Mongo\n[9] Salida")
            print("---------------------------------------------------------------")
            try:
                opcion = int(input("Opcion: "))
                print("---------------------------------------------------------------")
            except ValueError:
                print("Opcion no valida")
            if opcion == 1:
                self.agregarClienteVenta()
                opcion = 0
            elif opcion == 2:
                # self.ventaInstancia.mostrarDiccionario()
                self.tablaVentas()
                self.detente(1)
                opcion = 0
            elif opcion == 3:
                self.mongoMenu()
                opcion = 0


    #------------------------------------------------------------------------------#

    #---------------------------------VENTA----------------------------------------#


    def devolverDiccionarioVentas(self):
        return self.ventaInstancia.diccionario()

    # En estado de edicion, necesito que muestre una tabla con los datos de la persona
    def agregarClienteVenta(self):
        listaClientes = self.listaClientes
        # print(colored(self.diccionarioCliente, "magenta"))
        self.tablaClientes()
        print("---------------------------------------------------------------")
        nombreCliente = str(input("Ingrese el nombre del Cliente: "))
        print("---------------------------------------------------------------")
        se_ingreso = self.ventaInstancia.ingresarCliente(listaClientes, nombreCliente)
        self.detente(1)
        print("---------------------------------------------------------------")
        print("---------------------------------------------------------------")
        print("---------------------------------------------------------------")
        if se_ingreso == False:
            print("No existe este cliente")
            self.detente(1)
        else:
            listadoProductos = self.agregarProductos()
            self.ventaInstancia.construirVenta(listadoProductos, se_ingreso, self.diccionarioProducto)
            print("La venta se ha realizado con éxito!")
            self.detente(1)
            dicc = self.ventaInstancia.diccionario()
            self.ventaInstancia.conversionAJson(dicc)

    def agregarProductos(self):
        self.detente(1)
        listaProductos = self.diccionarioProducto
        print("Lista de productos disponibles")
        print("---------------------------------------------------------------")
        # print(colored(listaProductos, "red"))
        nombre_max_len = max([len(pn['_nombre']) for pn in listaProductos])
        codigo_max_len = max([len(pc['_codigo']) for pc in listaProductos])
        descripcion_max_len = max([len(pd['_descripcion']) for pd in listaProductos])
        precio_max_len = max([len(str(pp['_precio'])) for pp in listaProductos])
        
        print('-' * (nombre_max_len + codigo_max_len + descripcion_max_len + precio_max_len + 16))
        print(colored('| {0:^{1}} | {2:^{3}} | {4:^{5}} | {6:^{7}} |'.format('Nombre', nombre_max_len, 'Codigo', codigo_max_len, 'Descripcion', descripcion_max_len, 'Precio', precio_max_len), 'red'))
        print('-' * (nombre_max_len + codigo_max_len + descripcion_max_len + precio_max_len + 16))
        
        for producto in listaProductos:
            print('| {0:^{1}} | {2:^{3}} | {4:^{5}} | {6:^{7}} |'.format(producto['_nombre'], nombre_max_len, producto['_codigo'], codigo_max_len, producto['_descripcion'], descripcion_max_len, producto['_precio'], precio_max_len))
            print('-' * (nombre_max_len + codigo_max_len + descripcion_max_len + precio_max_len + 16))
            
        print("---------------------------------------------------------------")
        self.detente(2)
        print(colored("Recomendacion:\nSi agrega mas de un producto, separelos por coma y SIN espacio", "green"))
        print("Ejemplo: ")
        print(colored("Pollo frito,Papas de jamon", "cyan"))
        self.detente(2)
        print("---------------------------------------------------------------")
        arrayDeObjetos = input("Agregue el nombre de los productos comprados: ")  
        l = list(map(str, arrayDeObjetos.split(',')))
        return l
    
    def cargarListaJson(self):
        if self.ventaInstancia.cargarListaJson("ventas.json") == False:
            print("No existen ventas en el sistema actual")
        else: 
            listaRecargada = self.ventaInstancia.cargarListaJson("ventas.json")
            for cadaVenta in listaRecargada:
                cliente = cadaVenta["cliente"]
                productos = cadaVenta["productos"]
                fecha = cadaVenta["fecha"]
                self.ventaInstancia.cargarVenta(productos, cliente, fecha)      
                # self.ventaInstancia.construirVenta(productos, cliente, self.diccionarioProducto)
                
    def cargarListaJsonTemporal(self, lista):
        listaNuevaDondeGuardamos = []
        for cadaVenta in lista:
            cliente = cadaVenta["cliente"]
            productos = cadaVenta["productos"]
            fecha = cadaVenta["fecha"]
            venta = self.ventaInstancia.cargarVentaRetornable(productos, cliente, fecha)
            listaNuevaDondeGuardamos.append(venta)
        # print(listaNuevaDondeGuardamos)
        listaoli = self.ventaInstancia.convertirVentaADiccionario(listaNuevaDondeGuardamos)
        self.ventaInstancia.enviarDiccionarioYAlmacenamientoJson("ventas.json", listaoli)
        return listaoli 
            
    def tablaClientes(self):
        try:
            listaClientesT = self.listaClientes
            # print("-------------------Clientes existentes-------------------------")
            # print("----Nombre-----------------RFC----------------------Telefono---")
            # for cliente in listaClientesT:
            #     nombre = cliente.nombre
            #     rfc = cliente.rfc
            #     telefono = cliente.telefono
            #     print("---" + nombre + "-----------" + rfc + "-----------" + telefono + "----")
            nombre_max_len = max([len(cn.nombre) for cn in listaClientesT])
            rfc_max_len = max([len(cr.rfc) for cr in listaClientesT])
            telefono_max_len = max([len(ct.telefono) for ct in listaClientesT])
            
            print('-' * (nombre_max_len + rfc_max_len + telefono_max_len + 10))
            print(colored('| {0:^{1}} | {2:^{3}} | {4:^{5}} |'.format('Nombre', nombre_max_len, 'RFC', rfc_max_len, 'Telefono', telefono_max_len), "red"))
            print('-' * (nombre_max_len + rfc_max_len + telefono_max_len + 10))
            
            for cliente in listaClientesT:
                print('| {0:^{1}} | {2:^{3}} | {4:^{5}} |'.format(cliente.nombre, nombre_max_len, cliente.rfc, rfc_max_len, cliente.telefono, telefono_max_len))
                print('-' * (nombre_max_len + rfc_max_len + telefono_max_len + 10))
        except:
            print("No existen ventas en el sistema actual")

        
    def tablaVentas(self):
        try:
            ventaDiccionario = self.ventaInstancia.diccionario()
        
            # prueba = [venta['cliente']['nombre'] for venta in ventaDiccionario] este es para ver el nombre
            nombre_max_len = max([len(ventaN['cliente']['nombre']) for ventaN in ventaDiccionario])
            rfc_max_len = max([len(ventaR['cliente']['rfc']) for ventaR in ventaDiccionario])
            telefono_max_len = max([len(ventaT['cliente']['telefono']) for ventaT in ventaDiccionario])
            
            
            nombrePr_max_len = 0
            for ventaP in ventaDiccionario:
                for producto in ventaP['productos']:
                    nombre_len = len(producto['_nombre'])
                    if nombre_len > nombrePr_max_len:
                        nombrePr_max_len = nombre_len

            # print(nombrePr_max_len)
            
            codigoPr_max_len = 0
            for ventaC in ventaDiccionario:
                for productoC in ventaC['productos']:
                    codigo_len = len(productoC['_codigo'])
                    if codigo_len > codigoPr_max_len:
                        codigoPr_max_len = codigo_len
                        
            descripcionPr_max_len = 0
            for ventaD in ventaDiccionario:
                for productoD in ventaD['productos']:
                    descripcion_len = len(productoD['_descripcion'])
                    if descripcion_len > descripcionPr_max_len:
                        descripcionPr_max_len = descripcion_len
            
            precioPr_max_len = 0
            for ventaPr in ventaDiccionario:
                for productoPr in ventaPr['productos']:
                    precio_len = len(str(productoPr['_precio']))
                    if precio_len > precioPr_max_len:
                        precioPr_max_len = precio_len
            
            
            
            for EachVenta in ventaDiccionario:
                
                print('-' * (nombre_max_len + rfc_max_len + telefono_max_len + 10))
                print(colored('| {0:^{1}} | {2:^{3}} | {4:^{5}} |'.format('Nombre', nombre_max_len, 'RFC', rfc_max_len, 'Telefono', telefono_max_len), "yellow"))
                print('-' * (nombre_max_len + rfc_max_len + telefono_max_len + 10))
                
                print('| {0:^{1}} | {2:^{3}} | {4:^{5}} |'.format(EachVenta['cliente']['nombre'], nombre_max_len, EachVenta['cliente']['rfc'], rfc_max_len, EachVenta['cliente']['telefono'], telefono_max_len))
                print('-' * (nombre_max_len + rfc_max_len + telefono_max_len + 10))
            
            
                print('-' * (nombrePr_max_len + codigoPr_max_len + descripcionPr_max_len + precioPr_max_len + 16))
                print(colored('| {0:^{1}} | {2:^{3}} | {4:^{5}} | {6:^{7}} |'.format('Nombre', nombrePr_max_len, 'Codigo', codigoPr_max_len, 'Descripcion', descripcionPr_max_len, 'Precio', precioPr_max_len), 'green'))
                print('-' * (nombrePr_max_len + codigoPr_max_len + descripcionPr_max_len + precioPr_max_len + 16))
                
                total_venta = 0
                for ProductList in EachVenta['productos']:
                    print('| {0:^{1}} | {2:^{3}} | {4:^{5}} | {6:^{7}} |'.format(ProductList['_nombre'], nombrePr_max_len, ProductList['_codigo'], codigoPr_max_len, ProductList['_descripcion'], descripcionPr_max_len, ProductList['_precio'], precioPr_max_len))
                    print('-' * (nombrePr_max_len + codigoPr_max_len + descripcionPr_max_len + precioPr_max_len + 16))
                    precioCP = ProductList['_precio']
                    total_venta += precioCP
                
                    
                print(colored('| {0:{1}} | {2:{3}} |'.format( 'Precio Final', nombrePr_max_len, total_venta, codigoPr_max_len), 'red'))
                print()
        except:
            print(colored('No hay ventas registradas', 'red'))

          
    #------------------------------------------------------------------------------#

    #---------------------------------MONGO----------------------------------------#
    def mongoMenu(self):
        opcion = 0
        while opcion!= 9:
            print("---------------------------------------------------------------")
            print("----------------------- MONGO INTERFAZ ------------------------")
            print(colored("[1] Conectar a Mongo\n[2] Guardar clientes\n[3] Cerrar conexion\n[9] Salida", "blue"))
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
        #poner en el metodo connect la url de la conexion con mongodb
            conn = self.mongoInstancia.connect("conexion_db")
            if conn == False:
                print("Error al conectar con la base de datos")
            else:
                print("Conectado con la base de datos")
                # self.subirMongo()
        
    def mirarMongo(self):
        self.mongoInstancia.hacerFind()
        
    def guardarDatosEnMongo(self):
        jsontemporal = self.mongoInstancia.cargarListaJson("ventasTemporales.json")
        if jsontemporal == False:
            print("No existe ningun producto temporal actualmente")
            se_guardo = self.mongoInstancia.guardarEnMongoParaTodos('Tienda', 'Ventas', self.devolverDiccionarioVentas(), 'ventas.json', 'ventasTemporales.json')
            if se_guardo == False:
                print("No existe conexion con la base de datos, se han guardado los datos de manera temporal")
                # De aqui en adelante si exite la conexion, al menos en este if, es cuando no existe ar temporal, pero si conexion            
            else:
                print("Se han guardado los datos de manera adecuada en ambos sistemas")
        else:
            nuevojsonjeje = self.cargarListaJsonTemporal(jsontemporal)
            # print(jsonTemporalConvertido)
            # el jsontemporal tiene que pasar por el convertidor, porque si no me esta jodiendo la json
            se_guardo = self.mongoInstancia.guardarEnMongoParaTodos('Tienda', 'Ventas', nuevojsonjeje, 'ventas.json', 'ventasTemporales.json')
            if se_guardo == False:
                print("Pu;etas")
            else:
                print("Se han guardado los datos de manera adecuada en ambos sistemas")
                self.mongoInstancia.borrarJson("ventasTemporales.json")
    
    #------------------------------------------------------------------------------#
