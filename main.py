# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from circleshape import CircleShape
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
	pygame.init()
	print("Starting asteroids!")
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Asteroid.containers = (asteroids,updatable,drawable)
	AsteroidField.containers = (updatable,)
	Player.containers = (updatable, drawable)

	player = Player(x,y, Player.containers)
	asteroidfield = AsteroidField()

	while True:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        return

		for obj in updatable:
			obj.update(dt)

		for obj in asteroids:
			if player.collisionCheck(obj):
				print("Game over!")
				return

		pygame.Surface.fill(screen, (0,0,0))
		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)
