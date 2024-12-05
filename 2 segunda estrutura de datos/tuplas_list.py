"""
Tuplas são estrutura de dado ,uito parecidas com as lista, a principal deferença é que tuplas são imutavais
enquanto lista são mutaveis
Podemos criar tuplas atrvés da classe TUPLE, ou colocando valores separados por vírgula de parenteses.

"""
# EXEMPLO
# frutas = ("maça", "laranja", "uva",)

# letras = tuple("python")

# numero = tuple([1, 9, 4, 7])

# pais = ("brasil", "rusia",)

frutas = ("maça", "laranja", "uva", "pera",)

print(frutas[1]) #laranja
print(frutas[2])#uva

#numero negativo

print(frutas[-1]) #uva
print(frutas[-2]) #laranja


print("================= \n")

matriz = (
    (1, "a", 3),
    ("g", 5, 6),
    (7, 8, "i")
)

print(matriz[0]) #(1, 'a', 3)
print("")
print(matriz[0][0]) # 1
print("")
print(matriz[0][-1]) # 3
print("")
print(matriz[-1][-1]) # i

print("================= \n")
tupla = ("p", "y", "t", "h", "h", "o", "n",)


print(tupla[2:]) #('t', 'h', 'h', 'o', 'n')
print(tupla[:2]) #('p', 'y')
print(tupla[1:3]) #('y', 't')
print(tupla[0:3:1]) #('p', 'y', 't')
print(tupla[::]) #('p', 'y', 't', 'h', 'h', 'o', 'n')
print(tupla[:: -1]) #('n', 'o', 'h', 'h', 't', 'y', 'p')


print("================= \n")

carros = ("gol", "celta", "chery")


for indice, carros in enumerate(carros):
  print(f"{indice}: {carros}")
"""
0: gol
1: celta
2: chery
"""
print("================= \n")
carros = ("gol", "celta", "chery")

print(len(carros))


print("================= \n")