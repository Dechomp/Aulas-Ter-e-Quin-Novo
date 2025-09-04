def div(num1, num2):

    if isZero(num2):
        return "Divisão impossivel"
    else:
        return num1 / num2


def isZero(num):
    if num == 0:
        return True # 1
    else:
        return False # 0