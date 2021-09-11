import pygame, sys, math, random

def draw_play_field():
	for row in range(0,ROWS):
		for col in range(0,COLS):
			left = col*CELL_SIZE
			top = row*CELL_SIZE
			color = play_field[row][col]
			pygame.draw.rect(screen,color, (left,top, CELL_SIZE, CELL_SIZE),0 )
			
	left = current_cell[1] * CELL_SIZE
	top = current_cell[0] * CELL_SIZE
	pygame.draw.rect(screen,ant_color, (left,top, CELL_SIZE, CELL_SIZE),0 )
	
	textsurface = myfont.render(str(num_generations), True, (255, 0, 128))
	screen.blit(textsurface,(0,0))
	
def move_ant():
	global current_cell, current_dir, play_field
	
	row = current_cell [0]
	col = current_cell	[1]
	
	color = play_field[row][col]
	
	#if ant is on a white square, flip color and turn clockwise
	if color == WHITE:
		play_field [row][col] = BLACK
		current_dir = current_dir+1
		if current_dir == 4:
			current_dir = 0
	else: #if ant is on a black square, flip color and turn counter clockwise
		play_field [row][col] = WHITE
		current_dir = current_dir-1
		if current_dir == -1:
			current_dir = 3
	
	if current_dir == UP:
		row = row-1
	elif current_dir == DOWN:
		row = row+1
	elif current_dir == RIGHT:
		col = col+1
	elif current_dir == LEFT:
		col = col-1
	"""		
	if row < 0:
		row = ROWS - 1
	if row > ROWS - 1:
		row = 0	

	if col < 0:
		col = COLS - 1
	if col > COLS - 1:
		col = 0
	"""	
	
	row = row%ROWS
	col = col%COLS
	current_cell = (row,col)		
		
		
		
# Screen size (pixels)
WIDTH = 900	
HEIGHT = 900

BLACK = (0,0,0)
WHITE = (255,255,255)
CELL_SIZE = 5
ROWS = COLS = WIDTH//CELL_SIZE

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

play_field = [[ WHITE for cols in range(COLS)] for rows in range(ROWS)]

current_cell = [ROWS//2, COLS//2]
current_dir = RIGHT
ant_color = (255,0,0)

pygame.init()            

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Langtons Ant')
clock = pygame.time.Clock()
myfont = pygame.font.SysFont(None, 34)

num_generations = 0

while True: # main game loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	move_ant()
	num_generations+=1
	draw_play_field()	
	#clock.tick(120)
	pygame.display.update()
