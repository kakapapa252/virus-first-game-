import pygame
import random
import math
import time
from pygame import mixer

#initialize pygame
pygame.init()
#set_mode(width.height)
screen = pygame.display.set_mode((800,600))
#title of display
pygame.display.set_caption('VIRUS')
icon = pygame.image.load('leopard.png')	
pygame.display.set_icon(icon)

#background
background = pygame.image.load('batsoup.png')
#music 
mixer.music.load('farm.wav')
mixer.music.play(-1)

#player set
playerimg = pygame.image.load('man.png')
playerx = 355
playery = 500
playery_change = 0 
playerx_change = 0
def player(x,y):
	screen.blit(playerimg, (x,y))






#enemy
enemyimg = []
enemyx = []
enemyy = []
enemyy_change = []
enemyx_change = []
enemy_number  = 5

for i in range(enemy_number):

	enemyimg.append(pygame.image.load('coronavirus.png'))
	enemyx.append(random.randrange(20,720,30))
	enemyy.append(0)
	enemyy_change.append(45)
	enemyx_change.append(3)

def enemy(x,y,i):
	screen.blit(enemyimg[i], (x,y))



#weapon
weaponimg = pygame.image.load('spray.png')
weaponx = 0
weapony = 0
weapony_change = 3
weaponx_change = 0
weapon_state = 'ready'


def weapon(x,y):
	global weapon_state
	weapon_state = 'fire'
	screen.blit(weaponimg, (x+ 16, y+ 10))


def collision(ex,ey,wx,wy):
	d = math.sqrt((ex-wx)**2 + (wy-ey)**2)
	return(d<33)

scorevalue = 0
font = pygame.font.Font('freesansbold.ttf', 32)
fontx = 10
fonty = 10
def showscore(x,y):
	score = font.render('POINTS = '+str(scorevalue),True, (255,0,0))
	screen.blit(score, (x, y))


gameov = pygame.font.Font('freesansbold.ttf', 64)
def game_over(x,y):
	over = gameov.render('YOU GOT CORONA',True, (255,0,0))
	screen.blit(over, (x, y))









game = True
while game:
	screen.fill((173, 216, 230)) #(red green blue)
	screen.blit(background, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game = False


		if event.type == pygame.KEYDOWN:
			'''if event.key == pygame.K_UP:
													playery_change = -1.5
													
												if event.key == pygame.K_DOWN:
													playery_change = 1.5'''

			if event.key == pygame.K_LEFT:
				playerx_change = -2
				
			if event.key == pygame.K_RIGHT:
				playerx_change = 2

			if event.key == pygame.K_SPACE:
				if weapon_state =='ready':
					weaponsound = mixer.Sound('spraysound.wav')
					weaponsound.play()

					weaponx = playerx
					weapony =playery
					weapon(weaponx,weapony)
				
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				playery_change = 0
				playerx_change = 0



	#if playerx <800:
	#	playerx += 0.2
	#else:
	#	playerx = 0
	playerx += playerx_change
	if playerx <= 10:
		playerx = 10
	elif playerx >=730:
		playerx = 730
	#playery += playery_change
	#if playery <= 300:
	#	playery = 300
	#elif playery >=510:
	#	playery = 510

	for i in range(enemy_number):
		enemyx[i] += enemyx_change[i]
		
		
		if enemyx[i] <= 10:
			enemyx_change[i] = 2.5
			enemyy[i] += enemyy_change[i]

		elif enemyx[i] >=730:
			enemyx_change[i] = -2.5
			enemyy[i] += enemyy_change[i]

		


		collide = collision(enemyx[i],enemyy[i],weaponx,weapony)
		if collide:
			hitsound = mixer.Sound('ouch.wav')
			hitsound.play()
			enemyx[i] = random.randrange(10,730,30)
			enemyy[i] = random.randrange(0,30)

			weapon_state = 'ready'
			weapony = playery 
			weaponx = playerx
			scorevalue += 10
		if enemyy[i] >=470:
			for j in range(enemy_number):
				enemyy[j] = 1000
			game_over(100,300)
			break
				


		enemy(enemyx[i],enemyy[i],i)

		




	if weapon_state == 'fire':
		weapon(weaponx,weapony)
		weapony -= weapony_change
	if weapony <= 0:
		weapon_state = 'ready'
		weapony = playery 
		weaponx = playerx
		

		


		
			

	player(playerx,playery)
	showscore(fontx,fonty)
	






	pygame.display.update()




    
    
