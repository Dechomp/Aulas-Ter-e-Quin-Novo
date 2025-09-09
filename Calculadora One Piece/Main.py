from Mult import mult
from Potencia import potencia
from Div import div
from Raiz import raiz
from Resto import resto
from Soma import soma
from Sub import sub


def main():
    while True:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o seu segundo número: ")) 

        print("Digite \n+  Para somar \n- Para subtrair \n* para Multiplicar \n/ Para dividir\n% Para calcular o resto\n^ Para potencializar\n√ ou 2 Para calcular a raiz")
        
        operacao = input("Digite qual operação você deseja realizar: ")
        
        match operacao:
            case "+":
                soma(num1, num2)
            case "-":
                sub(num1,num2)
            case "*":
                mult(num1, num2)
            case "/":
                div(num1,num2)
            case "%":
                resto(num1, num2)
            case "^":
                potencia(num1, num2)
            case "2":
                raiz(num1, num2)
            case "√":
                raiz(num1, num2)
            case _:
                print("Valor Incorreto digite novamente\n")
        continuar = input("Deseja continuar? Digite S para sim ou qualquer outra tecla para sair: ")
        print("\n")
        
        if continuar != "S" and continuar != "s":
            break
    print("Receba!!! 🍖🍖🍖🍖🐔🐔🐔🐔🐟🐠🐡🦈🍥")
    return 0
main()