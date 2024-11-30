# Escreva uma função que calcule a média dos elementos em uma lista. Aplique a função em uma lista de números [10, 20, 30, 40, 50].

lista = [10, 20, 30, 70, 50]

def media(lista):
    soma = 0
    for i in lista:
        soma += i
    
    return soma / len(lista)

print(media(lista))

# def media(lista):
#     soma = 0
#     for i in lista:
#         soma += i
    
#     print(soma / len(lista))

# media(lista)