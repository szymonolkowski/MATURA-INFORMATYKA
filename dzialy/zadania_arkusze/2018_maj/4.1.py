with open("Dane_PR/przyklad.txt") as file:
    lista = file.read().splitlines()

res = "".join(lista[i][9] for i in range(39, len(lista) + 1, 40))
print(res)