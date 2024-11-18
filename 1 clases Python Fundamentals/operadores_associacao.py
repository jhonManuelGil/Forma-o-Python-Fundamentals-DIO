""" 
São operadores utilizado para verificar se uma objeto esta 
presente em uma sequência
"""

curso = "curso de Python"
frutas= ["laranja", "maça", "uva"]
saques = [562, 258]


prov_1 = "Python" in curso
#true
print(prov_1)

prov_2 = "Pera" not in frutas
#true
print(prov_2)

prov_3 = 200 in saques
#false
print(prov_3)
