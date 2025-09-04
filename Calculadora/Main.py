from Sub import sub
from Mult import mult
from Div import div
def main():
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))



    print("A soma de ", numero1 , " + ", numero2, " = ", soma(numero1, numero2))
    print("A subtração de ", numero1 , " - ", numero2, " = ", sub(numero1, numero2))
    print("A multiplicação de ", numero1 , " * ", numero2, " = ",mult(numero1, numero2))
    print("A divisão de ", numero1 , " / ", numero2, " = ", div(numero1, numero2))
    return 0

def soma(num1, num2):

    return num1 + num2

main()