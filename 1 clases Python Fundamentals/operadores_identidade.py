""" 
São operadores utilizado para comparar se os dois objeto
testados ocupam a mesma posição na memoria.

"""

curso = "curso do Python"
nome_curso = curso
saldo, limite = 200, 200

numm0 = curso is nome_curso
# True
print(numm0)
num_1 = curso is not nome_curso
#false
print(num_1)

num_2 = saldo is limite
#false
print(num_2)

