def main():
    num = int(input("Digite um número: "))
    quantDiv = 1
    divisores = "1 "
    i = 2
    while num >= i and num > 1:
        if num % i == 0:
            quantDiv += 1
            divisores += str(i) + " "
        i += 1
    if quantDiv == 2:
        print("O número", num," é primo")
    elif num < 0:
        print("O número ", num, " é negativo, portatanto e disconsiderado no cálculo")
    elif num == 0:
        print("O número 0 não é primo pois é divisivel por todos os número exceto ele mesmo descumprindo a 2ª regra")
    elif num == 1:
        print("O número 1 não é primo pois atende as duas regras porém possui apenas um número divisor que é ele mesmo")
    else:
        print("O número ", num," não é primo por que tem ", quantDiv, " e eles são:\n", divisores)
    return 0
main()