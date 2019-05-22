import os
import logging
import pygame
import time
import random  
import os
import math
os.chdir('D:/PBC')
from package.Class import mainCharacter,obstacle,special_obstacle,figure,text
from package.game_loop import stage2

display_width =  1280 
display_height = 960    
gameDisplay = pygame.display.set_mode((display_width, display_height))    
black = (0, 0, 0)
white = (255, 255,255)
red = (255,0,0)
blue0=(149,220,255)
blue1=(138,208,255)
blue2=(128,197,253)
clock = pygame.time.Clock()
##################################      for First_scene   #####################################
os.chdir('D:/PBC') #package資料夾所在目錄
from package.Class import mainCharacter,obstacle,special_obstacle,figure,text
from package.Functions import set_ColorBlock,set_River,collision,correction,set_to_origin
from package import OP_ED

display_width =  1280 
display_height = 960    
gameDisplay = pygame.display.set_mode((display_width, display_height))   

def First_scene():
	jailImg = pygame.image.load("jail.png")
	principleImg = pygame.image.load("principle.png")
	LOGOImg=pygame.image.load("LOGO.png")

	jailImg = pygame.transform.scale(jailImg, (900, 960))
	principleImg = pygame.transform.scale(principleImg, (900, 960))


	jail=figure(190,0,900,960)
	principle=figure(190,0,900,960)
	LOGO=figure(320,400,672,96)
	## start : use space
	startText= text('press Space to start',20,red,640,780)

	to_stage1=False

	while not to_stage1:

		
		principle.set(principleImg)
		jail.set(jailImg)
		LOGO.set(LOGOImg)
		startText.set("Center")
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					logging.info("space is pressed, will continue to stage 1")
					to_stage1=True

		pygame.display.update()
##################################      for Stage1        #####################################
def Opening_Trailer1():

	stage1 = obstacle(1280,180,192,96,-30)
	bellreal = obstacle (1280+500,265,192,96,-30)
	
	button2 = figure(720,510,192,96)
	OP_background = figure(0,0,1280,960)
	startText= text('press Space to start',20,red,640,780)
	introText=text('Press Space with the beat when the light turn on!',28,black,420,600)
	
	stage1Img = pygame.image.load("stage1.png") 
	stage1Img = pygame.transform.scale(stage1Img, (500, 400))
	bellImg = pygame.image.load("bell.png")
	bellImg = pygame.transform.scale(bellImg, (400, 240))
	button2Img = pygame.image.load("button2.png") 
	button2Img = pygame.transform.scale(button2Img, (450, 215))
	OP_backgroundImg = pygame.image.load("OP_background.png")
	OP_backgroundImg = pygame.transform.scale(OP_backgroundImg, (1280, 960))
	
	ExitOT = False
	Start_Play = True
	logging.info("start loop")
	
	while not ExitOT:	
	
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					Start_Play = False


		
		OP_background.set(OP_backgroundImg)	
		
		stage1.set(stage1Img)
		bellreal.set(bellImg)
		stage1.x += stage1.movespeed
		bellreal.x += bellreal.movespeed

		if stage1.x < 200 and Start_Play == True:

			stage1.movespeed =0
			bellreal.movespeed=0
			button2.set(button2Img)
			startText.set('Center')
			introText.set('Center')
			
		elif Start_Play == False: #如果按下空白建 Start_Play 就會變成 False
			stage1.movespeed = -30
			bellreal.movespeed=-30
			if stage1.x  < -1280:
					ExitOT = True
		
		pygame.display.update()
		
def	Failure_screen1():
	failText = text('Try again? ',20,red,640,380)
	YNText = text('press Y/N',20,red,640,780)
	gameover = False
	gameReset = False
	while True:	
		gameDisplay.fill(black)	
		failText.set('Center')
		YNText.set('Center')
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:
					gameover = True
				if event.key == pygame.K_y:
					gameReset = True
		if gameover == True:
			pygame.quit()
			quit()
		if gameReset == True:
			stage2()
			
		pygame.display.update()

##################################      for Stage2        #####################################

def Opening_Trailer2():

	stage2 = obstacle(1280,180,192,96,-30)
	ZhoushanRiver = obstacle (1280+500,265,192,96,-30)
	
	button = figure(720,510,192,96)
	OP_background = figure(0,0,1280,960)
	startText= text('press Space to start',20,red,640,780)
	introText=text('Dodge all the three treasures!',28,black,420,600)
	
	stage2Img = pygame.image.load("stage2.png") 
	stage2Img = pygame.transform.scale(stage2Img, (500, 400))
	ZhoushanRiverImg = pygame.image.load("ZhoushanRiver.png")
	ZhoushanRiverImg = pygame.transform.scale(ZhoushanRiverImg, (400, 240))
	buttonImg = pygame.image.load("button.png") 
	buttonImg = pygame.transform.scale(buttonImg, (450, 215))
	OP_backgroundImg = pygame.image.load("OP_background.png")
	OP_backgroundImg = pygame.transform.scale(OP_backgroundImg, (1280, 960))
	
	ExitOT = False
	Start_Play = True
	logging.info("start loop")
	
	while not ExitOT:	
	
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					Start_Play = False


		
		OP_background.set(OP_backgroundImg)	
		
		stage2.set(stage2Img)
		ZhoushanRiver.set(ZhoushanRiverImg)
		stage2.x += stage2.movespeed
		ZhoushanRiver.x += ZhoushanRiver.movespeed

		if stage2.x < 200 and Start_Play == True:

			stage2.movespeed =0
			ZhoushanRiver.movespeed=0
			button.set(buttonImg)
			startText.set('Center')
			introText.set('Center')
			
		elif Start_Play == False: #如果按下空白建 Start_Play 就會變成 False
			stage2.movespeed = -30
			ZhoushanRiver.movespeed=-30
			if stage2.x  < -1280:
					ExitOT = True
		
		pygame.display.update()
		
def	Failure_screen2():
	failText = text('Try again? ',20,red,640,380)
	YNText = text('press Y/N',20,red,640,780)
	gameover = False
	gameReset = False
	judge=True
	while judge:	
		gameDisplay.fill(black)	
		failText.set('Center')
		YNText.set('Center')
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:
					gameover = True
				if event.key == pygame.K_y:
					gameReset = True
		if gameover == True:
			pygame.quit()
			quit()
		if gameReset == True:
			stage2()
			judge=False
			
		pygame.display.update()

def	Ending_Trailer2(grade):

	pygame.mixer.music.stop()
	# text
	#def __init__(self,content,size,color,x,y):
	return_gpa = text("Your GPA is "+str(grade),50,red,display_width/2,display_height/2)
	instructions = text("Press C to continue",50,red,display_width/2,display_height/2+300)
	
	to_stage3=False



	while not to_stage3:	
		gameDisplay.fill(black)	
		return_gpa.set('Center')
		instructions.set('Center')

		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			##### keydown elements

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					logging.info("C is pressed, will continue to stage 3")
					to_stage3=True

		pygame.display.update()






##################################      for Stage3        #####################################		
def Opening_Trailer3():

	stage3 = obstacle(1280,180,192,96,-30)
	Proom = obstacle (1280+500,265,192,96,-30)
	
	button = figure(720,510,192,96)
	OP_background = figure(0,0,1280,960)
	startText= text('press Space to start',20,red,640,780)
	introText=text('Break blocks to save principle!',28,black,420,600)
	
	stage3Img = pygame.image.load("stage3.png") 
	stage3Img = pygame.transform.scale(stage3Img, (500, 400))
	ProomImg = pygame.image.load("Proom.png")
	ProomImg = pygame.transform.scale(ProomImg, (400, 240))
	buttonImg = pygame.image.load("button.png") 
	buttonImg = pygame.transform.scale(buttonImg, (450, 215))
	OP_backgroundImg = pygame.image.load("OP_background.png")
	OP_backgroundImg = pygame.transform.scale(OP_backgroundImg, (1280, 960))
	
	ExitOT = False
	Start_Play = True
	logging.info("start loop")
	
	while not ExitOT:	
	
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					Start_Play = False


		
		OP_background.set(OP_backgroundImg)	
		
		stage3.set(stage3Img)
		Proom.set(ProomImg)
		stage3.x += stage3.movespeed
		Proom.x += Proom.movespeed

		if stage3.x < 200 and Start_Play == True:

			stage3.movespeed =0
			Proom.movespeed=0
			button.set(buttonImg)
			startText.set('Center')
			introText.set('Center')
			
		elif Start_Play == False: #如果按下空白建 Start_Play 就會變成 False
			stage3.movespeed = -30
			Proom.movespeed=-30
			if stage3.x  < -1280:
					ExitOT = True
		
		pygame.display.update()
		
def	Failure_screen3():
	failText = text('Try again? ',20,red,640,380)
	YNText = text('press Y/N',20,red,640,780)
	gameover = False
	gameReset = False
	while True:	
		gameDisplay.fill(black)	
		failText.set('Center')
		YNText.set('Center')
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:
					gameover = True
				if event.key == pygame.K_y:
					gameReset = True
		if gameover == True:
			pygame.quit()
			quit()
		if gameReset == True:
			stage2()
			
		pygame.display.update()


def	Final_scene(gpa_init):

	# text
	#def __init__(self,content,size,color,x,y):
	final_gpa = gpa_init.mean()

	if final_gpa==4.3:
		final_grade='A+'
	elif final_gpa>=4.0:
		final_grade='A'
	elif final_gpa>=3.7:
		final_grade='A-'
	elif final_gpa>=3.3:
		final_grade='B+'
	elif final_gpa>=3.0:
		final_grade='B'
	elif final_gpa>=2.7:
		final_grade='B-'
	elif final_gpa>=2.3:
		final_grade='C+'
	elif final_gpa>=2.0:
		final_grade='C'
	else:
		final_grade='c-'

	final_background=figure(0,0,1280,960)
	final_gpa = text("Your final GPA is "+final_grade,50,red,display_width/2,display_height/2+160)
	final_backgroundImg = pygame.image.load("final_background.png")
	final_backgroundImg = pygame.transform.scale(final_backgroundImg,(1280,960))
	
	quitting=False
	while not quitting:	
		gameDisplay.fill(black)
		final_background.set(final_backgroundImg)
		time.sleep(3)
		final_gpa.set('Center')
		
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

		pygame.display.update()


