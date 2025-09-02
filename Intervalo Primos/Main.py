def main():
    inicio = int(input("Digite o inicio do intervalo: "))
    fim = int(input("Digite o fim do intervalo: "))
    primos = ""
    quantPrimos = 0
    if inicio <= fim:
        while inicio <= fim:
            i = 2
            while inicio != i and inicio > 1:
                if inicio % i == 0:
                    break
                i+= 1
            if inicio == i:
                primos += str(inicio) + " "
                quantPrimos += 1
            inicio += 1
    else:
        while inicio >= fim:
            i = 2
            while inicio != i and inicio > 1:
                if inicio % i == 0:
                    break
                i += 1
            if inicio == i:
                primos += str(inicio) + " "
                quantPrimos += 1
            inicio -= 1
    if quantPrimos == 0:
        print("Intervalo sem primos")
    else:
        print("Há ", quantPrimos, " números primos, e eles são: \n", primos)
    return 0
main()