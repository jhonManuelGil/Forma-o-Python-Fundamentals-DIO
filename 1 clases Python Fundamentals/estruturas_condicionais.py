""" 
Permite o desafio de controle, quando de terminadas expressões 
lógicas são atendidas


IF:
È uma estrutura condicional simple, compuesta por um único desvio, podemos utilizar a palavra reservada
IF. O comando irá testar expressão logica

IF/ELSE:

Uma estrutura condional com dois desvios, podemos utilizar as palabras reservadas
IF e ELSE. 


IF / ELIF / ELSE:
EN alguns cenararios queremos mais de dois desevios, para isso podemos utilizar a palavra reselvada ELIF. O 
ELIF é composto por uma nova expressão logica, que sera testada e caso retorne verdadeiro o bloco de cogigo
sera executado. Caso a expressão retorne falso, o bloco de código.

If Aninhado
Podemos criar estrutura condicionais aninhada, para isso
basta adiconar uma estrutura de contrurura IF/ELIF/ELSE dentro do bloco de código de estrutura
IF/ELIF/ELSE.

IF internario
O if ternario permite escrever uma codição em uma única linha,
Eçle é composta por três partes, a primeraparte retorna caso expressão retorne verdaeiro
a segunda parte retorna caso a expressão retorne falso e a terceira parte sem a expressão não seja atendida.
"""


# 1>  EXEMPLO if:

# Saldo = 250
# saque = float(input("Informe o volor do saque: "))
              
# if Saldo >= saque:
#     print("Saque realizado com sucesso")
# if Saldo <= saque:
#     print("Saldo insuficiente")
    
    
# 2>  EXEMPLO IF / ELSE

# saldo_1 = 5846
# saque_1 = float(input("Informe o valor do saque: "))

# if saldo_1 >= saldo_1:
#     print("Saque realizado com sucesso")
# else:
#     print("Saldo insuficiente ")
    
    
    
    
# 3>  EXEMPLO IF / ELif / else.


# opcao = int(input("Informe uma opção: [1] sacaer \n[2] Extrato: "))


# if opcao == 1:
#     valor = float(input("informe a quantia para o saque: "))

# elif opcao == 2:
#     print("Exibirndo o extrato...")
# else:
#     sys.exit("opção invalida")
    
    
    
#Exempli 4 

# maryor_idade = 18

# idade_epecial = 17

# idade = int(input("Informe sua edade puede CHN "))

# if idade >= maryor_idade:
#     print("Você é maior de idade")
# if idade < maryor_idade:
#     print("Ainda é menhor de idade Não puede CHN ")
    
# print("============================================")


# if idade >= maryor_idade:
#     print("Você é maior de idade puede fazer CNH")
# else:
#     print("Ainda é menhor de idade Não puede fazer CNH ")
    
# print("============================================")
#Exempli 6

# if idade >= maryor_idade:
#     print("Você é maior de idade pode ir a discoteca")
# elif idade == idade_epecial:
#     print("puede ir a la escula de manejo solo aulas teorica")
# else:
#     print("Ainda é menhor de idade Não pode ir a discoteca ")
    
#If Aninhado

# conta_normal = False
# conta__universitaria = False

# saldo = 2000
# sague = 1000
# cheque_especial = 450

# if conta_normal:
    
#     if saldo >= sague:
#         print("Saque realizado com sucesso com cheque especial")
#     elif sague <= (saldo + cheque_especial):
#         print("Saque realizado com sucesso")
#     else:
#         print("Saldo insuficiente para o saque SEM cheque especial")
        
# elif conta__universitaria:
    
#     print("================================")
#     if saldo >= sague:
#         print("Saque realizado con sucesso.")
#     else:
#         print("Saldo insuficiente")
        
# else:
#     print("Conta não achada fale con o Gerente.")


#IF internario
saldo = 1000
saque = 5000
estatus = "sucesso" if saldo >= saque else "falha"
print(f"{estatus} ao realizado o saque")

