#Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. 
#O último dado, que não entrará nos cálculos, contém o valor de idade negativa.
#Calcular e imprimir a idade média deste grupo de indivíduos.

numeros = 0
quantidade_numeros = 0
media = 0

while True:
    entrada = int(input())
    if entrada < 0:
        break

    numeros += entrada
    quantidade_numeros += 1

media = numeros / quantidade_numeros
print(f'{media:.2f}')
