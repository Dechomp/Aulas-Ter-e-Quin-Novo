import random
def main():
    notas = [0.0] * 4

    i = 0
    media = 0
    while i < 4:
        notas[i] = random.uniform(0, 10)
        print("A ", i + 1, f"ª nota foi de {notas[i]:,.3}")
        media += notas[i]
        i += 1
    
    media /= i
    print(f"A media do pikachu foi de {media:,.3}")

    if media >= 6:
        print("Aprovado, boas férias!")
    elif media >= 4:
        print("Recuparação, vai ficar aqui em dezembro Muahahaha!!!")
    else:
        print("Pelo amor, sai daqui")

    return 0
main()