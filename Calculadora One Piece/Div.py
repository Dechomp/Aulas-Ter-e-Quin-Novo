
from VerificarZero import verificarZero
def div(num1, num2):
    if verificarZero(num2):
        print("Divisão por zero é impossivel Luffy")
    else:
        print("A divisão de ", num1, " / ", num2, "= ", num1 / num2)

    return 0