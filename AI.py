import pygame
import random
from Display import whiteTable, blackTable, capture_pawn, move_pawn, move_test

def auto_play(): # Jogar automaticamente (brancas)
    took_turn = False # Variavel de controle
    while took_turn == False: # Loop principal
        pawn = random.choice(whiteTable) # Escolher um peao branco aleatorio
        cap = [] # Array de capturas possiveis
        last_x = pawn.x # Ultima posicao x
        last_y = pawn.y # Ultima posicao y
        
        for p in range(len(blackTable)): # Laço p/ identificar capturas possiveis
            if ((blackTable[p].y == (pawn.y - 218)) and ((blackTable[p].x == (pawn.x + 218)) or
                                                        (blackTable[p].x == (pawn.x - 218)))):
                cap.append(blackTable[p]) # Caso possivel, adicionar a cap
                sel = random.choice(cap)
            else:
                sel = None

        if pawn.trn != 0 and sel != None: # Checar variavel de controle (ver Classe Pawn)
            if not (capture_pawn(pawn, sel) == False): # Caso seja possivel capturar...
                capture_pawn(pawn, sel) # MATA ELE
        else:
            move_pawn(pawn) # Mover peao

        if pawn.x == last_x and pawn.y == last_y: # Caso o peao nao tenha sido movido...
            took_turn = False # Reiniciar loop
        else: # Senao...
            pawn.trn += 1 # Alterar variavel de controle em Pawn
            took_turn = True # Parar laço principal

def gen_arrays(): # Gerar sinapses da IA (até pq dá muito trabalho fazer manualmente...)
    for p in range(len(blackTable)):
        blackTable[p].mvs.clear()
        for e in range(len(whiteTable)):
            if (whiteTable[e].y == (blackTable[p].y + 218) and 
               (whiteTable[e].x == (blackTable[p].x + 218) or 
                whiteTable[e].x == (blackTable[p].x - 218))):
                # Testar se existem peoes capturaveis
                blackTable[p].mvs.append(str(blackTable[p].trn) + "C" + blackTable[p].id + whiteTable[e].id)
                # Adicionar á lista de movimentos possiveis do peao

        if not (move_test(blackTable[p]) == False):
            blackTable[p].mvs.append(str(blackTable[p].trn) + "M" + blackTable[p].id)

def make_a_move():
    gen_arrays()
    # Make-a-move (credits: Luska E)
    moves = []
    for x in range(len(blackTable)):
        for y in range(len(blackTable[x].mvs)):
            if blackTable[x].mvs is not None:
                moves.append(blackTable[x].mvs[y])
    print(moves)

    move = random.choice(moves) # Escolher um movimento ao acaso
    moves.clear()
    # "Desencriptar" o movimento -> N° do Turno + Tipo de movimento + ID do Peao
    # turn = move[0] # Detectar o turno em que deve ser adicionado
    tipo = move[1] # Detectar o tipo da acao (M/C)
    if tipo == "M":
        tgt = (move[2] + move[3] + move[4]) # Detectar o alvo da acao
    elif tipo == "C":
        pwn = (move[2] + move[3] + move[4])
        tgt = (move[5] + move[6] + move[7])

    print(blackTable)
    print(whiteTable)

    if tipo == "M": # Movimentar
        for p in range(len(blackTable)):
            if blackTable[p].id == tgt:
                move_pawn(blackTable[p])
                blackTable[p].trn += 1

    elif tipo == "C": # Capturar
        for p in range(len(blackTable)):
            for e in range(len(whiteTable)):
                if blackTable[p].id == pwn:
                    if whiteTable[e].id == tgt:
                        capture_pawn(pwn, tgt)