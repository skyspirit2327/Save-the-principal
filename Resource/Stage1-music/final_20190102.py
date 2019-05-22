

import os
import pygame
from pygame.locals import *
import time



os.chdir('C:\\Users\\family\\Documents\\GitHub\\python-final-project\\Stage1-music')

pygame.init()

width,height = 1280, 960
screen = pygame.display.set_mode((width,height))

	
pygame.mixer.init()


# 物件圖片
bell  	= pygame.image.load("object\\bell.png")
bell = pygame.transform.scale(bell,(250,250))

bell_m 	= pygame.image.load("object\\bell_miss.png")
bell_g 	= pygame.image.load("object\\bell_good.png")
play	= pygame.image.load("object\\play.png")
#
space 	= pygame.image.load("object\\space.png")
press	= pygame.image.load("object\\press.png")

fail	= pygame.image.load("object\\gameover.png")

pas	    = pygame.image.load("object\\pass.png")

sky 	= pygame.image.load("object\\sky.png")
background 	= pygame.image.load("object\\fubell.png")

#提示鍵
#hint0	= pygame.image.load("object\\blue.png")
#要按了的提示鍵變色
#hint1	= pygame.image.load("object\\orange.png")

#調整大小
fail = pygame.transform.scale(fail,(100,100))

bell_m = pygame.transform.scale(bell_m,(250,250))
bell_g = pygame.transform.scale(bell_g,(250,250))

play = pygame.transform.scale(play,(500,500))
space = pygame.transform.scale(space,(400,50))
press = pygame.transform.scale(press,(400,50))

#加聲音
hit  = pygame.mixer.Sound("sound\\correct.wav")
crash = pygame.mixer.Sound("sound\\wrong.wav")
song = pygame.mixer.music.load("sound\\ntu.mp3")


hit.set_volume(50)
crash.set_volume(50)

#WASD按鍵狀況記錄
keys = False


#使用者未按任何按鍵的預設狀態
music 	= play
gamestart = False
gpa = 4.3
#hint = hint0


		
#要按的秒數
mints = [30.68,31.38,31.88,31.98,32.83,33.48,34.18,34.83,35.48,
		 36.23,36.93,37.43,37.68,38.43,39.28,39.98,40.58,41.28,
		 42.18,42.78,43.28,43.53,44.18,45.08,45.28,45.53,46.13,
		 47.43,47.73,48.08,48.43,48.83,49.28,49.88,51.08,51.43,51.98,
		 54.93,55.53,56.33,56.98,57.38,57.73,58.43,
		 60.18,60.78,61.63,62.08,62.83,63.13,63.53,64.28,
		 66.03,66.23,66.53,66.98,67.73,68.43,68.83,69.18,69.93,70.98,71.38,72.13,
		 74.23,74.93,75.23,75.63,76.33,77.33,77.73,78.48,
		 79.93,80.23,80.68,81.38,82.83,83.13,83.53,84.23,85.43,85.83,86.53]



		
# 歌詞
lyric =("　　　　　　　　　　　　　　　　　　　　　"

		"　　　　　　　　　　　　　　　　　　　　　"
		
		"臺大的環境　鬱鬱蔥蔥　臺大的氣象　勃勃蓬蓬 "

		"遠望那玉山突出雲表　正象徵我們目標的高崇 "

		"近看蜿蜒的淡水　他不捨晝夜地流動 "

		"正顯示我們百折不撓的作風　這百折不撓的作風 "

		"定使我們　一切事業都成功")

def GoodOrMiss(start, timeclick, thetime, gpa):
	#偵測是否按對
	duration = timeclick - start
	for i in mints:
		if thetime == i and duration-0.15 < thetime < duration + 0.25:
			screen.fill(0)
				
			music = space
			button = bell_g
			gpa += 0.1
			hit.play()
						
			screen.blit(sky, (0,0))
			screen.blit(background, (100,65))
			screen.blit(button,(540,158))
			screen.blit(music, (474,530))
			life = font.render(str("GPA :")+str("%.1f" %gpa),True,  (255, 255, 255))
				
		else:
			screen.fill(0)
				
			music = space
			button = bell_g
			crash.play()
			gpa -= 0.1	
						
			screen.blit(sky, (0,0))
			screen.blit(background, (100,65))
			screen.blit(button,(540,158))
			screen.blit(music, (474,530))
			life = font.render(str("GPA :")+str("%.1f" %gpa),True,  (255, 255, 255))
	
		screen.fill(0)
				
		music = space
		button = bell
						
		screen.blit(sky, (0,0))
		screen.blit(background, (100,65))
		screen.blit(button,(540,158))
		screen.blit(music, (474,530))	
		

	
while 1 :

	#是否點擊play/stop
	clickbutton = False
	
	#是否在撥放音樂 
	playing = False
	
	#gpa
	gpa = 4.3
	font = pygame.font.Font(None, 50)
	life = font.render(str("GPA :")+str("%.1f" %gpa),True,  (255, 255, 255))
	textRect = life.get_rect()
	
	
	#指定中文字體
	fontc = pygame.font.Font("C:\\Windows\\Fonts\\msjhl.ttc",50)
	runninglyr = fontc.render(lyric, True, (0, 0, 0))
	#字開始出現的位置
	x = 480

	#偵測玩家是否按下play
	while not(gamestart):
	
		button = bell
		screen.fill(0)		
		screen.blit(sky, (0,0))
		screen.blit(background, (100,65))
		screen.blit(button,(540,158))
		screen.blit(music, (378,303))
			

		pygame.display.flip()
		
		
			
		for event in pygame.event.get() :
			
			if event.type == pygame.QUIT :
				
				pygame.quit()
				exit()
					
			#偵測是否有按滑鼠，與是否有按在"play"上		
			if event.type == pygame.MOUSEBUTTONDOWN and 378 <= event.pos[0] <= (500+378) and 303 <= event.pos[1] <= (500+303) :
				
				clickbutton = True
				playing = True

				
		#如果點play，則遊戲要開始了
		if clickbutton and playing:	

			pygame.mixer.music.play()
			music = space
			clickbutton = False
			playing = False
			gamestart = True

			

	while gamestart and gpa > 0:
		
		start = 0
			
		#song.play()
		
		music = space
							
		screen.blit(sky, (0,0))
		screen.blit(background, (100,65))
		screen.blit(button,(540,158))
		screen.blit(music, (474,530))
		screen.blit(life, (0,0))
		
		#遊戲開始字幕就開始跑
		x -= 40
		
		screen.blit(runninglyr, (x, 300))
		screen.blit(runninglyr, (x + runninglyr.get_width(), 300))
		
		pygame.display.flip()
		
		while True:
			theTime = pygame.time.get_ticks() / 1000
			print(theTime)

		
		#遊戲提示	
		#i:元素  n:index
		for i in mints:
			#遊戲當下的時間
					
			if  abs(theTime + 0.15 - float(i+16.836)) < 0.001:
				#hint = hint1  
				#screen.blit(hint, (50,50))
				
				screen.fill(0)
				
				music = press
										
				screen.blit(sky, (0,0))
				screen.blit(background, (100,65))
				screen.blit(button,(540,158))
				screen.blit(music, (474,530))
				
				screen.blit(life, (0,0))
				
				
				music = space
			
			else:
				music = space
		
			music = space
			screen.fill(0)
			screen.blit(sky, (0,0))
			screen.blit(background, (100,65))
			screen.blit(button,(540,158))
			screen.blit(music, (474,530))
			screen.blit(life, (0,0))
			
			
			"""
			
			if clickbutton and not(playing) :
			
				pygame.mixer.music.stop()		
				music = play
				clickbutton = False
				gamestart = False
				
				break
			"""
		
		
		#偵測玩家是否按按鍵，按了就記錄按下的time
		for event in pygame.event.get() :
			time_click = 0
			
			if event.type == pygame.QUIT :
					
				pygame.quit()
				exit()
				
			#space按鍵狀況
			if event.type == pygame.KEYDOWN :
				
				if event.key == pygame.K_SPACE :
					keys = True
					time_click = pygame.time.get_ticks()
					GoodOrMiss(start,time_click,theTime, gpa)
									
			if event.type == pygame.KEYUP :
				if event.key == pygame.K_SPACE :
					keys = False
					
			"""	
			if event.type == pygame.MOUSEBUTTONDOWN and 500 <= event.pos[0] <= (500+351) and 500 <= event.pos[1] <= (500+153) :
				
				clickbutton = True
				playing = False
			"""
			
			
			if gpa < 0 :
								
				break
			
			screen.fill(0)
			screen.blit(sky, (0,0))
			screen.blit(background, (100,65))
			screen.blit(button,(540,158))
			screen.blit(music, (474,530))
			screen.blit(life, (0,0))			
			screen.blit(runninglyr, (x, 700))
			screen.blit(runninglyr, (x + runninglyr.get_width(), 700))
			#screen.blit(hint, (50,50))

			pygame.display.flip()
			
			
			

		#print("%.1f" %gpa)
		pygame.display.flip()

		


if gpa < 0 :
	
	screen.fill(0)				
	screen.blit(fail, (500,400))
	pygame.display.flip()

else :
	
	screen.fill(0)				
	screen.blit(pas, (500,400))
	pygame.display.flip()
