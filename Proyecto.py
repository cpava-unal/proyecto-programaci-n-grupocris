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
                    break
                cont += 1
    print(f"Se encontro {x} en {cont} registros")

buscar()
