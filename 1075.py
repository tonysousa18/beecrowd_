#Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.
valor = int(input())

for _ in range(1, 10001): #O(N)
    if _ % valor == 2:
        print(_)
