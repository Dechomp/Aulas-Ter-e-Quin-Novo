def main():


    nome = input("Digite o seu nome: ")

    i = 0

    for i in range(len(nome)):
        print(nome[i])
    print("O seu nome tem ", i + 1, " letras")

    return 0
main()