import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	def __init__(self, shooter_game): 
		super().__init__()
		self.screen = shooter_game.screen
		self.settings = shooter_game.settings

		self.image = pygame.image.load('images/star.bmp')
		self.rect = self.image.get_rect()

		self.rect.midright = shooter_game.texas.rect.midright

		self.x = float(self.rect.x)

	def update(self): 
		self.x += self.settings.star_speed
		self.rect.x = self.x

	def blitme(self): 
		self.screen.blit(self.image, self.rect)
