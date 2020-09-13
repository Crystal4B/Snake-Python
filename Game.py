from random import randint
from sys import exit

import pygame
import time
import Snake
import Food

# Setup Game Parameters
winWidth = 800
winHeight = 800
boxWidth = winWidth / 30
running = True
player = Snake.Snake(4, boxWidth)
food = Food.Food(randint(1, round(boxWidth)) * boxWidth, randint(1, round(boxWidth)) * boxWidth)

# Initialize window
pygame.init()
screen = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Pygame Snake")

# Start Game Loop
while True:
	# Event Loop
	pygame.event.pump()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN:
			keys = pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]:
				pygame.quit()
				exit()
			if keys[pygame.K_a] or keys[pygame.K_LEFT]:
				player.move('L')
			if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
				player.move('R')
			if keys[pygame.K_w] or keys[pygame.K_UP]:
				player.move('U')
			if keys[pygame.K_s] or keys[pygame.K_DOWN]:
				player.move('D')
			if keys[pygame.K_p]: # DEBUG
				food.x = randint(1, round(boxWidth)) * boxWidth
				food.y = randint(1, round(boxWidth)) * boxWidth
				player.feed()
	
	# Update our snakes position
	player.update()

	# Update Display
	screen.fill((80, 80, 80))
	fruitRec = pygame.Rect(round(food.x), round(food.y), round(boxWidth), round(boxWidth))
	pygame.draw.rect(screen, (255, 0, 0, 1), fruitRec)
	for i in range(player.length-1, 0, -1):
		rectangle = pygame.Rect(round(player.x[i]), round(player.y[i]), round(boxWidth), round(boxWidth))
		pygame.draw.rect(screen, (255, 255, 255, 1), rectangle)
	pygame.display.update()

	# Check for Collision
	# Snake to Snake
	for i in range(1, player.length):
		if round(player.x[0]) == round(player.x[i]) and round(player.y[0]) == round(player.y[i]):
			pygame.quit()
			exit()
	
	# Snake to food
	if round(player.x[0]) == round(food.x) and round(player.y[0]) == round(food.y):
		food.x = randint(1, round(boxWidth)) * boxWidth
		food.y = randint(1, round(boxWidth)) * boxWidth
		player.feed()

	# Snake to Wall
	if round(player.x[0]) < 0 or round(player.x[0]) > winWidth or round(player.y[0]) < 0 or round(player.y[0]) > winHeight:
		pygame.quit()
		exit()

	# Make the Game Wait
	time.sleep (50.0 / 1000.0)