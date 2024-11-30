def fibonnaci(sequencia):
    a, b = 0, 1
    lista = []
    
    for i in range(sequencia):
        lista.append(a)
        a, b = b, a + b

    return lista

print(*fibonnaci(10))

# def fibonnaci(sequencia):
#     a, b = 0, 1
    
#     for i in range(sequencia):
#         print(a)
#         a, b = b, a + b


# fibonnaci(10)