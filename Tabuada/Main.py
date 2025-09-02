def main():
    inicio = int( input("Digite o inicio do seu intervalo: "))
    fim = int( input("Digite o fim do seu intervalo: "))

    if inicio <= fim:
        while inicio <= fim:
            i = 1
            print("Tabuada do ", inicio)
            while i < 11:
                print(inicio, "X", i, "=", inicio * i)
                i += 1
            inicio += 1
            print("\n")
    else: 
        while inicio >= fim:
            i = 1
            print("Tabuada do ", inicio)

            while i <= 10:
                print(inicio, "X", i, "= ",inicio*i) 
                i += 1  
            inicio -= 1
            print("\n")
    return 0
main()