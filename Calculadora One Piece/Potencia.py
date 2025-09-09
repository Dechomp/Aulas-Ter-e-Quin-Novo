import math
def potencia(num1, num2):
    i = 2

    numPotencializado = num1
    print("O ", num1, " elevado à ", num2, " é ", math.pow(num1, num2))
    while num2 < 0:
        print("Este programa não suporta ainda potencias negativas, digite novamente") 
        num2 = input("Digite o número novamente: ")
    
    if num2 == 0:
        print(num1, " elevado a 0 é = 1")
    else:
        while i <= num2:
            numPotencializado *= num1
            i += 1
        print("O ", num1, " elevado à ", num2, " é ", numPotencializado)

        
    return 0