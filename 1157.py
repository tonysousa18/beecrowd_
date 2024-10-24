#Ler um número inteiro N e calcular todos os seus divisores.
valor = int(input())

divisores = 0

for i in range(1, 100):
    if valor % i == 0:
        divisores = i
        print(divisores)
