import pygame, os
from random import randint
from Sprites import Pawn

def main():
	pygame.init()

	logo = pygame.image.load("logo32x32.png") # Associar a imagem a variavel logo
	pygame.display.set_icon(logo) # Carregar a imagem
	pygame.display.set_caption("HexaPawn") # Mudar o titulo do programa

	screen = pygame.display.set_mode((660, 660)) # Criar tela de 660x660
	background = pygame.Surface(screen.get_size()) # Criar um plano e nomear como BKG
	background.fill((randint(0, 255), randint(0, 255), randint(0, 255))) # Preencher o fundo com uma cor aleatoria
	background = background.convert() # Converter o objeto para otimizar o jogo

	# TABULEIRO
	A1 = None
	A2 = None
	A3 = None
	B1 = None
	B2 = None
	B3 = None
	C1 = None
	C2 = None
	C3 = None

	tab_array = [A1, A2, A3,
		   		 B1, B2, B3,
		  		 C1, C2, C3]

	tab_pos = [(5, 441)	 , (5, 223)	 , (5, 5),
			   (223, 441), (223, 223), (223, 5),
			   (441, 441), (441, 223), (441, 5)]

	# Criar os "objetos" representando o tabuleiro
	for x in range(len(tab_array)):
		tab_array[x] = pygame.Surface((213, 213))
		if (x % 2 == 0):
			tab_array[x].fill((0,0,0))
		else:
			tab_array[x].fill((255,255,255))

		tab_array[x] = tab_array[x].convert()
		background.blit(tab_array[x], (tab_pos[x]))

	WA1 = Pawn("whitePawn", 5, 441) # Peao Branco em A1
	#WA2 = Pawn("whitePawn") # Peao Branco em A2
	#WA3 = Pawn("whitePawn") # Peao Branco em A3
	#BC1 = Pawn("blackPawn") # Peao Preto em C1
	#BC2 = Pawn("blackPawn") # Peao Preto em C2
	#BC3 = Pawn("blackPawn") # Peao Preto em C3

	background.blit(WA1.image, (WA1.x, WA1.y)) # Mostrar peao A1 na tela
	#background.blit(WA2.image, (223, 441)) # Mostrar peao A1 na tela
	#background.blit(WA3.image, (441, 441)) # Mostrar peao A1 na tela
	#background.blit(BC1.image, (5, 5)) # Mostrar peao A1 na tela
	#background.blit(BC2.image, (223, 5)) # Mostrar peao A1 na tela
	#background.blit(BC3.image, (441, 5)) # Mostrar peao A1 na tela

	screen.blit(background, (0,0)) # Imprimir na tela

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
				# text = "Pos (%d, %d)" % event.pos # Mostra a posicao do mouse (x, y)
				pass
				
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == pygame.BUTTON_LEFT:
					print(WA1.rect.__str__())
					WA1.rect.move((223, 441))

		# Atualizar a tela
		pygame.display.flip()

if __name__ == "__main__":
	main()

# Nao permite que esse script seja 
# importado, apenas executado como principal
