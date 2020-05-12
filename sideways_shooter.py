import pygame
import sys
from settings import Settings
from texas import Texas 
from star import Star

class SideWaysShooter: 

	def __init__(self): 
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Texas Shoot 'Em")

		self.texas = Texas(self)
		self.stars = pygame.sprite.Group()


	def run_game(self):
		while True: 
			self._check_events()
			self.texas.update_position()
			self.update_stars()
			self._update_screen()

	def update_stars(self): 
		self.stars.update()
		for star in self.stars.copy():
			if star.rect.left >= self.settings.screen_width: 
				self.stars.remove(star)


	def _check_events(self): 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN: 
				self._key_down_events(event)
			if event.type == pygame.KEYUP: 
				self._key_up_events(event)

	def _key_down_events(self, event):
		if event.key == pygame.K_DOWN: 
			self.texas.moving_down = True
		elif event.key == pygame.K_UP:
			self.texas.moving_up = True
		elif event.key == pygame.K_SPACE: 
			self._shoot_star()

	def _shoot_star(self): 
		new_star = Star(self)
		self.stars.add(new_star)

	def _key_up_events(self, event):
		if event.key == pygame.K_DOWN: 
			self.texas.moving_down = False
		elif event.key == pygame.K_UP:
			self.texas.moving_up = False


	def _update_screen(self): 
		self.screen.fill(self.settings.bg_color)
		for star in self.stars.sprites(): 
			star.blitme()
		self.texas.blitme()
		pygame.display.flip()


if __name__ == "__main__": 
	sws = SideWaysShooter()
	sws.run_game()