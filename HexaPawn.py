import pygame
from Display import WA1, WA2, WA3, BC1, BC2, BC3, board_init, board_update, board_reset, move_pawn, capture_pawn, move_test, blackTable, whiteTable
from Sprites import Pawn
from AI import auto_play, make_a_move, moves, gen_arrays, wht_mv, blk_mv

def main():

	board_init() # Carregar o tabuleiro

	# Pontuações
	white_wins = 0
	black_wins = 0

	# O tempo (kak)
	clock = pygame.time.Clock()
	FPS = 1
	playtime = 0.0

	running = True # Variavel de controle

	while running: # Loop Principal
		milliseconds = clock.tick(FPS) # Limitar o FPS
		playtime += milliseconds / 1000.0 # Formatar em segundos o tempo de jogo

		for event in pygame.event.get(): # Tratador de Eventos
			if event.type == pygame.QUIT: # Se um evento do tipo SAIR for detectado...
				running = False # Alterar a variavel de controle p/ False
			
			elif event.type == pygame.KEYDOWN: # Trata eventos ligados ao pressionar de uma tecla
				if event.key == pygame.K_ESCAPE: # Se a tecla ESC for pressionada...
					running = False # Sair do Jogo
			
			elif event.type == pygame.MOUSEMOTION: # Trata movimentos do mouse
				pass
		
		# Parar a execução quando X gerações tiverem passado
		if (white_wins + black_wins == 10):
			print("Brancas: " + str(white_wins))
			print("Pretas: " + str(black_wins))
			running = False
		else:
			if whiteTable == None or wht_mv == False:
				black_wins += 1
				board_reset()
			
			elif blackTable == None or blk_mv == False:
				white_wins += 1
				board_reset()

			else:
				auto_play()
				board_update()
				
				if wht_mv == False or blk_mv == False:
					black_wins += 1
					board_reset()
				
				# Checar se as brancas ganharam
				elif (WA1.y == 5 or WA2.y == 5 or WA3.y == 5) or (blackTable == None):
					white_wins += 1
					board_reset()

				else:
					make_a_move()
					board_update()
				
					# Checar se as pretas ganharam
					if (BC1.y == 441 or BC2.y == 441 or BC3.y == 441) or (whiteTable == None):
						black_wins += 1
						board_reset()

		# Atualizar a tela
		pygame.display.flip()

if __name__ == "__main__":
	main()

# Nao permite que esse script seja 
# importado, apenas executado como principal
