import pygame
import random as rand
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x,y,radius)
		self.velocity = pygame.Vector2(0,0)

	def draw(self, screen):
		pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius,width=2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			angle = rand.uniform(20,50)
			velocity_1 = self.velocity.rotate(angle)
			velocity_2 = self.velocity.rotate((angle * -1))
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			a1 = Asteroid(self.position.x, self.position.y, new_radius)
			a1.velocity = velocity_1 * 1.2
			a2 = Asteroid(self.position.x, self.position.y, new_radius)
			a2.velocity = velocity_2 * 1.2
