while True:
    try:
        lista_valores = list(map(int, input().split()))  

        if len(lista_valores) != 3:
            continue 

        if all(num == lista_valores[0] for num in lista_valores): #Se todos forem iguais
            print('*')
        else:
            if lista_valores.count(0) == 1: # Se tiver uma ocorrencia de Zero
                indice = lista_valores.index(0) #Vai procurar o indice de zero
            else: #Se a unica ocorrencia for 1
                indice = lista_valores.index(1) #Vai procurar o indice de 1

            match indice:
                case 0:
                    print('A')
                case 1:
                    print('B')
                case 2:
                    print('C')

    except EOFError:
        break 
    except ValueError:
        continue  
