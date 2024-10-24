#Faça um programa que leia um vetor A[100]. 
#No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 e o valor armazenado em cada uma das posições.


lista = list(range(100))

for i in lista:
    valor = float(input())
    lista[i] = valor

for _, valor in enumerate(lista):
    if valor <= 10:
        print(f'A[{_}] = {valor:.1f}')
