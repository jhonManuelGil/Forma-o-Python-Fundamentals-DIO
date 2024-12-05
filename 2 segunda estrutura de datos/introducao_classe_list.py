
"""


"""

print("=======")
fruta = ["laraja", "maça", "melão"]

print(fruta)
print("======= \n")

fruta = []
print(fruta)
print("======= \n")

letra = list("Python")
print(letra) 
print("======= \n")

numero = list(range(10))
print(numero)
print("======= \n")

carro =  ["ferrari", "F8", "voll", 12552, "são paulo", True, "\n"]
print(carro)
print("=======")


# ======================= MAtriz ==========================

matriz = [
    [1, "a", 3],
    ["y", 5, 6],
    [7, 8, "m"]
]

print("====MAtriz===")
print(matriz[0])
print("=======")
print(matriz[0][-1])
print("=======")
print(matriz[0][0])
print("=======")
print(matriz[-1][-1])
print("=======")


lista_2 = ["P", "y", "t", "h", "o", "n"]


print(lista_2[2:])    #['t', 'h', 'o', 'n']
print(lista_2[:2])    #['P', 'y']
print(lista_2[1:3])   #['y', 't']
print(lista_2[0:3:2]) #['P', 't']
print(lista_2[::-1])  #['n', 'o', 'h', 't', 'y', 'P']
print(lista_2[::])    #['P', 'y', 't', 'h', 'o', 'n']
print("======= \n")

carron = ["gol", "maravel", "missan"]

for indice, carron in enumerate(carron):
    print(f"{indice}: {carron}") #gol


print("==== Filtro versão 1 === \n")

num_0 = [1, 2, 3, 4, 58, 89, 106]

par = []

for num_m in num_0:
    if num_m % 2 == 0:
        par.append(num_m)

print(par) #[]

print("=== Filtro versão 2 ==== \n")

num_3 = [1, 2, 3, 4, 58, 89, 606]

pares = [num_t for num_t in num_3 if num_t % 2 == 0]

print(pares)

print("=== modificado valores ==== \n")


num_modificado = [1, 2, 45, 67, 3, 6, 2, 89, 12, 0]
guadrado = []

for modificado in num_modificado :
    guadrado.append(modificado ** 2)

print(guadrado)

print("=== versão 2 ==== \n")

num_modificado_2 = [1, 2, 45, 67, 3, 6, 2, 89, 12, 0]
guadrado_2 = [modificado_2 ** 2 for modificado_2 in num_modificado_2]

print(guadrado_2) # [1, 4, 2025,

print("======= \n")


# [].append

listrado = [1, "python", [24, 15, 9]]

print(listrado)
print(listrado.clear())
print(listrado)

print("=== Métodos da classe list ==== \n")

lista_clas = [1, "python", "TROPA", 2, [2, 4, 78]]

l2 = lista_2.copy()

print(lista_2) # ['P', 'y', 't', 'h', 'o', 'n']
print("")
print(id(l2), id(lista_2))

l2[0] = 89
print("")
print(l2) # [89, 'y', 't', 'h', 'o',
print("")

# Caunt
print("==== []Caunt === \n")


cores = ["verde", "azul", "amarillo", "rojo", "rojo", "rojo", "azul"]

print(cores.count("verde"))
print(cores.count("azul"))
print(cores.count("rojo"))

print("=== EXTEND ==== \n")

lenguaje = ["python", "JS", "rubi", "C"]

print(lenguaje)
print("")
print(lenguaje.extend(["java", "c++"]))
print("")
print(lenguaje)


print("===INDEX==== \n")

lengu = ["python", "JS", "rubi", "C++"]

print(lengu.index("C++"))
print("")
print(lengu.index("JS"))
print("")
print(lengu.index("python"))

print("=== POP ==== \n")

lengua = ["python", "JS", "rubi", "C++"]

print(lengua.pop())
print("")
print(lengua.pop())
print("")
print(lengua.pop())
print("")
print(lengua.pop(0))

print("==== REMOVE ==== \n")

coloRes = ["verde", "azul", "amarillo", "rojo", "azules"]

coloRes.remove("verde")
print(coloRes)

print("")

print("==== REVERSO ==== \n")

cor = ["verde", "azul", "amarillo", "rojo", "azules"]

cor.reverse()
print(cor) #['azules', 'rojo', 'amarillo', 'azul', 'verde']
print("")


print("==== .SORT ==== \n")

cor_sort = ["verde", "azul", "violeta", "rojo", "azules"]

cor_sort.sort()
print(cor_sort) # ['azul', 'azules', 'rojo', 'verde', 'violeta']
print("")

cor_sort.sort(reverse=True)
print(cor_sort) # ['violeta', 'verde', 'rojo', 'azules', 'azul']
print("")

cor_sort.sort(key=lambda x: len(x))
print(cor_sort) # ['rojo', 'azul', 'verde', 'azules', 'violeta']
print("")


cor_sort.sort(key=lambda x: len(x), reverse=True) 
print(cor_sort) #['violeta', 'azules', 'verde', 'rojo', 'azul']
print("")


print("==== LEN ==== \n")
cor_sort = ["verde", "azul", "violeta", "rojo", "azules"]

len(cor_sort)
print(cor_sort) # ['verde', 'azul', 'violeta', 'rojo', 'azules']
print("")


print("==== SORTED ==== \n")

cor_sort = ["verde", "azul", "violeta", "rojo", "azules"]

sorted(cor_sort, key=lambda x: len(x))
print(cor_sort) # ['verde', 'azul', 'violeta', 'rojo', 'azules']
print("")

cor_sort = ["verde", "azul", "violeta", "rojo", "azules"]

sorted(cor_sort, key=lambda x: len(x), reverse=True)
print(cor_sort) # ['verde', 'azul', 'violeta', 'rojo', 'azules']
print("")

print(sorted(cor_sort)) #['azul', 'azules', 'rojo', 'verde', 'violeta']




print("======= \n")