def main():

    num = int (input("Digite um número: "))

    i = 2

    while num != i and num > 1:
        if num % i == 0:
            break
        i += 1
    
    if num == i:
        print("O numero ", num, " é primo")
    else:
        print("O número ", num, " não é primo")

    return 0
main()