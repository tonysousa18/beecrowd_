# #Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior.
# Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente.
# Mostre o vetor em seguida.

numero = int(input())

lista_numeros = [numero]

for i in range(1, 10):
    lista_numeros.append(lista_numeros[i-1] * 2)

for i in range(10):
    print(f"N[{i}] = {lista_numeros[i]}")
