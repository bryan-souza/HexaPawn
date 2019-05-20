import pygame
from Display import board_init, board_update, move_pawn, WA1, BC3
from Sprites import Pawn

def main():

	board_init() # Carregar o tabuleiro

	# O tempo (kak)
	clock = pygame.time.Clock()
	FPS = 30
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
				
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == pygame.BUTTON_LEFT:
					move_pawn(WA1) # Mover o peão A1
					move_pawn(BC3) # Mover o peão B3
					board_update() # Atualizar o tabuleiro

		# Atualizar a tela
		pygame.display.flip()

if __name__ == "__main__":
	main()

# Nao permite que esse script seja 
# importado, apenas executado como principal
