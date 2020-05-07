import pygame 

class Texas: 
	def __init__(self,sideways_shooter): 
		self.screen = sideways_shooter.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = sideways_shooter.settings

		self.image = pygame.image.load("images/texas.bmp")
		self.rect = self.image.get_rect()
		self.rect.midleft = self.screen_rect.midleft

		self.y = float(self.rect.y)

		self.moving_down = False
		self.moving_up = False

	def blitme(self): 
		self.screen.blit(self.image, self.rect)

	def update_position(self): 
		if self.moving_up and self.rect.top > 0: 
			self.y -= self.settings.texas_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom: 
			self.y += self.settings.texas_speed
		self.rect.y = self.y