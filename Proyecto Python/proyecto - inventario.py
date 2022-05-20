#Variables globales: Inventario (listas)
producto = ["martillo", "pinza", "pincel"]
precio = [900.0, 720.5, 300.10]


"""---------------------------FUNCIÓN PRINCIPAL---------------------------""" 

def sistema():
    while (True):
        mostar_menu()
                                                                                 #Mostrar Menú
        opcion = int(input("Ingrese la opción que desea realizar: "))            #¿Qué desea hacer el usuario?
        if opcion ==1:                                                           #Agregar producto si la opción es 1)
            agregar_producto()
        if opcion ==2: 
            eliminar_producto()                                                  #Eliminar producto si la opción es 2)
        if opcion ==3: 
            vender_producto()                                                    #Vender productos si la opción es 3)
        if opcion ==4:
            reporte_ventas()                                                     #Reporte de ventas si la opción es 4)
        if opcion ==0:
            print("El programa se ha cerrado")                                   #Cerrar el programa si la opción es "0"
            break
        else: 
            print("Seleccione una opción correcta")                              #Ingresar una opción correcta (entre 0 y 4)



""" --------------------------- FUNCIONES ---------------------------"""



""" --------------------- GESTIÓN DE INVENTARIO ---------------------"""


"""-------------------------------MENÚ-------------------------------"""

#Función "Menú": el objetivo es mostrar las opciones disponibles para el usuario

def mostar_menu():
    print("""
            ¡Bienvenido al sistema de gestión ASC!

            Usted puede: 

            1. Agregar un producto en el inventario
            2. Eliminar un nuevo producto en el inventario
            3. Vender productos
            4. Reporte de ventas
            0. Cerrar el programa
            
            """)



"""---------------------------AGREGAR PRODUCTO---------------------------"""

#Función "Agregar P.": el objetivo principal es que el usuario pueda agregar un producto al inventario. 

def agregar_p():

        producto_agregar = input("Ingrese el nombre del producto que desea agregar: ")          #Ingreso del producto a agregar por el usuario.

        for p in producto:                                                                      #Ciclo en el listado de productos

            if p == producto_agregar:                                                           #Si el producto ingresado está en el listado NO puede agregarse
                print(f"{producto_agregar} ya se encuentra en el inventario")
                break
        else:                                                                                   #Si el producto ingresado NO está en el listado:PUEDE agregarse 
            usuario_precio = int(input("ingrese el precio: $ ") )                               #Solicitud de ingreso de precio
            producto.append(producto_agregar)                                                   #Se agrega el producto ingresado
            precio.append(usuario_precio)                                                       #Se agrega el precio ingresado
                
            print(f"Se agregó: {producto_agregar} - ${usuario_precio}")                         #Qué se agregó al inventario


#Función "Agregar Producto.": el objetivo principal es que el usuario pueda agregar la cantidad de productos que desee al inventario. 

def agregar_producto():
    agregar_p()
    while (True): 
        seguir_agregando = int(input("¿Desea seguir añadiendo más productos al carro? Digite la opción:\r\n 1) Si \r\n 2) No \r\n "))
        if seguir_agregando == 1:
            agregar_p()
            continue

        else:
            print(f" Inventario actual: \r\n Productos: {producto}, \r\n Precios: {precio}")    #Inventario actual                              

        break



"""---------------------------ELIMINAR PRODUCTO---------------------------"""

#Función "Eliminar P": el objetivo principal es que el usuario pueda eliminar tanto un producto como su precio de las listas (inventario)

def eliminar_p():
    producto_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")             #Ingreso del producto a eliminar por el usuario. 
        
    for p in producto:                                                                           #Ciclo en el listado de productos. 
                                            
        if p == producto_eliminar:                                                               #Si el producto ingresado está en el listado:
            pos_producto = producto.index(p)                                                     #Buscar la posición del producto ingresado.
            producto.pop(pos_producto)                                                           #Se elimina el producto ingresado (en base a la posición)
            precio.pop(pos_producto)                                                             #Se elimina el producto ingresado (en base a la posición)
                
            print(f"{producto_eliminar} se eliminó exitosamente")
            break
        
    else:
        print(f"{producto_eliminar} no se encuentra en el inventario.")                         #Si el producto ingresado no está en el inventario: 
        

#Función "Eliminar Producto": el objetivo principal es que el usuario pueda eliminar los productos que desee y su precio de las listas (inventario)

def eliminar_producto():
    eliminar_p()
    while (True):
        seguir_eliminando = int(input("¿Desea seguir eliminando más productos del inventario? Digite la opción:\r\n 1) Si \r\n 2) No \r\n ")) 
        if seguir_eliminando == 1:
            eliminar_p()
            continue
        
        else:
            print(f" Inventario actual:\r\n Productos: {producto}, \r\n Precios: {precio}") 
            break  




"""--------------------------------VENTAS-----------------------------------"""

#Variables globales para añadir productos al carrito de compras (listas)
carrito_productos = []
carrito_precios =[]


"""-----------------AGREGAR PRODUCTO AL CARRITO DE COMPRAS------------------"""
#Función "Agregar un Producto al Carrito": el objetivo principal es que se agregue un producto (existente en el inventario) al carrito con su respectivo precio. 

def agregar_producto_carrito():
    producto_comprar = input("Ingrese el nombre del producto que desea comprar: ")

    for p in producto:
        if p == producto_comprar:                                                   #Si el producto ingresado está en el listado:
            pos_producto = producto.index(producto_comprar)                         #Buscar la posición del producto ingresado. 
            carrito_productos.append(producto_comprar)                              #Se añade al carrito el producto ingresado
            carrito_precios.append(precio[pos_producto])                            #Se añade a carrito_precios el precio del producto (en base a la posición)
            print(f"{producto_comprar} se añadió exitosamente al carro")
            break
    else:                                                                           #Si el producto ingresado no está en el inventario
        print(f"{producto_comprar} no se encuentra en el inventario.") 
        


"""---------------------------VENDER PRODUCTOS------------------------------""" 

#Función "Vender Producto": el objetivo principal es que el usuario pueda vender al cliente los productos que desee. 

def vender_producto(): 
    agregar_producto_carrito()
    while(True): 
        seguir_comp = int(input("¿Desea seguir añadiendo más productos al carro? Digite la opción:\r\n 1) Si \r\n 2) No \r\n "))
        if seguir_comp == 1:
            agregar_producto_carrito()
            continue

        else:
            print(f" Producto(s) añadido(s): {carrito_productos}, \r\n Precios: {carrito_precios}")   #Resultado
            suma_precios = sum(carrito_precios)                                                       #Suma de los precios del producto del carrito (Total)
            print(f"El total a pagar es: ${suma_precios}")                                            #Cuánto es el TOTAL que se debe pagar. 

        break
     

"""--------------BÚSQUEDA DE VENTAS POR RANGO DE PRECIOS---------------"""

#Función "Reporte Ventas", tiene por objeto determinar qué ventas se hicieron en base a un rango de precios establecido por el usuario.

def reporte_ventas():
    ventas_rango = []
    print("Veamos cuáles son las ventas que se realizaron en base a un rango de precios")
    precio_inicial = int(input("Ingrese el límite inferior: $ "))
    precio_final = int(input("Ingrese el límite superior: $ "))
    
    
    for v in carrito_precios:                                    #Se crea un ciclo que recorra todas las ventas. Esto permitirá saber cuáles son, por ejemplo, las ventas más altas.  

        if precio_inicial <= v <= precio_final:                  #Este ciclo se recorrerá solo entre los rangos definidos (LI-LS)
            ventas_rango.append(v)                               #Agrega a la lista vacía los resultados de ventas obtenidos para este rango.
            
            continue
            
        else:   
            continue
      

    print(f"Las ventas realizadas entre ${precio_inicial} y ${precio_final} fueron: {len(ventas_rango)} y vienen dadas por: \r\n{ventas_rango}")  
    

sistema()
