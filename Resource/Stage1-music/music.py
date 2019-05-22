# music
#半拍24/16秒
#先註解掉asd與第二個按鈕功能
#tab讓其他字串在螢幕外
#顏色標示關鍵字(未解)


#按鈕改傅鐘
#背景是鐘架子
#設大笨鳥做為提示

import os
import pygame
from pygame.locals import *
import time



os.chdir('C:\\Users\\user\\Desktop\\NTU\\107-1\\python\\final')

pygame.init()

width,height=1280,960
screen = pygame.display.set_mode((width,height))

	
pygame.mixer.init()


# 物件圖片
blue  	= pygame.image.load("object\\bell.png")
red   	= pygame.image.load("object\\bell_press.png")
green 	= pygame.image.load("object\\bell_miss.png")
play	= pygame.image.load("object\\play.png")
stop 	= pygame.image.load("object\\stop.png")
fail	= pygame.image.load("object\\gameover.png")
pas		= pygame.image.load("object\\pass.png")
sky 	= pygame.image.load("object\\sky.png")
background 	= pygame.image.load("object\\fubell.png")

hint0	= pygame.image.load("object\\blue.png")
hint1	= pygame.image.load("object\\orange.png")

fail = pygame.transform.scale(fail,(100,100))



#加聲音
hit  = pygame.mixer.Sound("sound\\Air_Woosh_Underwater.wav")
crash = pygame.mixer.Sound("sound\\crash.wav")
song = pygame.mixer.music.load("sound\\ntu.wav")


hit.set_volume(100)
crash.set_volume(0.5)

# WASD按鍵狀況記錄
keys = [False,False,False,False]




#使用者未按任何按鍵的預設狀態
music 	= play
gamestart = False
gpa = 4.3
hint = hint0


#樂譜,半拍為單位
score =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
		1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
		1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,
		0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
		1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,
		1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,
		1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,
		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
		1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,
		1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,
		1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,
		1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,
		1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0]
		
# 歌詞
lyric =("臺大的環境　鬱鬱蔥蔥　臺大的氣象　勃勃蓬蓬 "

		"遠望那玉山突出雲表　正象徵我們目標的高崇"

		"近看蜿蜒的淡水　他不捨晝夜地流動"

		"正顯示我們百折不撓的作風　這百折不撓的作風"

		"定使我們　一切事業都成功")




	
while 1 and gpa>0 :

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
	x =480

	
	while not(gamestart):
	
		button 	= blue
		screen.fill(0)
		
		screen.blit(sky, (0,0))
		screen.blit(background, (100,65))
		screen.blit(button,(150,0))
		screen.blit(music, (500,500))
			

		pygame.display.flip()
		
		
			
		for event in pygame.event.get() :
			
			if event.type == pygame.QUIT :
				
				pygame.quit()
				exit()
					
			#偵測是否有按滑鼠，與是否有按在"play"上		
			if event.type == pygame.MOUSEBUTTONDOWN and 500 <= event.pos[0] <= (500+351) and 500 <= event.pos[1] <= (500+153) :
				
				clickbutton = True
				playing = True

				
		#如果點play/stop
		if clickbutton and playing:	

			pygame.mixer.music.play()
			music = stop
			clickbutton = False
			gamestart = True

			

	while gamestart and gpa>0:
	

		for n,i in enumerate(score) :
			
			
			#如果下一拍需要按，hint即變色提示
			hint = hint1 if score[n+1] == 1 else hint0
			

			start = time.time()
			
			screen.fill(0)
			button = blue
			screen.blit(sky, (0,0))
			screen.blit(background, (100,65))
			screen.blit(button,(150,0))
			screen.blit(music, (500,500))
			screen.blit(life, (0,0))
			screen.blit(hint, (50,50))
			
			x -= 40
		
			screen.blit(runninglyr, (x, 700))
			screen.blit(runninglyr, (x + runninglyr.get_width(), 700))
		
			pygame.display.flip()



			for event in pygame.event.get() :
			
				if event.type == pygame.QUIT :
					
					pygame.quit()
					exit()
				
				#wasd按鍵狀況
				if event.type == pygame.KEYDOWN :
				
					if event.key == pygame.K_w :
						keys[0] = True

					
				if event.type == pygame.KEYUP :
					if event.key == pygame.K_w :
						keys[0] = False
				
				if event.type == pygame.MOUSEBUTTONDOWN and 500 <= event.pos[0] <= (500+351) and 500 <= event.pos[1] <= (500+153) :
				
					clickbutton = True
					playing = False

			
			if clickbutton and not(playing) :
			
				pygame.mixer.music.stop()		
				music = play
				clickbutton = False
				gamestart = False
				
				break
			
			#如果按下w	
			if keys[0] :		
					
				button=red
				
				if i == 1 :
					hit.play()
					gpa += 0.1
					
				else :
					crash.play()
					gpa -= 0.1		
				
			else :
				
				if i == 1 :
					button=green
					gpa -= 0.1
	
	
			life = font.render(str("GPA :")+str("%.1f" %gpa),True,  (255, 255, 255))
			
			
			if gpa < 0 :
								
				break
			
			screen.fill(0)
			screen.blit(sky, (0,0))
			screen.blit(background, (100,65))
			screen.blit(button,(150,0))
			screen.blit(music, (500,500))
			screen.blit(life, (0,0))			
			screen.blit(runninglyr, (x, 700))
			screen.blit(runninglyr, (x + runninglyr.get_width(), 700))
			screen.blit(hint, (50,50))

			pygame.display.flip()
			
			
			

			if time.time() - start < 0.74 :
				time.sleep(0.74-(time.time()-start))
				print("%.1f" %gpa)

				pygame.display.flip()


if gpa < 0 :
	
	screen.fill(0)				
	screen.blit(fail, (500,400))
	pygame.display.flip()

else :
	
	screen.fill(0)				
	screen.blit(pas, (500,400))
	pygame.display.flip()
