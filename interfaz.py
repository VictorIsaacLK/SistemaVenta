import interfazproducto, interfazcliente, interfazventa


def menuBienvenida():
    opcion = 0
    interfazproductoInstancia = interfazproducto.InterfazProducto()
    interfazclienteInstancia = interfazcliente.InterfazCliente()
    listaCliente = interfazclienteInstancia.devolverListaCliente()
    listaProducto = interfazproductoInstancia.devolverListaProductos()
    diccionarioCliente = interfazclienteInstancia.devolverDiccionarioCliente()
    diccionarioProducto = interfazproductoInstancia.devolverDiccionarioProductos()
    interfazventaInstancia = interfazventa.InterfazVenta(listaCliente, listaProducto, diccionarioCliente, diccionarioProducto)
    while opcion!= 9:
        print("---------------------------------------------------------------")
        print("Bienvenido al sistema de compras, decida la opcion que necesite")
        print("[1] Productos\n[2] Clientes\n[3] Ventas\n[9] Salida")
        print("---------------------------------------------------------------")
        try:
            opcion = int(input("Opcion: "))
        except ValueError:
            print("Opcion no valida")
        if opcion == 1:
            interfazproductoInstancia.menuProductos()
            opcion = 0
        if opcion == 2:
            interfazclienteInstancia.menuClientes()
            opcion = 0
        if opcion == 3:
            interfazventaInstancia.menuVentas()
            opcion = 0


menuBienvenida()