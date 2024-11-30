#Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

valores = []

try:
    for i in range(1, 3):
        valor = int(input())
        valores.append(valor)

    maior_elemento = valores[0]

    for elemento in valores:
        if elemento > maior_elemento:
            maior_elemento = elemento

    print(maior_elemento)
    print(valores.index(maior_elemento) + 1)

except EOFError:
    print('Nenhum valor inserido')

