"""
São operadores utilizado em conjunto com os operadores
de compraração, para mostar uma expressão lógica



"""

"""  
opredor  lógico AND (e) - é verdadeiro se ambos os operandos forem verdadeiros
saldo = 1000
sague = 250
limite = 536

saldo >= sague and sague <= limite

falso

===================================
operador  lógico OR (ou) - é verdadeiro se pelo menos um dos operandos for verdade

saldo = 1000
sague = 250
limite = 536

saldo >= sague or sague <= limite
verdadero
====================================================================

operador not
é verdadeiro se o operando for falso e vice versa

contatos_emergencia = []

not 100 > 1500

not contatos_emergencia
#true

not "saque 1500: "
#false

not ""
#true

====================================================================
EJEMPLO

saldo = 1000
saque = 250
limite = 536
contatos_emergencia = true

saldo >= saque and saque <= limite or contatos_emergencia and saldo >= saque
#true


(saldo >= saque and saque <= limite) or (contatos_emergencia and saldo >= saque)
#true


"""
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(True and True)
print(False and False)



saldo = 1000
saque = 250
limite = 536
contatos_emergencia = True



resul_1 = saldo >= saque and saque <= limite or contatos_emergencia and saldo >= saque
#true
print("===========")
print(resul_1)

print("===========")
resul_2 = (saldo >= saque and saque <= limite) or (contatos_emergencia and saldo >= saque)
#true

print(resul_2)