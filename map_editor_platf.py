"""
this platformer map editor keeps on-screen coords of different objects in an np array (i.e. a grid system)
and saves that data in txt file. Every unique object has a different
numerical value (with zero being empty tile).
"""

import numpy as np
import pygame 
from pygame.locals import *

pygame.init()

# window 
scr_width  = 800
scr_height = 600

screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("map editor")


def draw_grid():
	x, y = 0, 0

	# horiz lines
	for i in range((scr_height // tile_size)-1): 
		y += tile_size
		line = pygame.draw.line(screen, (255,255,255), (x, y), (x+scr_width,y))

	# vertical lines
	x, y = 0, 0
	for i in range((scr_width // tile_size)-1): 
		x += tile_size
		line = pygame.draw.line(screen, (255,255,255), (x, y), (x,y+scr_height))


def draw_objs():
	global world_data
	
	for i, row in enumerate(world_data):
		for j, col in enumerate(row):
			if col == 1:
				x = j * tile_size
				y = i * tile_size
				screen.blit(tile_img, (x,y)) 
			elif col == 2:
				x = j * tile_size
				y = i * tile_size
				screen.blit(sun_img, (x,y))
			elif col == 3:
				x = j * tile_size
				y = i * tile_size
				screen.blit(enm_img, (x,y))
			elif col == 4:
				x = j * tile_size
				y = i * tile_size
				screen.blit(lava_img, (x,y))


def set_data(pos):
	global world_data

	# calculate the tile based on mouse position
	x, y = pos
	place_x = x // tile_size
	place_y = y // tile_size
	
	# change value in data array with each click 
	world_data[place_y, place_x] += 1
	if world_data[place_y, place_x] > 4:
		world_data[place_y, place_x] = 0
	#print(world_data)

def save_map():
	# turn map data array into lst, then join into str 
	arrLst = ["\n"]
	for i , row in enumerate(world_data):
		for col in row:
			arrLst.append(str(int(col)))
	#print(arrLst)

	mapStr = "".join(arrLst)
	map_size_tuple = world_data.shape
	map_size = str(map_size_tuple[0]), str(map_size_tuple[1])
	map_size = ",".join(map_size)
	#print(map_size)

	# open txt file and write data into it
	with open("maps.txt", "w") as file:
		file.write(map_size)
		file.write(mapStr)



# object images
sun_img  = pygame.image.load("sun.png") 
bg_img   = pygame.image.load("sky.png")
tile_img = pygame.image.load("dirt.png")
ply_img  = pygame.image.load("guy.png")
enm_img  = pygame.image.load("enemy.png")
lava_img  = pygame.image.load("lava.png")

# map vars
tile_size = 50

# create an array of 0s to hold world data 
world_data = np.zeros((scr_height//tile_size, scr_width//tile_size))



# main loop for graphics
run = True
while run:

	# fill screen color
	screen.fill((0,0,0))

	# EVENTS
	# leave loop, quit program
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		# left mouse click
		if event.type == pygame.MOUSEBUTTONDOWN:
			left_click = pygame.mouse.get_pressed()[0] # returns 3 bools for mouse buttons
			if left_click:
				m_pos = pygame.mouse.get_pos() # get mouse pos as (x,y)			
				
				set_data(m_pos)


	# draw on screen
	draw_grid()

	draw_objs()

	# update display
	pygame.display.update()

save_map()





pygame.quit()
