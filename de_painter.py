import sys, pygame
import random
import time
from pygame import key
pygame.init()

pygame.display.set_caption("De Painter")

screensize = x, y = 400,400
screen = pygame.display.set_mode(screensize)
screenshot_taken = False

save_trigger = 0
my_color = (255,255,255)

#mouse pos detection
def get_mouse_pos():
	pos = pygame.mouse.get_pos()
	x1 = pos[0]
	y1 = pos[1]
	return (x1,y1)

#checks if you actually wanted to change brush color 
def overlap(self = False):
	x2,y2 = get_mouse_pos()

	global my_color 
	
	if x2>=10 and x2<=30 and y2>=10 and y2<=30 and pygame.mouse.get_pressed()[0]:	
		my_color = (255,0,0)
		return True
		
	if x2>=10 and x2<=30 and y2>=40 and y2<=60 and pygame.mouse.get_pressed()[0]:	
		my_color = (0,255,0)
		return True
		
	if x2>=10 and x2<=30 and y2>=70 and y2<=90 and pygame.mouse.get_pressed()[0]:
		my_color = (0,0,255)
		return True

	if x2>=10 and x2<=30 and y2>=100 and y2<=120 and pygame.mouse.get_pressed()[0]:
		my_color = (255,255,255)
		return True

#clears the workspace
def clean(self = False):
	global clean_trigger
	x2,y2 = get_mouse_pos()
	if x2>=10 and x2<=30 and y2>=370 and y2<=390 and pygame.mouse.get_pressed()[0]:
		return True
#works only once per launch, takes screenshot
def take_scr():
	global screen
	global screenshot_taken
	datetime = time.asctime(time.localtime(time.time()))
	datetime = datetime.replace(" ","_")
	datetime = datetime.replace(":",".")
	savefile = "screenshots/" + datetime + ".png"
	if screenshot_taken == False:
		pygame.image.save(screen,savefile)
	screenshot_taken = True


#too lazy too write pygame.display.flip() which refreshes the screen
def display_update():
	pygame.display.flip()

clock = pygame.time.Clock()

while True:
	clock.tick(2000)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	keys = pygame.key.get_pressed()
	mouse = pygame.mouse.get_pressed()

	overlap()
	clean()

	pygame.draw.rect(screen,(255,0,0),[10,10,20,20])
	pygame.draw.rect(screen,(0,255,0),[10,40,20,20])
	pygame.draw.rect(screen,(0,0,255),[10,70,20,20])
	pygame.draw.rect(screen,(120,0,120),[10,370,20,20])
	pygame.draw.rect(screen,my_color,[10,340,20,20])
	pygame.draw.rect(screen,(255,255,255),[10,100,20,20])
	pygame.draw.line(screen,(255,255,255),(38,0),(38,y),5)


	#Switch between colors
	if mouse[0] and overlap() != True and get_mouse_pos()[0]>40:
		pygame.draw.circle(screen,my_color,(get_mouse_pos()),5,5)

	#Clear the screen
	if mouse[0] and clean():
		pygame.draw.rect(screen,(0,0,0),[40,0,400,400])

	# Take a screenshot
	if keys[pygame.K_TAB]:
		save_trigger += 1

	if keys[pygame.K_s]:
		save_trigger += 1

	if save_trigger == 2:
		take_scr()

	save_trigger = 0


	display_update()
