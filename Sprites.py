import pygame

class Pawn(pygame.sprite.Sprite):
	"""Classe representativa de um peao generico"""
	def __init__(self, img, x, y):
		super(Pawn, self).__init__()

		self.img = img
		self.image = pygame.image.load((""+self.img+".png"))
		self.rect = self.image.get_rect()
		self.trn = 0
		self.x = x
		self.y = y
