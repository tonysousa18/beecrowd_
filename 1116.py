n = int(input())

for i in range(n):

    a = int(input())
    b = int(input())
    
    try:
        print(a / b)
    except ZeroDivisionError:
        print('divisão impossivel')