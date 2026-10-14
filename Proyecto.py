setdatos = []


with open ("gsales50.csv", "r")  as f:
    for linea in f:
        setdatos.append(linea.strip().split(","))



print(setdatos[0])