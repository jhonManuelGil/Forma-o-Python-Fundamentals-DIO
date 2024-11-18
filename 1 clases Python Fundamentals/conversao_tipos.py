""" 
em algun momentos é necesario será necesario converter o tipo de uma variavel
para manipulamos a variavel de forma mas direta


"""




# preso = 10

# print(preso)
# # output: 10


# preso = float(preso)
# print(preso)
# #10.0


# preso = 10 / 2
# print(preso)
# # 5.0

preso_1 = 10.0

idade_1 = 28
print("************************")
print(str(preso_1))
#10.5


print(str(idade_1))
#28

text = f"idade {idade_1} preco {preso_1} total."
#idade 28 preco 10.0 total.
print(text)

print("************************")

# preso_2 = "10.25"

# print(float(preso_2))

# presso = "pithon"
# print(float(presso))

###

# traceback (most recent call last):
#     File "main.py", line 3, in <madulo>
#     print(float(presso))

# ValueError: could not convert string to float: "python"

print("************************")


valor = 20

valor_str = str(valor)

print(type(valor))
print(type(valor_str))
