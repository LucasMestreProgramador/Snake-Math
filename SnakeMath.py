# -*- coding: UTF-8 -*-
# Importar as bibliotecas
import pygame
from random import randint
import time

# Iniciar o pygame e verificar se houve algum erro na inicialização
try: 
    pygame.init()
    print("Jogo iniciado!")
except:
    print("O módulo pygame não foi inicializado com sucesso! :(")

# Definir as cores e medidas
verde = (0, 255, 127),
azul = (28, 134, 238)
amarelo = (255, 255, 0)
vermelho = (255, 48, 48)
preto = (0, 0, 0)
branco = (255, 255, 255)
largura_da_tela = 640 
altura_da_tela = 520 
tamanho_da_cobra = 10

# Criar a tela de exibição
tela_de_exibicao = pygame.display.set_mode((largura_da_tela,altura_da_tela))

# Criar o relógio do pygame
relogio = pygame.time.Clock()

# Definir um título para o jogo
pygame.display.set_caption("Snake Math")

# Criar a tela e exibir a mensagem de fim de jogo

def exibir_texto(texto, cor_texto, tamanho_fonte, x, y):
    font = pygame.font.SysFont(None, tamanho_fonte, bold = True)
    texto_1 = font.render(texto, True, cor_texto)
    tela_de_exibicao.blit(texto_1, [x, y])

# Função criada para criar a cobra

def criar_cobra(cobra_horizontal_vertical):
    for horizontal_vertical in cobra_horizontal_vertical:
        pygame.draw.rect(tela_de_exibicao, azul, [horizontal_vertical[0], horizontal_vertical[1], tamanho_da_cobra, tamanho_da_cobra])

# Função criada para criar os valores certo e errado

def criar_acerto_erro(posicao_horizontal_acerto, posicao_vertical_acerto, posicao_horizontal_erro, posicao_vertical_erro, vermelho, amarelo, cores):
    print(cores)
    if cores >= 1 and cores <= 5:
        pygame.draw.rect(tela_de_exibicao, vermelho, [posicao_horizontal_acerto, posicao_vertical_acerto, tamanho_da_cobra, tamanho_da_cobra])
        pygame.draw.rect(tela_de_exibicao, amarelo, [posicao_horizontal_erro, posicao_vertical_erro, tamanho_da_cobra, tamanho_da_cobra])
    else:
        pygame.draw.rect(tela_de_exibicao, amarelo, [posicao_horizontal_acerto, posicao_vertical_acerto, tamanho_da_cobra, tamanho_da_cobra])
        pygame.draw.rect(tela_de_exibicao, vermelho, [posicao_horizontal_erro, posicao_vertical_erro, tamanho_da_cobra, tamanho_da_cobra])

operacao = randint(1,5)
operacao2 = randint(1,3)
erro_sorteado = randint(1,3)
fase = 1
timer = 400
cores = randint(1,10)

# Função voltada ao desenvolvimento do jogo

def desenvolver_jogo(operacao, erro_sorteado, fase, timer, cores, operacao2):
    # Definir as posições dos valores certos e errados e criar a tela de fim de jogo
    sair = True
    fim_de_jogo = False
    posicao_horizontal = randint(0, (largura_da_tela - tamanho_da_cobra) / 10) * 10
    posicao_vertical = randint(40, 480 / 10) * 10
    posicao_horizontal_acerto = randint(0, (largura_da_tela - tamanho_da_cobra) / 10) * 10
    posicao_vertical_acerto = randint(40, 480 / 10) * 10
    posicao_horizontal_erro = randint(0, (largura_da_tela - tamanho_da_cobra) / 10) * 10
    posicao_vertical_erro = randint(40, 480 / 10) * 10
    velocidade_horizontal = 0
    velocidade_vertical = 0
    cobra_horizontal_vertical = []
    comprimento_da_cobra = 2
    pontuacao = 0

    # Definir os movimentos do jogo
    while sair:
        while fim_de_jogo:
            tela_de_exibicao.fill(verde)
            largura_text = largura_da_tela / 12
            altura_text = altura_da_tela / 2
            if fase != 21:
                exibir_texto("Fim de jogo! Clique no espaço para jogar ou digite F para sair!", azul, 25, largura_text, altura_text)
                exibir_texto("Você fez {0} pontos".format(pontuacao), azul, 25, largura_da_tela / 2.6, altura_da_tela / 3)
            elif fase == 20:
                exibir_texto("PARABÉNS!!! VOCÊ ZEROU O JOGO!", azul, 25, largura_text, altura_text)
            fase = 1
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False 
                    fim_de_jogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        fim_de_jogo = False
                        sair = True
                        # altura_da_tela - 40
                        # altura_da_tela - 480
                        posicao_horizontal = randint(0, (largura_da_tela - tamanho_da_cobra) / 10) * 10
                        posicao_vertical = randint(altura_da_tela - 480, (altura_da_tela - 40 - tamanho_da_cobra - 40) / 10) * 10
                        posicao_horizontal_acerto = randint(0, (largura_da_tela - tamanho_da_cobra) / 10) * 10
                        posicao_vertical_acerto = randint(altura_da_tela - 480, (altura_da_tela - 40 - tamanho_da_cobra - 40) / 10) * 10
                        posicao_horizontal_erro = randint(0, (largura_da_tela - tamanho_da_cobra) / 10) * 10
                        posicao_vertical_erro = randint(altura_da_tela - 480, (altura_da_tela - 40 - tamanho_da_cobra - 40) / 10) * 10
                        velocidade_horizontal = 0
                        velocidade_vertical = 0
                        cobra_horizontal_vertical = []
                        comprimento_da_cobra = 2
                        pontuacao = 0
                        timer = 400
                        operacao = randint(1, 5)
                        definir_operacao(operacao, erro_sorteado)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        sair = False 
                        fim_de_jogo = False
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_horizontal != tamanho_da_cobra:
                    velocidade_horizontal = -tamanho_da_cobra
                    velocidade_vertical = 0
                
                if event.key == pygame.K_a and velocidade_horizontal != tamanho_da_cobra:
                    velocidade_horizontal = -tamanho_da_cobra
                    velocidade_vertical = 0

                if event.key == pygame.K_RIGHT and velocidade_horizontal != - tamanho_da_cobra:
                    velocidade_horizontal = tamanho_da_cobra
                    velocidade_vertical = 0

                if event.key == pygame.K_d and velocidade_horizontal != - tamanho_da_cobra:
                    velocidade_horizontal = tamanho_da_cobra
                    velocidade_vertical = 0
                    
                if event.key == pygame.K_UP and velocidade_vertical != tamanho_da_cobra:
                    velocidade_horizontal = 0
                    velocidade_vertical = -tamanho_da_cobra
                
                if event.key == pygame.K_w and velocidade_vertical != tamanho_da_cobra:
                    velocidade_horizontal = 0
                    velocidade_vertical = -tamanho_da_cobra

                if event.key == pygame.K_DOWN and velocidade_vertical != - tamanho_da_cobra:
                    velocidade_horizontal = 0
                    velocidade_vertical = tamanho_da_cobra
                
                if event.key == pygame.K_s and velocidade_vertical != - tamanho_da_cobra:
                    velocidade_horizontal = 0
                    velocidade_vertical = tamanho_da_cobra

        # Preencher a tela de exibição com a cor verde
        tela_de_exibicao.fill(verde)

        # Criar a lista que auxiliará no crescimento da cobra
        cobra_inicio = []
        cobra_inicio.append(posicao_horizontal)
        cobra_inicio.append(posicao_vertical)
        cobra_horizontal_vertical.append(cobra_inicio)
        criar_cobra(cobra_horizontal_vertical)

        # Fazer com que a cobra cresça
        if len(cobra_horizontal_vertical) > comprimento_da_cobra:
            del cobra_horizontal_vertical[0]

        # Caso a cobra colida com ela mesma
        if any(bloco == cobra_inicio for bloco in cobra_horizontal_vertical[1:-1]):
            fim_de_jogo = True

        pygame.draw.rect(tela_de_exibicao, preto, [0, altura_da_tela - 40, largura_da_tela, 40])
        pygame.draw.rect(tela_de_exibicao, preto, [0, altura_da_tela - 520, largura_da_tela, 40])
        exibir_texto("Pontuação: " + str(pontuacao), branco, 25, 10, altura_da_tela - 30)
        timer -= 1
        exibir_texto("Tempo Restante: " + str(timer), branco, 25, 440, altura_da_tela - 30)
        if timer == 0:
            timer = 400
            fim_de_jogo = True

        def definir_operacao(operacao, erro_sorteado):
            if fase == 1:
                operacao = 1
                # Fase 01: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("5 + 4 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("9", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("8"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("10"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("11"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 2:
                    exibir_texto("5 + 3 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("8", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("8"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("10"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("11"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 3:
                    exibir_texto("6 + 4 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("10", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("8"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("9"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("11"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 4:
                    exibir_texto("9 - 4 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("5", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("8"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("10"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("11"), branco, 25, largura_da_tela - 30, 10)
                
                if operacao == 5:
                    exibir_texto("3 - 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("1", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("3"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("2"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("0"), branco, 25, largura_da_tela - 30, 10)



            if fase == 2:    
                # Fase 01: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("43 + 28 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("71", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("70"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("72"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("73"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 2:
                    exibir_texto("42 + 27 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("69", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("68"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("70"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("71"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 3:
                    exibir_texto("44 + 23 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("67", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("66"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("68"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("69"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 4:
                    exibir_texto("58 - 36 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("22", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("24"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("23"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("21"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("53 - 26 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("27", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("29"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("28"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("26"), branco, 25, largura_da_tela - 30, 10)



            if fase == 3:    
                # Fase 03: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("86 + 47 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("133", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("132"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("134"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("135"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 2:
                    exibir_texto("81 + 43 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("124", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("123"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("125"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("126"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 3:
                    exibir_texto("72 + 59 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("131", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("130"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("132"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("133"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 4:
                    exibir_texto("93 - 37 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("56", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("57"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("55"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("54"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("94 - 34 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("60", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("61"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("59"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("58"), branco, 25, largura_da_tela - 30, 10)


            
            if fase == 4:    
                # Fase 04: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("120 + 108 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("228", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("226"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("227"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("229"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 2:
                    exibir_texto("113 + 118 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("231", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("230"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("232"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("233"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 3:
                    exibir_texto("127 + 94 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("221", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("220"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("222"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("223"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 4:
                    exibir_texto("184 - 55 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("129", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("131"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("130"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("128"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("196 - 69 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("127", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("129"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("128"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("126"), branco, 25, largura_da_tela - 30, 10)


            
            if fase == 5:    
                # Fase 05: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("257 + 139 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("396", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("395"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("397"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("398"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 2:
                    exibir_texto("248 + 142 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("390", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("389"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("391"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("392"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 3:
                    exibir_texto("236 + 155 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("391", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("381"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("392"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("393"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 4:
                    exibir_texto("303 - 67 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("236", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("238"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("237"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("235"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("314 - 79 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("235", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("237"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("236"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("234"), branco, 25, largura_da_tela - 30, 10)



            if fase == 6:    
                # Fase 06: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("2 x 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("4", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("3"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("5"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("6"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 2:
                    exibir_texto("2 x 3 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("6", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("5"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("7"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("8"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 3:
                    exibir_texto("2 x 4 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("8", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("7"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("9"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("10"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 4:
                    exibir_texto("2 : 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("1", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("0"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("2"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("4"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("4 : 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("2", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("3"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("1"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("0"), branco, 25, largura_da_tela - 30, 10)



            if fase == 7:    
                # Fase 07: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("9 x 7 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("63", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("62"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("64"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("65"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 2:
                    exibir_texto("9 x 8 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("72", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("71"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("73"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("74"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 3:
                    exibir_texto("8 x 7 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("56", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("55"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("57"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("58"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 4:
                    exibir_texto("63 : 9 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("7", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("8"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("6"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("5"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("72 : 3 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("24", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("25"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("23"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("22"), branco, 25, largura_da_tela - 30, 10)



            if fase == 8:    
                # Fase 08: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("44 x 39 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("1716", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("1706"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("1726"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("1736"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 2:
                    exibir_texto("43 x 38 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("1634", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("1624"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("1644"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("1654"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 3:
                    exibir_texto("42 x 37 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("1554", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("1544"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("1564"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("1574"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 4:
                    exibir_texto("936 : 8 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("117", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("127"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("107"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("97"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("932 : 4 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("233", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("243"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("223"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("213"), branco, 25, largura_da_tela - 30, 10)



            if fase == 9:
                # Fase 09: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("77 x 65 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("5005", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("4995"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("5015"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("5025"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 2:
                    exibir_texto("76 x 64 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("4864", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("4854"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("4874"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("4884"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 3:
                    exibir_texto("75 x 67 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("5025", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("5015"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("5035"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("5045"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 4:
                    exibir_texto("1540 : 35 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("44", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("45"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("43"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("42"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("1702 : 37 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("46", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("47"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("45"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("44"), branco, 25, largura_da_tela - 30, 10)



            if fase == 10:    
                # Fase 10: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("106 x 96 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("10176", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("10166"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("10186"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("10196"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 2:
                    exibir_texto("107 x 97 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("10379", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("10369"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("10389"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("10399"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 3:
                    exibir_texto("108 x 98 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("10584", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("10574"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("10594"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("10604"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 4:
                    exibir_texto("7654 : 86 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("89", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("91"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("90"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("88"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("8554 : 91 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("94", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("95"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("93"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("92"), branco, 25, largura_da_tela - 30, 10)


            
            if fase == 11:    
                # Fase 11: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("2 ^ 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("4", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("2"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("5"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("6"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 2:
                    exibir_texto("3 ^ 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("9", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("6"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("8"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("10"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 3:
                    exibir_texto("4 ^ 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("16", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("8"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("15"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("17"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 4:
                    exibir_texto("Raiz quadrada de 4 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("2", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("3"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("1"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("0"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("Raiz quadrada de 9 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("3", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("4"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("2"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("1"), branco, 25, largura_da_tela - 30, 10)


                        
            if fase == 12:    
                # Fase 12: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("7 ^ 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("49", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("14"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("48"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("50"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 2:
                    exibir_texto("8 ^ 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("64", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("16"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("63"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("65"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 3:
                    exibir_texto("9 ^ 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("81", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("18"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("80"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("82"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 4:
                    exibir_texto("Raiz quadrada de 81 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("9", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("10"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("8"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("7"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("Raiz quadrada de 64 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("8", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("9"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("7"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("6"), branco, 25, largura_da_tela - 30, 10)



            if fase == 13:    
                # Fase 13: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("7 ^ 3 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("343", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("333"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("353"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("363"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 2:
                    exibir_texto("8 ^ 3 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("512", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("502"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("522"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("532"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 3:
                    exibir_texto("9 ^ 3 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("729", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("719"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("739"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("749"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 4:
                    exibir_texto("Raiz cúbica de 512 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("8", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("9"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("7"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("6"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("Raiz cúbica de 729 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("9", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("8"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("7"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("27"), branco, 25, largura_da_tela - 30, 10)



            if fase == 14:    
                # Fase 14: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("28 ^ 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("784", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("774"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("794"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("804"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 2:
                    exibir_texto("29 ^ 3 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("841", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("831"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("851"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("861"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 3:
                    exibir_texto("31 ^ 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("961", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("951"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("971"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("981"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 4:
                    exibir_texto("Raiz quadrada de 961 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("31", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("32"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("30"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("29"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("Raiz quadrada de 841 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("29", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("30"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("28"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("27"), branco, 25, largura_da_tela - 30, 10)


           
            if fase == 15:    
                # Fase 15: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("7 ^ 4 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("2401", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("2391"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("2411"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("2421"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 2:
                    exibir_texto("8 ^ 4 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("4096", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("4086"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("4106"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("4116"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 3:
                    exibir_texto("9 ^ 4 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("6561", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("6551"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("6571"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("6581"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 4:
                    exibir_texto("Raiz quarta de 1296 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("6", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("8"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("7"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("5"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("Raiz quarta de 625 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("5", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("7"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("6"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("4"), branco, 25, largura_da_tela - 30, 10)



            if fase == 16:    
                # Fase 16: ---------------------------------------------------------------------------------------------- 
                if operacao == 1:
                    exibir_texto("42 ^ 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("1764", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("1754"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("1774"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("1784"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 2:
                    exibir_texto("43 ^ 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("1849", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("1839"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("1859"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("1869"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 3:
                    exibir_texto("44 ^ 2 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("1936", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("1926"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("1946"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("1956"), branco, 25, largura_da_tela - 120, 10)

                if operacao == 4:
                    exibir_texto("Raiz quadrada de 2116 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("46", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("47"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("45"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("44"), branco, 25, largura_da_tela - 30, 10)

                if operacao == 5:
                    exibir_texto("Raiz quadrada de 2209 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("47", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("48"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("46"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("57"), branco, 25, largura_da_tela - 30, 10)



            if fase == 17:    
                # Fase 17: ---------------------------------------------------------------------------------------------- 
                if operacao2 == 1:
                    exibir_texto("5! = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("120", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("119"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("121"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("122"), branco, 25, largura_da_tela - 30, 10)

                if operacao2 == 2:
                    exibir_texto("log3 216 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("6", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("5"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("7"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("8"), branco, 25, largura_da_tela - 30, 10)

                if operacao2 == 3:
                    exibir_texto("6! = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("720", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("710"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("730"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("740"), branco, 25, largura_da_tela - 30, 10)



            if fase == 18:    
                # Fase 18: ---------------------------------------------------------------------------------------------- 
                if operacao2 == 1:
                    exibir_texto("7! = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("5040", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("5030"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("5050"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("5060"), branco, 25, largura_da_tela - 120, 10)

                if operacao2 == 2:
                    exibir_texto("8! = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("40320", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("40310"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("40330"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("40340"), branco, 25, largura_da_tela - 120, 10)

                if operacao2 == 3:
                    exibir_texto("log2 128 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("7", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("6"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("8"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("9"), branco, 25, largura_da_tela - 30, 10)



            if fase == 19:    
                # Fase 19: ---------------------------------------------------------------------------------------------- 
                if operacao2 == 1:
                    exibir_texto("9! = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("362880", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("362870"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("362890"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("362900"), branco, 25, largura_da_tela - 120, 10)

                if operacao2 == 2:
                    exibir_texto("log3 6561 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("8", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("7"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("9"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("10"), branco, 25, largura_da_tela - 30, 10)

                if operacao2 == 3:
                    exibir_texto("10! = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [500, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [500, 15, largura_da_tela - 630, 10])
                    exibir_texto("3628800", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("3628700"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("3628900"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("3629000"), branco, 25, largura_da_tela - 120, 10)



            if fase == 20:    
                # Fase 20: ---------------------------------------------------------------------------------------------- 
                if operacao2 == 1:
                    exibir_texto("439 + 342 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("781", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("771"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("791"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("801"), branco, 25, largura_da_tela - 30, 10)

                if operacao2 == 2:
                    exibir_texto("768 - 374 = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("394", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("384"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("404"), branco, 25, largura_da_tela - 30, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("414"), branco, 25, largura_da_tela - 30, 10)

                if operacao2 == 3:
                    exibir_texto("10! = ?", branco, 25, 280, altura_da_tela - 510)
                    if cores >= 1 and cores <= 5:
                        pygame.draw.rect(tela_de_exibicao, vermelho, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, amarelo, [590, 15, largura_da_tela - 630, 10])
                    else:
                        pygame.draw.rect(tela_de_exibicao, amarelo, [10, altura_da_tela - 500, largura_da_tela - 630, 10])
                        pygame.draw.rect(tela_de_exibicao, vermelho, [590, 15, largura_da_tela - 630, 10])
                    exibir_texto("3628800", branco, 25, 30, altura_da_tela - 505)
                    if erro_sorteado == 1:
                        exibir_texto(str("3628700"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 2:
                        exibir_texto(str("3628900"), branco, 25, largura_da_tela - 120, 10)

                    if erro_sorteado == 3:
                        exibir_texto(str("3629000"), branco, 25, largura_da_tela - 120, 10)

            if fase == 21:
                fim_de_jogo = True

        # Criar as novas posições dos valores certo e errado e somar a pontuação

        if posicao_horizontal == posicao_horizontal_acerto and posicao_vertical == posicao_vertical_acerto:
            posicao_horizontal_acerto = randint(0, (largura_da_tela - tamanho_da_cobra) / 10) * 10
            posicao_vertical_acerto = randint(altura_da_tela - 480, (altura_da_tela - tamanho_da_cobra - 40) / 10) * 10
            posicao_horizontal_erro = randint(0, (largura_da_tela - tamanho_da_cobra) / 10) * 10
            posicao_vertical_erro = randint(altura_da_tela - 480, (altura_da_tela - tamanho_da_cobra - 40) / 10) * 10
            comprimento_da_cobra += 1
            pontuacao += 1
            fase += 1
            timer = 400
            cores = randint(1,10)
            operacao = randint(1, 5)
            definir_operacao(operacao, erro_sorteado)

        definir_operacao(operacao, erro_sorteado)
        criar_acerto_erro(posicao_horizontal_acerto, posicao_vertical_acerto, posicao_horizontal_erro, posicao_vertical_erro, vermelho, amarelo, cores) 
        posicao_horizontal += velocidade_horizontal
        posicao_vertical += velocidade_vertical
        pygame.display.update()
        relogio.tick(13)

        # Definir o limite da borda
        if posicao_horizontal + tamanho_da_cobra > largura_da_tela:
            fim_de_jogo = True
        if posicao_horizontal < 0:
            fim_de_jogo = True
        if posicao_vertical + tamanho_da_cobra > altura_da_tela - 40:
            fim_de_jogo = True
        if posicao_vertical + tamanho_da_cobra < 40:
            fim_de_jogo = True
        if posicao_vertical < 0:
            fim_de_jogo = True
        if posicao_horizontal == posicao_horizontal_erro and posicao_vertical == posicao_vertical_erro:
            fim_de_jogo = True

desenvolver_jogo(operacao, erro_sorteado, fase, timer, cores, operacao2)
pygame.quit()
