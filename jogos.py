import forca
import adivinhacao

def escolher():
    print("*********************************")
    print("******* Escolha seu jogo  *******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação ")
    jogo = int(input("qual jogo?"))

    if(jogo == 1):
        print("Jogo da forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo da Adivinhação")
        adivinhacao.jogar()
if(__name__ == "__main__"):
    escolher()
