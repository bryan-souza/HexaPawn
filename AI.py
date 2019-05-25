import pygame
import random
from Display import whiteTable, blackTable, capture_pawn, move_pawn

def auto_play():
    pawn = random.choice(whiteTable)
    trn = 0
    cap = []
    
    for p in range(len(blackTable)):
        if ((blackTable[p].y == (pawn.y - 218)) and ((blackTable[p].x == (pawn.x + 218)) or
                                                     (blackTable[p].x == (pawn.x - 218)))):
            cap.append(blackTable[p])
            print(cap)
    
    if trn != 0:
        pass
    else:
        move_pawn(pawn)