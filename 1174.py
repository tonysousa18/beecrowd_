lista = list(range(100))

for i in lista:
    valor = float(input())
    lista[i] = valor

for _, valor in enumerate(lista):
    if valor <= 10:
        print(f'A[{_}] = {valor:.1f}')
