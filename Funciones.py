import sys
import MySQLdb

#FUNCIONES DE CONEXIÓN Y DESCONEXIÓN
#Función Conexión:
def ConectarBD(host, usuario, password, nombrebd):
    try:
        db = MySQLdb.connect(host, usuario, password, nombrebd)
        return db
    except MySQLdb.Error as e:
        print ("No se ha podido establecer la conexión.",e)
        sys.exit(1)


#Función Desconexión:
def Desconexión (db):
    db.close()



#Función Menú
def Menu():
    menu= '''
    1. Listar compositores, su época y número de compositores.
    2. Mostrar los compositores de un tipo de composición introducida por teclado.
    3. Introduce el apellido y muestra sus obras.
    4. Insertar nueva obra, en caso de no existir el compositor, añadir compositor.
    5. Elimina las obras de los movimientos insertados.
    6. Actualizar la époda de un compositor.
    0. Salir.
    '''
    print (menu)
    while True:
        try:
            opcion= int(input("Introduzca la opción deseada: "))
            return opcion
        except:
            print("La opción introducida es incorrecta.")



#FUNCIONES OPCIONES DE MENÚ
#Función Ejercicio 1: Listar los compositores, su época y el número de compositores.
def ListarCompositores(db):
    sql= "SELECT nombreautor, count(*) as 'NumComposiciones' FROM composiciones, compositores WHERE nombre = nombreautor GROUP BY nombre"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        lista = cursor.fetchall()
        for comp in lista:
            print(comp["nombreautor"],"---",comp["NumComposiciones"])
    except:
        print("Consulta: Error.")



#Función Ejercicio2: Mostrar los compositores de un tipo de composición introducida por teclado.
def BuscarTipo(db,tipo):
    sql = "SELECT nombreautor FROM composiciones WHERE tipo='%s'" % tipo
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print("Ninguna compositor con ese tipo.")
        else:
            tip = cursor.fetchall()
            for comp in tip:
                print(comp["nombreautor"])
    except:
        print("Consulta: Error.")



#Función 3
def ListarApellido(db,nombreautor):
    sql="SELECT * FROM composiciones WHERE nombreautor='%s'" % nombreautor
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print("No existe el compositor en la base de datos.")
        else:
            listas = cursor.fetchall()
            for lista in listas:
                print(lista["nombrecomposicion"])
    except:
        print("Consulta: Error.")



#Función 4:
##a
def InsertarObra(db,composiciones):
    sql= "INSERT INTO composiciones VALUES ('%s','%d','%s','%s','%s')" % (composiciones["nombrecomposicion"],composiciones["movimientos"],composiciones["tipo"],composiciones["grupo"],composiciones["nombreautor"])
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Consulta: Error.")
        db.rollback()

##b
def InsertarCompositor(db,compositores):
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    sql= "INSERT INTO compositores VALUES ('%s','%d','%s')" % (compositores["nombre"],compositores["anonacimiento"],compositores["tipo"],compositores["epoca"])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Consulta: Error.")
        db.rollback()

##mostrar tablas:
def MostrarCompositores(db):
    sql = "SELECT * FROM compositores"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        lista = cursor.fetchall()
        for comp in lista:
            print(comp)
    except:
        print("Consulta: Error.")



#Función 5
def BorrarComposicion(db,movimientos):
    sql = "DELETE FROM composiciones WHERE movimientos = %d" % movimientos
    print(sql)
    cursor = db.cursor()
    confirmacion = input("¿Desea eliminar dichas obras? (S/N): ")
    if confirmacion== "S":
        try:
            cursor.execute(sql)
            db.commit()
            print("Composiciones eliminadas.")
            if cursor.rowcount ==0:
                print("No hay composiciones con ese número de movimientos.")
        except:
            print("Eror: No se han podido eliminar las composiciones.")
            db.rollback()



#Función 6
##a
def ActualizarEpoca(db,epoca):
    sql= "UPDATE compositores SET epoca = '%s'"(epoca)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.coomit()
    except:
        print("Consulta: Error.")

##b
def MostrarEpoca(db):
    sql ="SELECT epoca FROM compositores"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        tabla = cursor.fetchall()
        print(tabla)
    except:
        print("Consulta: Error.")