def main():

    num = int(input("Digite um número: "))

    i = len( str(num)) - 1
    ordem ="" 

    while i >= 0:
        ordem += str(num)[i]
        i -= 1
    print("Número na ordem inversa: ", ordem)


    return 0
main()