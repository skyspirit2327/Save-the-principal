

import os
import pygame
from pygame.locals import *
import time
import numpy
import sched
import threading


os.chdir('/Volumes/drive/course/107winter/商管程式設計/final progect/python-final-project/Stage1-music/object') #package資料夾所在目錄

pygame.init()

width,height = 1280, 960
gameDisplay = pygame.display.set_mode((width,height))

pygame.mixer.init()


#load and setting objects and sounds
# 物件圖片
bell  	= pygame.image.load("bell_origin.png")
bell = pygame.transform.scale(bell,(250,250))

bell_m 	= pygame.image.load("bell_miss.png")
bell_g 	= pygame.image.load("bell_good.png")
play	= pygame.image.load("play.png")
#
space 	= pygame.image.load("space.png")
press	= pygame.image.load("press.png")

sky 	= pygame.image.load("sky.png")
background 	= pygame.image.load("fubell.png")

graph0 = pygame.image.load("subtitle/0.png")
graph1 = pygame.image.load("subtitle/1.png")
graph2 = pygame.image.load("subtitle/2.png")
graph3 = pygame.image.load("subtitle/3.png")
graph4 = pygame.image.load("subtitle/4.png")
graph5 = pygame.image.load("subtitle/5.png")
graph6 = pygame.image.load("subtitle/6.png")
graph7 = pygame.image.load("subtitle/7.png")

graph8 = pygame.image.load("subtitle/8.png")
graph9 = pygame.image.load("subtitle/9.png")
graph10 = pygame.image.load("subtitle/10.png")
graph11 = pygame.image.load("subtitle/11.png")
graph12 = pygame.image.load("subtitle/12.png")
graph13 = pygame.image.load("subtitle/13.png")
graph14 = pygame.image.load("subtitle/14.png")

graph15 = pygame.image.load("subtitle/15.png")
graph16 = pygame.image.load("subtitle/16.png")
graph17 = pygame.image.load("subtitle/17.png")
graph18 = pygame.image.load("subtitle/18.png")
graph19 = pygame.image.load("subtitle/19.png")
graph20 = pygame.image.load("subtitle/20.png")
graph21 = pygame.image.load("subtitle/21.png")

Graph = [graph1, graph2, graph3, graph4, graph5, graph6, graph7,
		 graph8, graph9, graph10, graph11, graph12, graph13, graph14,
		 graph15, graph16, graph17, graph18, graph19, graph20, graph21
		]
		
for i in range(len(Graph)):
	Graph[i] = pygame.transform.scale(Graph[i],(400,60))


#調整大小
#fail = pygame.transform.scale(fail,(100,100))

bell_m = pygame.transform.scale(bell_m,(250,250))
bell_g = pygame.transform.scale(bell_g,(250,250))

play = pygame.transform.scale(play,(500,500))
space = pygame.transform.scale(space,(400,50))
press = pygame.transform.scale(press,(400,50))

graph0 = pygame.transform.scale(graph0,(400,150))

#gpa
gpapic = pygame.image.load("GPA.png")
hpbar = pygame.image.load("HPbar_2.png")

#加聲音
hit  = pygame.mixer.Sound("correct.wav")
crash = pygame.mixer.Sound("wrong.wav")
song = pygame.mixer.music.load("ntu.mp3")
def gameDisplay_refresh(num):
	gameDisplay.fill(0)
	gameDisplay.blit(sky, (0,0))
	gameDisplay.blit(background, (100,65))
	gameDisplay.blit(button,(540,158))
	gameDisplay.blit(music, (474,530))
	gameDisplay.blit(life, (30,100))
	gameDisplay.blit(hpbar,(20,10))
	gameDisplay.blit(gpapic,(0,0))
	gameDisplay.blit(Graph[num], (474,600))
	pygame.display.flip()

def HINT(num):
	press = pygame.image.load("press.png")
	press = pygame.transform.scale(press,(400,50))
	gameDisplay.fill(0)
	music = press
	gameDisplay.blit(sky, (0,0))
	gameDisplay.blit(background, (100,65))
	gameDisplay.blit(button,(540,158))
	gameDisplay.blit(music, (474,530))
	gameDisplay.blit(life, (30,100))
	gameDisplay.blit(hpbar,(20,10))
	gameDisplay.blit(gpapic,(0,0))
	gameDisplay.blit(Graph[num], (474,600))
	pygame.display.flip()

def HINT2(num):
	gameDisplay.fill(0)
	music = space
	gameDisplay.blit(sky, (0,0))
	gameDisplay.blit(background, (100,65))
	gameDisplay.blit(button,(540,158))
	gameDisplay.blit(music, (474,530))
	gameDisplay.blit(life, (30,100))
	gameDisplay.blit(hpbar,(20,10))
	gameDisplay.blit(gpapic,(0,0))
	gameDisplay.blit(Graph[num], (474,600))
	pygame.display.flip()
	hit.set_volume(50)
	crash.set_volume(50)

# def HINTS(num):
# 	gameDisplay.fill(0)
# 	music = space
# 	gameDisplay.blit(sky, (0,0))
# 	gameDisplay.blit(background, (100,65))
# 	gameDisplay.blit(button,(540,158))
# 	gameDisplay.blit(music, (474,530))
# 	gameDisplay.blit(life, (30,100))
# 	gameDisplay.blit(hpbar,(20,10))
# 	gameDisplay.blit(gpapic,(0,0))
# 	gameDisplay.blit(Graph[num], (474,630))
# 	pygame.display.flip()
# 	hit.set_volume(50)
# 	crash.set_volume(50)

#WASD按鍵狀況記錄
keys = False

#num
num_s = -1
num_e = -1

#要按的秒數
mints = [30.68,33.48,36.23,39.28,42.18,45.08,47.43,49.28,51.08,54.93,57.73,60.18,63.53,66.03,68.43,70.98,74.23,77.33,79.93,82.83,85.43]
mints = numpy.array(mints)

		

fin = False
	
while not(fin):

	#使用者未按任何按鍵的預設狀態
	music 	= play
	gamestart = False
	makechoice=0
	hpbarlen=430
	hpbar = pygame.transform.scale(hpbar,(hpbarlen,50))
	fin = False

	#是否點擊play/stop
	clickbutton = False
	
	#是否在撥放音樂 
	playing = False
	
	#gpa
	gpa = 4.3
	font = pygame.font.Font(None, 50)
	life = font.render(str("GPA :")+str("%.1f" %gpa),True,  (255, 255, 255))
	textRect = life.get_rect()
	
	


	#偵測玩家是否按下play
	while not(gamestart):
	
		button = bell
		gameDisplay.fill(0)		
		gameDisplay.blit(sky, (0,0))
		gameDisplay.blit(background, (100,65))
		gameDisplay.blit(button,(540,158))
		gameDisplay.blit(music, (378,303))
			

		pygame.display.flip()
		
		
			
		for event in pygame.event.get() :
			
			if event.type == pygame.QUIT :
				
				pygame.quit()
				exit()
					
			#偵測是否有按滑鼠，與是否有按在"play"上		
			if event.type == pygame.MOUSEBUTTONDOWN and 378 <= event.pos[0] <= (500+378) and 303 <= event.pos[1] <= (500+303) :
				
				clickbutton = True
				playing = True
				
			if event.type == pygame.K_t:#pressing Down arrow will increase x-axis coordinate
				fin = True
				
		#如果點play，則遊戲要開始了
		if clickbutton and playing:	

			pygame.mixer.music.play()

			music = space
			clickbutton = False
			playing = False
			gamestart = True

			start = time.time()

			break

			
	#hint設定
	if gamestart and gpa >0:
		
		gameDisplay.fill(0)
		gameDisplay.blit(sky, (0,0))
		gameDisplay.blit(background, (100,65))
		gameDisplay.blit(button,(540,158))
		gameDisplay.blit(music, (474,530))
		gameDisplay.blit(life, (30,100))
		gameDisplay.blit(graph0, (474,720))
		gameDisplay.blit(hpbar,(20,10))
		gameDisplay.blit(gpapic,(0,0))
		pygame.display.flip()

		schedule = mints - 0.5

		for i in schedule:
			num_s += 1
			print(num_s)
			T = threading.Timer(i , HINT, args= [num_s])
			T.start()
		
		# schedule_sub = mints + 1
		# for i in schedule_sub:
		# 	S = threading.Timer(i , HINTS, args= [num])
		# 	num += 1
		# 	S.start()

		schedule_end = mints + 1
		
		for i in schedule_end:
			num_e += 1
			print(num_e)
			T_b = threading.Timer(i , HINT2, args = [num_e])
			T_b.start()

	
	while gamestart and gpa > 0:
		#偵測玩家是否按按鍵，按了就記錄按下的time
		for event in pygame.event.get() :
			
		
			if event.type == pygame.QUIT :
				
				pygame.quit()
				exit()
			
			#space按鍵狀況
			if event.type == pygame.KEYDOWN :
			
				if event.key == pygame.K_SPACE :
					keys = True

					time_click = time.time() - start
					
					time_diff = time_click - mints
					upper = set(time_diff[time_diff <= 0.25])
					upper_len = len(upper)
					lower = set(time_diff[time_diff >= -0.15])

					if len(upper & lower) == 1:

						button = bell_g
						
						if gpa < 4.3:
							gpa += 0.1

						life = font.render(str("GPA :")+str("%.1f" %gpa),True,  (255, 255, 255))

						hit.play()
						
						print(len(mints) - len(upper))
						gameDisplay_refresh(len(mints) - len(upper))

						button = bell

						print(len(upper))
						gameDisplay_refresh(len(mints) - len(upper))
					
					else :
						
						time_miss = time.time() - start
						print(time_miss)
						print(time_diff[0])

						if time_miss < mints[0]:
							
							gameDisplay.fill(0)
							gameDisplay.blit(sky, (0,0))
							gameDisplay.blit(background, (100,65))
							gameDisplay.blit(button,(540,158))
							gameDisplay.blit(music, (474,530))
							gameDisplay.blit(life, (30,100))
							gameDisplay.blit(graph0, (474,720))
							gameDisplay.blit(hpbar,(20,10))
							gameDisplay.blit(gpapic,(0,0))
							pygame.display.flip()
						
						else :

							button = bell_m
							crash.play()
							gpa -= 0.1	
							hpbarlen -= 10
							hpbar = pygame.transform.scale(hpbar,(hpbarlen,50))
							life = font.render(str("GPA :")+str("%.1f" %gpa),True,  (255, 255, 255))
						
							if time_miss > time_diff[upper_len-1]+0.25:
								pos = len(mints) - len(upper) - 1
							else :
								pos = len(mints) - len(upper)

							print(len(mints) - len(upper))
							gameDisplay_refresh(pos)
			
							button = bell
											
							print(len(upper))
							gameDisplay_refresh(pos)
								
			if event.type == pygame.KEYUP :
				if event.key == pygame.K_SPACE :
					keys = False

					time_click = time.time() - start

					time_diff = time_click - mints
					upper = set(time_diff[time_diff <= 0.25])
					lower = set(time_diff[time_diff >= -0.15])

					if len(upper & lower) == 1:
							
							gpa -= 0.1
							
		
		if gpa < 0 :
				
			while not(makechoice) :
				for event in pygame.event.get(): 
						
					pygame.mixer.music.stop()
					fail = font.render(str("You have failed the semester, do you want to try again? (y/n)"),True,  (255, 255, 255))
						
					textRect = fail.get_rect()
					gameDisplay.fill(0)
					gameDisplay.blit(fail, (100,400))
					pygame.display.flip()
						
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_n:
							pygame.quit()
							quit()
								
						if event.key == pygame.K_y:
							makechoice = True
							gamestart = False
			
		#如果完成遊戲且gpa大於0
		if gpa > 0 and 89 <=time.time() - start <= 95:		
			fin = True
		
			gamestart = False

			
gameDisplay.fill(0)
pas = font.render(str("You have finish the semester!"),True,  (255, 255, 255))			
textRect = pas.get_rect()
gameDisplay.blit(life, (100,300))

					
life = font.render(str("GPA :")+str("%.1f" %gpa),True,  (255, 255, 255))
textRect = life.get_rect()
gameDisplay.blit(pas, (100,400))

pygame.display.flip()		
time.sleep(10)
			



gameDisplay.fill(0)				
gameDisplay.blit(pas, (500,400))
pygame.display.flip()
