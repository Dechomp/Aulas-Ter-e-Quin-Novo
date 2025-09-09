from VerificarZero import verificarZero

def resto(num1, num2):
    if verificarZero(num2):
        print("Não exite resto de uma divisão pois não existe divsião por zero")
    else:
        print("O resto da divisão de ", num1, " % ", num2, " = ", num1 % num2)
    return 0