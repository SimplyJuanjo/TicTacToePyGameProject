import pygame


# Button class
class Button:
	def __init__(self, x, y, image, scale):
		self.width = image.get_width()
		self.height = image.get_height()
		self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		# Draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

	def check(self):
		action = False
		# Get mouse position
		pos = pygame.mouse.get_pos()

		# Check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return action

	def clear(self, scale=0):
		self.image = pygame.transform.scale(self.image, (int(self.width * scale), int(self.height * scale)))
		self.rect.update(self.rect.x * scale, self.rect.y * scale, self.width * scale, self.height * scale)

	def move(self, x, y):
		self.rect.topleft = (x, y)
