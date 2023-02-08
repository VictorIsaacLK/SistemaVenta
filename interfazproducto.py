import producto, time, mongo
from termcolor import colored

class InterfazProducto():
    def __init__(self, productoInstancia = producto.Producto(), mongoInstancia = mongo.MongoDB()):
        self.productoInstancia = productoInstancia
        self.productoInstancia.cargarListaJson()
        self.mongoInstancia = mongoInstancia
        
        
        
    #--------------------------------PRODUCTO--------------------------------------#

    def IngresarProducto(self):
        productoObjeto = self.crearProducto()
        self.productoInstancia.agregarProductoLista(productoObjeto)
        self.productoInstancia.conversionAJson()


    def crearProducto(self):
        nombre = str(input("Ingresar el nombre del producto: "))
        codigo = str(input("Ingresar el codigo del producto: "))
        descripcion = str(input("Ingresar la descripcion del producto: "))
        try:
            print("El precio del Producto debe ser solo numeros")
            precio = float(input("Ingresar el precio del producto: "))
        except ValueError:
            print("Solo se aceptan numeros.")
            precio = float(input("Ingresar el precio del producto: "))
        prod = producto.Producto(nombre, codigo, descripcion, precio)
        print("\nSe ha creado un Producto con el nombre de:", nombre)
        return prod
        
    def mostrarListadoDeProductos(self):
        diccionarioProductos = self.devolverDiccionarioProductos()
        
        try:
            nombre_max_len = max([len(pn['_nombre']) for pn in diccionarioProductos])
            codigo_max_len = max([len(pc['_codigo']) for pc in diccionarioProductos])
            descripcion_max_len = max([len(pd['_descripcion']) for pd in diccionarioProductos])
            precio_max_len = max([len(str(pp['_precio'])) for pp in diccionarioProductos])
            
            print('-' * (nombre_max_len + codigo_max_len + descripcion_max_len + precio_max_len + 16))
            print(colored('| {0:^{1}} | {2:^{3}} | {4:^{5}} | {6:^{7}} |'.format('Nombre', nombre_max_len, 'Codigo', codigo_max_len, 'Descripcion', descripcion_max_len, 'Precio', precio_max_len), 'green'))
            print('-' * (nombre_max_len + codigo_max_len + descripcion_max_len + precio_max_len + 16))
            
            for producto in diccionarioProductos:
                print('| {0:^{1}} | {2:^{3}} | {4:^{5}} | {6:^{7}} |'.format(producto['_nombre'], nombre_max_len, producto['_codigo'], codigo_max_len, producto['_descripcion'], descripcion_max_len, producto['_precio'], precio_max_len))
                print('-' * (nombre_max_len + codigo_max_len + descripcion_max_len + precio_max_len + 16))
        except:
            print("No hay productos disponibles")
            
        

    def cambiarPropiedadProducto(self):
        opcion = 0
        while opcion != 9:
            print("---------------------------------------------------------------")
            print("Seleccione el campo que va a cambiar")
            print("[1] Nombre - Codigo - Descripcion\n[2] Precio\n[9] Salir")
            opcion = int(input("Opcion: "))
            print("---------------------------------------------------------------")
            if opcion == 1:
                antiguoValor = str(input("Valor a cambiar: "))
                nuevoValor = str(input("Nuevo valor: "))
                self.productoInstancia.cambiarPropiedad(antiguoValor, nuevoValor)
                self.productoInstancia.conversionAJson()
            elif opcion == 2:
                antiguoValor = float(input("Valor a cambiar: "))
                nuevoValor = float(input("Nuevo valor: "))
                self.productoInstancia.cambiarPropiedad(antiguoValor, nuevoValor)
                self.productoInstancia.conversionAJson()
                
    def eliminarProducto(self):
        print("---------------------------------------------------------------")
        nombre = str(input("Ingrese el nombre del producto a eliminar: "))
        print("---------------------------------------------------------------")
        self.productoInstancia.eliminarProducto(nombre)
        self.productoInstancia.conversionAJson()
        
    def devolverListaProductos(self):
        return self.productoInstancia.devolverLista()
    
    def devolverDiccionarioProductos(self):
        return self.productoInstancia.diccionario()        

#------------------------------------------------------------------------------#

#-----------------------------------MONGODB------------------------------------#

    def conexion(self):
        #en el metodo connect poner la url de tu conexion
            conn = self.mongoInstancia.connect("conexion_base_datos")
            if conn == False:
                print("Error al conectar con la base de datos")
            else:
                print("Conectado con la base de datos")
                # self.subirMongo()
    
    def subirMongo(self):  
        db_name = input("Ingrese el nombre de la base de datos: ")
        coll_name = input("Ingrese el nombre de la colección: ")
        paquete = self.productoInstancia.traerJson()
        self.mongoInstancia.update_all_documents(db_name, coll_name, paquete)
        
    def mirarMongo(self):
        self.mongoInstancia.hacerFind()
        
    def guardarDatosEnMongo(self):
        jsontemporal = self.mongoInstancia.cargarListaJson("productosTemporales.json")
        if jsontemporal == False:
            print("No existe ningun producto temporal actualmente")
            se_guardo = self.mongoInstancia.guardarEnMongo('Tienda', 'Productos', self.devolverDiccionarioProductos())
            if se_guardo == False:
                print("No existe conexion con la base de datos, se han guardado los datos de manera temporal")
                # De aqui en adelante si exite la conexion, al menos en este if, es cuando no existe ar temporal, pero si conexion            
            else:
                print("Se han guardado los datos de manera adecuada en ambos sistemas")
        else:
            nuevojsonjeje = self.productoInstancia.cargarListaJsonTemporal(jsontemporal)
            # print(jsonTemporalConvertido)
            # el jsontemporal tiene que pasar por el convertidor, porque si no me esta jodiendo la json
            se_guardo = self.mongoInstancia.guardarEnMongo('Tienda', 'Productos', nuevojsonjeje)
            if se_guardo == False:
                print("Pu;etas")
            else:
                print("Se han guardado los datos de manera adecuada en ambos sistemas")
                self.mongoInstancia.borrarJson("productosTemporales.json")
        
    def MongoInterfaz(self):
        opcion = 0
        while opcion!= 9:
            print("---------------------------------------------------------------")
            print("----------------------- MONGO INTERFAZ ------------------------")
            print(colored("[1] Conectar a Mongo\n[2] Guardar lista de productos\n[3] Cerrar conexion\n[9] Salida", "green"))
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
            elif opcion == 3:
                self.mongoInstancia.cerrarConexion()

#------------------------------------------------------------------------------#

#---------------------------------MENU-----------------------------------------#

    def detente(self, segundos):
        time.sleep(segundos)

    def menuProductos(self):
        opcion = 0
        while opcion!= 9:
            print("---------------------------------------------------------------")
            print("[1] Ingresar Producto\n[2] Ver Lista de Productos\n[3] Cambiar valor de un Producto de la lista\n[4] Eliminar Producto\n[5] MongoDB\n[9] Salida")
            print("---------------------------------------------------------------")
            try:
                opcion = int(input("Opcion: "))
            except ValueError:
                print("Opcion no valida")
            print("---------------------------------------------------------------")
            if opcion == 1:
                self.IngresarProducto()
                opcion = 0
            elif opcion == 2:
                self.mostrarListadoDeProductos()
                self.detente(1)
                opcion = 0
            elif opcion == 3:
                self.cambiarPropiedadProducto()
                opcion = 0
            elif opcion == 4:
                self.eliminarProducto()
                opcion = 0
            elif opcion == 5:
                self.MongoInterfaz()
                opcion = 0

