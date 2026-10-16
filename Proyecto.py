setdatos = []


with open ("gsales50.csv", "r")  as f:
    for linea in f:
        setdatos.append(linea.strip().split(","))

def buscar():
    print("Se le pedira que ingrese el nombre de lo que desee buscar, y se le dara en cuantos registros se encuentra")
    x = input("Ingrese que desea buscar: ").lower()
    cont = 0
    for i in range(len(setdatos)):
        for y in setdatos[i]:
            if x in y.lower():
                if x == y.lower():
                    cont += 1
                    break
    if cont == 0:
        print(f"No se encontro {x} en ningun registro")
    else:
        print(f"Se encontro {x} en {cont} registros")


#funcion para imprimir el top de juegos segun lo desea el usuario
def topgames():
    top = int(input("Ingrese el top de juegos que desea Consultar: "))
    print(f"El top {top} de juegos mas vendidos son:")
    print("# | Nombre del Juego                              |         Desarrolador         | Plataforma |  Año   |")
    for i in setdatos[1:top+1]:
        print(f"{i[0]:^2}| {i[1]:<45} | {i[4]:^28} | {i[2]:^10} | {i[8]:^6} |")

#Función estadística
def estadist():
    a = 1
    calculo = []
    while a != 0:
        option = input("[---MENÚ---]\nPor favor, elija la categoría para la cuál desea conocer información estadística:\n 1. Puntuación de los Críticos\n 2. Puntuación de los usuarios\n 3. Total Vendidos\n 4. Año de publicación\n 5. Salir\n")
        if option == "1":
            for j in range(1,len(setdatos[1:])+1):
                calculo.append(setdatos[j][5])
            calcfloat = [float(x) for x in calculo if x.strip() != '']
            promc = (reduce(lambda x,y:x+y,calcfloat)/50)
            maxc = max(calcfloat)
            minc = min(calcfloat)
            print(f"[---RESULTADO---]\nPara las puntuaciones de los críticos, tenemos:\nEl promedio: {promc:.1f}\nEl número máximo: {maxc}\nEl número mínimo: {minc}.")
            calculo = []
        elif option == "2":
            for j in range(1,len(setdatos[1:])+1):
                calculo.append(setdatos[j][6])
            calcfloat = [float(x) for x in calculo if x.strip() != '']
            promc = (reduce(lambda x,y:x+y,calcfloat)/50)
            maxc = max(calcfloat)
            minc = min(calcfloat)
            print(f"[---RESULTADO---]\nPara las puntuaciones de los usuarios, tenemos:\nEl promedio: {promc:.1f}\nEl número máximo: {maxc}\nEl número mínimo: {minc}.")
            calculo = []
        elif option == "3":
            for j in range(1,len(setdatos[1:])+1):
                calculo.append(setdatos[j][7])
            calcfloat = [float(x) for x in calculo if x.strip() != '']
            promc = (reduce(lambda x,y:x+y,calcfloat)/50)
            maxc = max(calcfloat)
            minc = min(calcfloat)
            print(f"[---RESULTADO---]\nPara las ventas totales, tenemos:\nEl promedio: {promc:.1f}\nEl número máximo: {maxc}\nEl número mínimo: {minc}.")
            calculo = []
        elif option == "4":
            for j in range(1,len(setdatos[1:])+1):
                calculo.append(setdatos[j][8])
            calcfloat = [float(x) for x in calculo if x.strip() != '']
            promc = (reduce(lambda x,y:x+y,calcfloat)/50)
            maxc = max(calcfloat)
            minc = min(calcfloat)
            print(f"[---RESULTADO---]\nPara los años de publicación, tenemos:\nEl promedio: {promc:.1f}\nEl número máximo: {maxc:.0f}\nEl número mínimo: {minc:.0f}")
            calculo = []
        elif option == "5":
            print("¡Muchas gracias!")
            break
        else:
            print("Opción ingresada no es válida, por favor vuelve a intentarlo.")

#llamado de funciones
buscar()
topgames()
estadist()
