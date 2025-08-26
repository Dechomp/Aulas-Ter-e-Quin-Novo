def main():
    idade = int ( input("Digite a sua idade: "))
    
    while idade < 0:
        print("Idade inválida, digite novamente")
        idade = int ( input("Digite a sua idade: "))
    
    if idade > 17:
        print("Entrada liberada!")
    elif idade >= 16:
        acom = input("Você está acompanhado? ")
        if  acom == "S" or acom == "s":
            print("Pode entrar!")
        else:
            print("Sai daqui")
    else:
        print("Não aceitamos crianças")   
    return 0
main()