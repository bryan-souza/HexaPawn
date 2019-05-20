import pygame
from Display import WA1, WA2, WA3, BC1, BC2, BC3

class Pawn(pygame.sprite.Sprite):
	"""Classe representativa de um peao generico"""
	def __init__(self, img, x, y):
		super(Pawn, self).__init__()

		self.img = img
		self.image = pygame.image.load((""+self.img+".png"))
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y

	def move(self): # Metodo para mover um peao no tabuleiro
		if self.img == "whitePawn": # Mudar o sentido de movimento
			if not ((BC1.y == (self.y - 218)) or (BC2.y == (self.y - 218)) or (BC3.y == (self.y - 218))):
				self.y -= 218 # Sentido para cima
		else:
			if not ((WA1.y == (self.y + 218)) or (WA2.y == (self.y + 218)) or (WA3.y == (self.y + 218))):
				self.y += 218 # Sentido para baixo
