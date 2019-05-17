import pygame

class Pawn(pygame.sprite.Sprite):
	"""Classe representativa de um peao generico"""
	def __init__(self, image, x, y):
		super(Pawn, self).__init__()

		self.image = pygame.image.load((""+image+".png"))
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y

	def update(self):
		pass
