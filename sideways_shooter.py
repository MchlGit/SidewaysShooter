import pygame
import sys
from settings import Settings
from texas import Texas 

class SideWaysShooter: 

	def __init__(self): 
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Texas Shoot 'Em")

		self.texas = Texas(self)


	def run_game(self):
		while True: 
			self._check_events()
			self.texas.update_position()
			self._update_screen()


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

	def _key_up_events(self, event):
		if event.key == pygame.K_DOWN: 
			self.texas.moving_down = False
		elif event.key == pygame.K_UP:
			self.texas.moving_up = False


	def _update_screen(self): 
		self.screen.fill(self.settings.bg_color)
		self.texas.blitme()
		pygame.display.flip()


if __name__ == "__main__": 
	sws = SideWaysShooter()
	sws.run_game()