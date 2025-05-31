"""
O que é funções:
Função é um bloco de código indentificado por um nome e pode receber uma lista 
de parâmetro 
 
"""


# def exibir_memsagem():
#     print("Olá, mundo!")
    
    
# def exibir_memsagem2(nome):
#     print(f"Olá, mundo! 2 {nome}")
    
    
# def exibir_memsagem3(nome="Antomio"):
#     print(f"Olá, mundo! 3 {nome}")
    

# print("----1------")
# exibir_memsagem()
# print("-----2-----")
# exibir_memsagem2(nome="luis")
# print("-----0-----")
# exibir_memsagem3()
# print("-----3-----")
# exibir_memsagem3(nome="Jhon")


# def calcular_total(numero):
#     return sum(numero)



# def retornar_antecessor_e_sucessor(numero):
#     antecessor = numero - 1
#     sucessor = numero + 1
    
#     return antecessor, sucessor


# print(calcular_total([10, 20, 25, 23, 98])) #176
# print("------")
# print(retornar_antecessor_e_sucessor(10)) #(9, 11)



""" 
Retornando valores.

Para retornar um valor, utilizando a palavra reservada return 
tada função Python retorna none por padrão, Diferente de autras 
linguajens de programação em Python uma função pode retornar mais de um valor.

Argumentos nomeados

funcçoes também podem ser chamada usando argumentos nomeados da forma chave=valor
"""

def salvar_carro(marca, modelo, ano, placa):
    #salva carro no banco de dados...
    
    print(f"Carro inserido com sucesso!: {marca}/{modelo}/{ano}/{placa}")

print("=============1==========")
salvar_carro("Fiat", "Palio", 1289, "ABC-1256") # Carro inserido com sucesso!:  Fiat/Palio/1289/ABC-1256
print("=============2========== \n")
salvar_carro(marca="Fiat", modelo="Palio", ano="1289", placa="ABC-1256") #Carro inserido com sucesso!:  Fiat/Palio/1289/ABC-1256
print("=============3========== \n")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1289, "placa": "ABC-1256"}) # Carro inserido com sucesso!:  Fiat/Palio/1289/ABC-1256