from functools import reduce

setdatos = [] #Se crea una lista para caergar el csv

#abrimos el archivo y lo cargamos en la lista
with open ("gsales50.csv", "r")  as f:
    for linea in f:
        setdatos.append(linea.strip().split(","))

#Funciones
def buscar():
    a = True
    while a:
        x = input("Ingrese que desea buscar: ").lower()
        cont = 0
        print(" | ".join(setdatos[0]))
        for i in range(len(setdatos)):
            for y in setdatos[i]:
                if x in y.lower():
                    if x == y.lower():
                        cont += 1
                        print(" | ".join(setdatos[i]))
                        break
        if cont == 0:
            print(f" No se encontro {x} en ningun registro\n")
            print(" Si desea seguir buscando? (si/no)")
            print(" Ingresar algo distinto a estos dos, se volvera al menu principal")
            sino = input().lower()
            if sino == "si":
                a = True
            elif sino == "no":
                a = False
            else:
                print(" Opcion invalida, se cerrara la busqueda")
                a = False
        else:
            print(f" Se encontro {x} en {cont} registros\n")
            print(" Si desea seguir buscando? (si/no)")
            print(" Ingresar algo distinto a estos dos, se volvera al menu principal")
            sino = input().lower()
            if sino == "si":
                a = True
            elif sino == "no":
                a = False
            else:
                print(" Opcion invalida, volviendo al menu principal...")
                a = False


#Función filtrar 
def filtrar_por_condicion_numerica(datos, indice_columna, valor_limite):
    """
    Filtra los registros de la lista donde el valor de una columna numérica 
    sea estrictamente mayor al valor límite ingresado por el usuario.
    
    """
    #crear una lista vacía para ir guardando solo las filas que cumplan la condición
    registros_filtrados = []
    
    #recorrer la lista principal registro por registro fila por fila mediante un bucle
    for fila in datos:
        
        #verificar que la fila actual tenga la cantidad de columnas suficiente para evitar un error de tipo "IndexError" si hay líneas corruptas
        if len(fila) > indice_columna:
            
            #usar un bloque try-except para manejar posibles errores de conversión
            try:
                #extraer el valor del texto de la columna requerida, eliminar espacios en blanco 
                #en los extremos con .strip() y convertir el valor de texto (str) a decimal (float)
                valor_actual = float(fila[indice_columna].strip())
                
                # evaluar si el número extraído es mayor al umbral definido por el usuario
                if valor_actual > valor_limite:
                    #si se cumple la condición, agregar la fila completa a la lista de resultados
                    registros_filtrados.append(fila)
                    
            except ValueError:
                #si la casilla está vacía o contiene texto no numérico,
                #el programa ignora la fila y continúa con la siguiente sin detenerse
                continue
                
    #retornar la lista final con todos los registros filtrados
    return registros_filtrados

def menu_filtrar_por_condicion(datos):
    '''
    Función que interactúa con el usuario desde la consola, 
    muestra las columnas disponibles, valida los límites y ejecuta el filtro.
    '''
    print("\n FILTRAR POR CONDICIÓN NUMÉRICA ")
    print("Seleccione la columna por la cual desea filtrar:")
    print("1. Ventas Totales en millones (Total_Shipped)")
    print("2. Calificación de la Crítica (Critic_Score)")
    print("3. Calificación de Usuarios (User_Score)")
    print("4. Año de Lanzamiento (Year)")
    
    opcion = input("Ingrese el número de la opción (1-4): ").strip()
    
    # mapeo de opción elegida a su respectivo índice en el CSV y su nombre
    indices_columnas = {
        "1": (7, "Ventas Totales (millones)", 14.64, 82.90),
        "2": (5, "Calificación de Críticos", 5.9, 10.0),
        "3": (6, "Calificación de Usuarios", 3.3, 10.0),
        "4": (8, "Año de Lanzamiento", 1985, 2019)
    }
    
    # validar que la opción elegida sea válida
    if opcion not in indices_columnas:
        print("Opción inválida. Regresando al menú principal...")
        return

    idx_col, nombre_col, min_val, max_val = indices_columnas[opcion]
    
    # informar al usuario el rango válido de datos que existen en el CSV
    print(f"\nHa elegido: {nombre_col}")
    print(f"Los valores en el dataset van desde {min_val} hasta {max_val}.")
    
    # capturar el valor límite validando que sea realmente un número
    try:
        limite = float(input(f"Ingrese el valor límite (debe ingresar un número): "))
    except ValueError:
        print("\nError: Debe ingresar un valor numérico válido (ejemplo: 20.0 o 8.5).")
        return
        
    # llamada a la función de filtrado
    resultados = filtrar_por_condicion_numerica(datos, idx_col, limite)
    
    # mostrar los resultados sin errores
    print(f"\n=== Se encontraron {len(resultados)} registro(s) con {nombre_col} > {limite} ===")
    
    if len(resultados) == 0:
        print("No hay registros en el dataset que superen ese valor.")
    else:
        for reg in resultados:
            # imprimir campos clave: nombre, plataforma y el Valor filtrado
            print(f"- {reg[1]} ({reg[2]}) -> {nombre_col}: {reg[idx_col]}")



def topgames(top):
    """
    Esta funcion le piede al usuario un numero, 
    despues imprime una tabla con la lista del top videojuegos que quizo consultar
    El data set ya esta ordenado de esa forma, solo es necesario imprimir las columnas deseadas
    """
    print(f"El top {top} de juegos mas vendidos son:")
    print("# | Nombre del Juego                              |         Desarrolador         | Plataforma |  Año   |")
    for i in setdatos[1:top+1]:
        print(f"{i[0]:^2}| {i[1]:<45} | {i[4]:^28} | {i[2]:^10} | {i[8]:^6} |")



def estadist():
    a = 1
    calculo = []
    while a != 0:
        option = input("\n [---MENÚ ESTADITICAS---]\n"
                        " Por favor, elija la categoría para la cuál desea conocer información estadística:\n" 
                        " 1. Puntuación de los Críticos\n"
                        " 2. Puntuación de los usuarios\n"
                        " 3. Total Vendidos\n"
                        " 4. Año de publicación\n" 
                        " 5. Volver al Menú Principal\n"
                        " Opcion: "
                        )
        if option == "1":
            for j in range(1,len(setdatos[1:])+1):
                calculo.append(setdatos[j][5])
            calcfloat = [float(x) for x in calculo if x.strip() != '']
            promc = (reduce(lambda x,y:x+y,calcfloat)/50)
            maxc = max(calcfloat)
            minc = min(calcfloat)
            print("\n  [---RESULTADO CRITICOS---]\n"
                  "  Para las puntuaciones de los críticos, tenemos:\n"
                  f"  El promedio: {promc:.1f}\n"
                  f"  El número máximo: {maxc}\n"
                  f"  El número mínimo: {minc}."
                  )
            calculo = []
        elif option == "2":
            for j in range(1,len(setdatos[1:])+1):
                calculo.append(setdatos[j][6])
            calcfloat = [float(x) for x in calculo if x.strip() != '']
            promc = (reduce(lambda x,y:x+y,calcfloat)/50)
            maxc = max(calcfloat)
            minc = min(calcfloat)
            print("\n  [---RESULTADO USUARIOS---]\n"
                   "  Para las puntuaciones de los usuarios, tenemos:\n"
                   f"  El promedio: {promc:.1f}\n"
                   f"  El número máximo: {maxc}\n"
                   f"  El número mínimo: {minc}."
                   )
            calculo = []
        elif option == "3":
            for j in range(1,len(setdatos[1:])+1):
                calculo.append(setdatos[j][7])
            calcfloat = [float(x) for x in calculo if x.strip() != '']
            promc = (reduce(lambda x,y:x+y,calcfloat)/50)
            maxc = max(calcfloat)
            minc = min(calcfloat)
            print(f"\n  [---RESULTADO VENTAS---]\n"
                    "  Para las ventas totales, tenemos:\n"
                    f"  El promedio: {promc:.1f}\n"
                    f"  El número máximo: {maxc}\n"
                    f"  El número mínimo: {minc}."
                    )
            calculo = []
        elif option == "4":
            for j in range(1,len(setdatos[1:])+1):
                calculo.append(setdatos[j][8])
            calcfloat = [float(x) for x in calculo if x.strip() != '']
            promc = (reduce(lambda x,y:x+y,calcfloat)/50)
            maxc = max(calcfloat)
            minc = min(calcfloat)
            print("\n  [---RESULTADO AÑOS---]\n"
                "  Para los años de publicación, tenemos:\n"
                f"  El promedio: {promc:.1f}\n"
                f"  El número máximo: {maxc:.0f}\n"
                f"  El número mínimo: {minc:.0f}"
                )
            calculo = []
        elif option == "5":
            print("  Regresando al Menú Principal...")
            break
        else:
            print("Opción ingresada no es válida, por favor vuelve a intentarlo.")

#menu principal

print("\nProyecto de Programación GSales\n" 
        "Primera Entrega\n"
        "\n Integrantes:"
        "\n   Edwin Andres Niño Garcia"
        "\n   Henry Andres Fernandez Lozano"
        "\n   Emmanuel Diaz Montes"
        "\n   Camilo Alejandro Arevalo Inampues"
        "\n DataSet Escogido: Video Game Sales Data\n"
        " link: https://www.kaggle.com/datasets/holmjason2/videogamedata"
        )
#Menu principal
"""
El menu donde se ejecutan las funciones
las funciones de Buscar() y estadist() no tienen parametros ya que esas llevan a sus propios submenus donde se piden los valores a consultar
la funcion topgames() pide el parametro ya que es una funcion sencilla
La funcion menu_filtrar_por_condicion() pide como parametro la lista del dataset
"""
menu = str()
while menu != 0:
    menu = input("\n[-----MENU PRINCIPAL-----]\n"
                "1. Busqueda Por Terminos\n"
                "2. Filtrar Por condicion\n"
                "3. Consular Top Juegos Vendidos\n"
                "4. Estadisticas\n"
                "5. Salir\n"
                "Ingrese Una Opcion: ")
    
    if menu == "1":
        buscar()
    elif menu == "2":
        menu_filtrar_por_condicion(setdatos)
    elif menu == "3":
        topconsultado = int(input("Ingrese el top de juegos que desea Consultar: "))
        topgames(topconsultado)
    elif menu == "4":
        estadist()
    elif menu == "5":
        print("Cerrando Programa... Gracias por Consultar!")
        break
    else:
        print("Opcion Invalida, Intentelo denuevo. ")
