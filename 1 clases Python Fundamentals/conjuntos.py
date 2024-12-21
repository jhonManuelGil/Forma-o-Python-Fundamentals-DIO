""" 
Conjunto ou set é uma estrutura de dados notiva da lenguajem de Python
capazes de armazenar uma sequência não ordenada de valores unicos.

não armnazena itens duplicado

"""

# 1. Operaciones con conjuntos de enteros
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Mostrar los conjuntos
print("Conjunto 1:", set1)
print("Conjunto 2:", set2)

# Unión
union = set1 | set2
print("Unión:", union)

# Intersección
interseccion = set1 & set2
print("Intersección:", interseccion)

# Diferencia
diferencia = set1 - set2
print("Diferencia (set1 - set2):", diferencia)

# Diferencia simétrica
diferencia_simetrica = set1 ^ set2
print("Diferencia simétrica:", diferencia_simetrica)


# 2. Operaciones con conjuntos de strings
europa = {"España", "Francia", "Italia", "Alemania", "Portugal"}
america = {"Argentina", "Brasil", "México", "Colombia", "España"}

# Mostrar los conjuntos
print("\nConjunto Europa:", europa)
print("Conjunto América:", america)

# Intersección
interseccion_paises = europa & america
print("Países en ambos conjuntos:", interseccion_paises)

# Diferencia (solo Europa)
solo_europa = europa - america
print("Países solo en Europa:", solo_europa)

# Unión
union_paises = europa | america
print("Todos los países sin repetir:", union_paises)

# Diferencia simétrica
diferencia_simetrica_paises = europa ^ america
print("Países que están solo en un conjunto:", diferencia_simetrica_paises)
