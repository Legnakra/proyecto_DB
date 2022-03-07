from Funciones import *
import time

db = ConectarBD("localhost", "mj","admin","Compositores")
opcion=Menu()
while opcion!=0:

#Opción 1 del menú:
    if opcion==1:
        ListarCompositores(db)
        print ("- - - - - - - - - - - - - - - - - - -")
        time.sleep(2)
    
#Opción 2 del menú:
    elif opcion==2:
        print ("Los tipos de composiciones que hay son: Sonata, Oratorio, Sinfonia,")
        busctipo=input("Introduzca el tipo de composición que desea buscar: ")
        print("Composiciones ", busctipo)
        BuscarTipo(db,busctipo)
        time.sleep(2)

#Opción 3 del menú:
    elif opcion ==3:
        nombreautor= input("Escriba el nombre del compositor que desea buscar: ")
        print("Nombre: ",nombreautor)
        ListarApellido(db,nombreautor)
        time.sleep(2)


#Opción 4 del menú:
    elif opcion ==4:
        composicion = {}
        composicion["nombrecomposicion"] = input("Obra: ")
        composicion["movimientos"] = int(input("Nº movimientos: "))
        composicion["tipo"] = input("Tipo: ")
        composicion["grupo"] = input("Agrupación: ")
        composicion["nombreautor"] = input("Autor: ")
        InsertarObra(db,composicion)
        agregar_autor = ("El autor no se encuentra en la base de datos. ¿Desea incluirlo en la misma?(S/N)")
        if agregar_autor =="S":
            print("Nuevo compositor.")
            autor = {}
            autor["nombre"] = input("Compositor: ")
            autor["annonacimiento"] = int(input("Fecha de nacimiento (YYYY-MM-DD): "))
            autor["epoca"] = input("Época: ")
            InsertarCompositor(db,autor)
            time.sleep(2)
        


#Opción 5 del menú:
    elif opcion ==5:
        movimientos = int(input("¿Cuantos movimientos tienen las obras que desea eliminar?: "))
        BorrarComposicion(db,movimientos)
        time.sleep(2)


#Opción 6 del menú:
    elif opcion ==6:
        print (MostrarEpoca(db))
        epoca = input("¿Cuál es la época que desea actualizar?: ")
        ActualizarEpoca(db,epoca)
        time.sleep(2)



#Opción 0 del menú:
    elif opcion ==0:
        Desconexión(db)
    else:
        print("\n")
    opcion=Menu()

print("¡Hasta pronto!")