# "Na matemática, um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos próprios (excluindo ele mesmo) é igual ao próprio número. 
# Por exemplo o número 6 é perfeito, pois 1+2+3 é igual a 6. 
# Sua tarefa é escrever um programa que imprima se um determinado número é perfeito ou não."


# Identificar Divisores Próprios: Encontrar todos os divisores de X que são menores que ele.
# Para fazer isso, verificamos todos os números de 1 até X-1.
# Se X for divisível por um número i (ou seja, X % i == 0), então i é um divisor de X.
# Calcular a Soma dos Divisores: Somar todos esses divisores próprios.
# Comparar a Soma com o Número: Se a soma dos divisores for igual a X, então X é um número perfeito.
#  Caso contrário, não é.

casos_teste = int(input())

def verifica_divisores(numero):
    divisores = []
    for numeros in range(1, numero):
        if numero % numeros == 0:
            divisores.append(numeros)
    return divisores

for i in range(casos_teste):
    soma = 0
    entrada = int(input())
    divisores_resultado = verifica_divisores(entrada)

    for _ in divisores_resultado:
        soma += int(_)

    if soma == entrada:
        print(f'{entrada} eh perfeito')

    else:
        print(f'{entrada} não eh perfeito')
