#maiúcula, minuscula e titulo

curso = "  #Python#  "
print(curso.strip())


# >>>> Python

print(curso.lstrip())
# >>>> "Python " 


print(curso.rstrip())

#>> "  Python"

#juncões e centralização
print("=========juncões e centralização===========")
curso1 = "Jhon"

print(curso1.center(10, "#"))

print(".".join(curso1))
print("")



print("=========")


nome = "Jhon Manuel"
print(nome.upper())
print(nome.lower())
print(nome.title())
print("=========")
print("")

#eliminar espaço
text = "  Hola mundo    "

print("=========")
print(text + "=")
#print(text.split())
print(text.strip() + "=")
print(text.rstrip() + "=")
print(text.lstrip() + "=")
print("")
print("========= \n")

menu = "mundoTrue"

print("=====" + menu + "=====")

print(menu.center(15))
print(menu.center(50, "#"))
print("")


print("_".join(menu))