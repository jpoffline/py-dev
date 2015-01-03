import pygame, sys, random, math
from pygame.locals import *
pygame.init()
random.seed()

FPS = 100
fpsClock = pygame.time.Clock()

WINDOW_SIZEX = 500
WINDOW_SIZEY = 500

FONT_SIZE = 30

DISPLAYSURF = pygame.display.set_mode((WINDOW_SIZEX, WINDOW_SIZEY), 0, 32)
catIMG = pygame.image.load('cat.png')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


pos_x = int( WINDOW_SIZEX / 2 )
pos_y = int( WINDOW_SIZEY / 2 )
px_0 = pos_x
py_0 = pos_y
pos = [px_0, py_0]
WINDOW_SIZE = [WINDOW_SIZEX, WINDOW_SIZEY]
dx = 1
dy = 1
rad = int( 0.5 * pos_y )
n = 3
r0 = rad
t = 0
dt = 0.1
whichloop = 0
DISP_cat = 2
ndim = 2
motion = 1

if DISP_cat == 1:
	pygame.display.set_caption('Animation: CAT')
elif DISP_cat == 2:
	pygame.display.set_caption('Animation: WORD')
	


while True:
	if whichloop == 0:
		text_col = WHITE
		DISPLAYSURF.fill(BLUE)
	if whichloop == 1:
		text_col = WHITE
		DISPLAYSURF.fill(BLUE)
	if whichloop == 2:
		text_col = WHITE
		whichloop = -1
		DISPLAYSURF.fill(BLUE)

	if motion == 1:	
		for i in range(0, ndim):
			sign = 1
			if random.random() < 0.5:
				sign = - sign
			d = random.randint(1, 10)
			pos[i] = pos[i] + sign * d
			if pos[i] < 0:
			       	pos[i] = 0
			if pos[i] > WINDOW_SIZE[i]:
			      	pos[i] = WINDOW_SIZE[i]
		text_pos = pos		

	
	if motion == 2:		
		rad = r0 * math.sin(n * t) 
		pos_x = rad * math.cos(t) + px_0
		pos_y = rad * math.sin(t) + py_0
		t = t + dt
		if t > 2 * math.pi:
			t = 0.0
		text_pos = (pos_x, pos_y)
	
	myfont = pygame.font.SysFont("monospace", FONT_SIZE)

	# render text
	text_msg = "Hello"  	
	label = myfont.render(text_msg, 1, text_col)
	if DISP_cat == 1:
		DISPLAYSURF.blit(catIMG, text_pos)
	elif DISP_cat == 2:
		DISPLAYSURF.blit(label, text_pos)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	whichloop = whichloop + 1
	pygame.display.update()
	fpsClock.tick(FPS)	
