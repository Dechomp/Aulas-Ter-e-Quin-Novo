from Sub import sub
from Mult import mult
from Div import div
def main():
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
    

    add = soma(numero1, numero2)
    subt = sub(numero1, numero2)
    divi =  div(numero1, numero2)
    print("A soma de ", numero1 , " + ", numero2, " = ", add)
    print("A subtração de ", numero1 , " - ", numero2, " = ", subt)
    print("A multiplicação de ", numero1 , " * ", numero2, " = ",mult(numero1, numero2))
    print("A divisão de ", numero1 , " / ", numero2, " = ", divi)
    return 0

def soma(num1, num2):

    return num1 + num2

main()