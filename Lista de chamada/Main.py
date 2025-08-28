def main():
    quantAlunos = int(input("Digite a quantidade de alunos: "))

    while quantAlunos < 1:
        print("Número inválido, digite novamente")
        quantAlunos = int(input("Digite a quantidade de alunos: "))
    
    nomes = [""] * quantAlunos

    i = 0

    while i in range(len(nomes)):
        nomes[i] = input("Digite o nome do aluno: ")
        i += 1
    print(nomes)
    return 0
main()