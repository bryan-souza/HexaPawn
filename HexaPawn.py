import pygame
from Display import WA1, WA2, WA3, BC1, BC2, BC3, board_init, board_update
from Sprites import Pawn
from AI import auto_play

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
					auto_play()

		# Atualizar a tela
		board_update()
		pygame.display.flip()

		# Checar se alguém ganhou
		if WA1.y == 5 or WA2.y == 5 or WA3.y == 5:
			text = "Branco Wins"
			pygame.display.set_caption(text)
			running = False
			
		elif BC1.y == 441 or BC2.y == 441 or BC3.y == 441:
			text = "Preto Wins"
			pygame.display.set_caption(text)
			running = False

if __name__ == "__main__":
	main()

# Nao permite que esse script seja 
# importado, apenas executado como principal
