"""
As estrutura de retetição são estrutura utilizadas para repetir um trecho de código
determinada vecez com uma expressão lógica

Comando FOR
È usado para percorrer um objeto um objeto iterável.
Fas sentido de usar um FOR quando sabemos o número exato de vezes 
que nosso bloco de código deve ser executado.

Função range:
è uma função built-in do Python ela é para produzir uma sequência de número inteiros a partir de um incio
(inclusivo) para um fim (exclusivo).


WHILE:
È usado para repatir um bloco de codigo várias vezes. Fas sentido usar WHILE quando não sabemos o número 
exatos de vecez que nosso bloco de código deve ser executado.

"""

# a = int(input("Informe um numero: "))
# print(a)

# a += 1
# print(a)
# a += 1
# print(a) 


#exemplo 2 FOR utilizabndio um interavel

# text = input("informe un text: ")
# vagais = "AEIOU"

# for letra in text:
#     if letra.upper() in vagais:
#         print(letra, end="")
# else:
#     print() #diaciona en otra Linha
    
#exemplo 3 utilizabdo a função built-in range

# for num in range(0, 12):  
#   print(num)
  
# print("==========================")

# for num_2 in range(0, 155, 8):
#     print(num_2, end=" ")
    

#exemplo 3

# opacao = - 1

# while opacao != 0:
#   opacao = int(input("[1] sacar \n[2] extrato \n[0] sair \n: "))
  
#   if opacao == 1:
#     print("Sacando.... ")
    
#   elif opacao == 2:
#     print("Exibir o Extrato ")

# else:
#   print("Obrigado por usar o sistema")


#exemplo 4


opacao = -1

while opacao != 0:
  opacao = int(input("Intradusca um número "))
  
  if opacao == 1:
    print("Numero escrito: ", opacao)
    break
  
    
#exemplo 5

# while True:
#   numero = int(input("informe un numero: "))
  
#   if numero == 10:
#     break
  
#   print(numero)
  


#exemplo 5

while True:
  numero_2 = int(input("informe um numero: "))
  
  if numero_2 == 10:
   break
 
 
  if numero_2 % 2 == 0:
    continue
    
  print(numero_2)
  #forma erroa de fazer
  # if numero_2 % 2 == 0:
  #   continue
  
  # if numero_2 == 10:
  #   break