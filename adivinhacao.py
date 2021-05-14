def jogar():
    import random


    print("*********************************")
    print("Bem vindo ao jogo da adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Escolha o nível"))

    if(nivel==1):
        tentativas = 12
    elif(nivel==2):
        tentativas = 9
    else:
        tentativas = 7


    for rodada in range(1, tentativas +1):
        print("Tentativas {} de {}".format(rodada,tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("você digitou ", chute_str)
        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou. Chutou muito alto")
            elif menor:
                print("Você errou. Chutou muito baixo")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        rodada = rodada + 1

    print("fim do jogo")
if(__name__ == "__main__"):
    jogar()