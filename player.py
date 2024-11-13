from circleshape import CircleShape
from constants import *
import pygame as pygame
from shot import Shot



class Player(CircleShape):

	def __init__(self,x,y, *groups):
		super().__init__(x,y,PLAYER_RADIUS)
		self.rotation = 0
		self.containers = groups
		self.SHOOT_COOLDOWN_TIMER = 0
	# in the player class
	def triangle(self):
	    forward = pygame.Vector2(0, 1).rotate(self.rotation)
	    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
	    a = self.position + forward * self.radius
	    b = self.position - forward * self.radius - right
	    c = self.position - forward * self.radius + right
	    return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen,"white", self.triangle(), width=2)

	def rotate(self, dt):
		self.rotation += (PLAYER_TURN_SPEED * dt)

	def update(self, dt):
		self.SHOOT_COOLDOWN_TIMER -= dt
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
    			self.rotate(dt)
		if keys[pygame.K_a]:
			inverse_dt = dt * -1
			self.rotate(inverse_dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			inverse_dt = dt * -1
			self.move(inverse_dt)
		if keys[pygame.K_SPACE]:
			self.shoot()
	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		if self.SHOOT_COOLDOWN_TIMER > 0:
			pass
		else:
			shot = Shot(self.position.x,self.position.y)
			shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
			self.SHOOT_COOLDOWN_TIMER = 0.3
