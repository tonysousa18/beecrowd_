colocacao = int(input())

while True:
    if colocacao > 100:
        continue

    if colocacao == 1:
        print('Top 1')
        break
    
    elif colocacao <= 3:
        print('Top 3')
        break

    elif colocacao <= 5:
        print('Top 5')
        break

    elif colocacao <= 10:
        print('Top 10')
        break

    elif colocacao <= 25:
        print('Top 25')
        break

    elif colocacao <= 50:
        print('Top 50')
        break
    
    elif colocacao <= 100:
        print('Top 100')
        break