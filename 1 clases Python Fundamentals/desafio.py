# # Solicita ao usuário um número inteiro
# numero = int(input())

# # Verifica se o número é par ou ímpar e imprime o resultado
# if numero % 2 == 0:
#     print("Par")
# else:
#     print("Ímpar")


# def verificador_ano_bissexto():
# #     """Verifica se um ano é bissexto.

# #     Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400.
# #     """

#     ano = int(input())

#     if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
#         print("SIM")
#     else:
#         print("NÃO")

# verificador_ano_bissexto()


def verificar_ano_bissexto():
    # Recebe o ano como entrada
    ano = int(input())

    # Verifica se o ano é bissexto
    divisivel_por_4 = ano % 4 == 0
    divisivel_por_100 = ano % 100 == 0
    divisivel_por_400 = ano % 400 == 0

    if divisivel_por_4 and (not divisivel_por_100 or divisivel_por_400):
        print("SIM")
    else:
        print("NÃO")

# Chama a função
verificar_ano_bissexto()