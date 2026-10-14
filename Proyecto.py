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
    print(f"Se encontro {x} en {cont} registros")


#funcion para imprimir el top de juegos segun lo desea el usuario
def topgames():
    top = int(input("Ingrese el top de juegos que desea Consultar: "))
    print(f"El top {top} de juegos mas vendidos son:")
    print("# | Nombre del Juego                              |         Desarrolador         | Plataforma |  Año   |")
    for i in setdatos[1:top+1]:
        print(f"{i[0]:^2}| {i[1]:<45} | {i[4]:^28} | {i[2]:^10} | {i[8]:^6} |")

#llamado de funciones
buscar()
topgames()
