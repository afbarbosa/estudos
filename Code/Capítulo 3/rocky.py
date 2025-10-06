import random

movements = ['Papel','Tesoura','Pedra']
vencedores = ['Você venceu','Você perdeu','Empatou']
jogada_pc = ""
resultado = ""
jogador = ""

def jogada():
    jogada_pc = random.choice(movements)
    return jogada_pc

def conflito(jogada_pc):
    jogador = input("Escolha entre, Pedra, Papel ou Tesoura ")
    if jogador.lower().capitalize() in movements:
        if jogada_pc.lower() == jogador.lower():
            resultado = vencedores[2]
        elif jogada_pc == "Pedra" and jogador.lower() == "tesoura":
            resultado = vencedores[1]
        elif jogada_pc == "Tesoura" and jogador.lower() == "papel":
            resultado = vencedores[1]
        elif jogada_pc == "Papel" and jogador.lower() == "pedra":
            resultado = vencedores[1]
        else:
            resultado = vencedores[0]
        return resultado, jogador
    else:
        print("Erro: jogada inválida. Escolha entre: Papel, Tesoura ou Pedra.")

def definicao (resultado, jogador, jogada_pc):
    print(f"Sua jogada: {jogador.capitalize()} | Jogada do PC: {jogada_pc} → {resultado}") 

def jogo():
    jogar = True
    while jogar:
        jogada_pc = jogada()
        resultado, jogador = conflito(jogada_pc)
        definicao(resultado, jogador, jogada_pc)
        continua = input("Quer jogar de novo? Sim(S), Não(N): ")
        if continua.lower() == "n":
            jogar = False
            print("Fim de jogo")
        else:
            jogar = True
            
jogo()





    

            
            
        



