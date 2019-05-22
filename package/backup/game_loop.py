import logging
import pygame
import time
import random  
import os
import math
##################################      for Stage1        #####################################
import os
import pygame
from pygame.locals import *
import time
import numpy
import sched
import threading
from package.Class import calculate_gpa
os.chdir('D:/PBC') #package資料夾所在目錄

pygame.init()

width,height = 1280, 960
gameDisplay = pygame.display.set_mode((width,height))
	
pygame.mixer.init()
gpa_init=calculate_gpa([])

def stage1():
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
	hit  = pygame.mixer.Sound("correct.ogg")
	crash = pygame.mixer.Sound("wrong.ogg")
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
								gpa -= 0.3	
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

						#if len(upper & lower) == 1:
								
								#gpa -= 0.3
								
			
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

	gpa_init.add(gpa)					
	life = font.render(str("GPA :")+str("%.1f" %gpa),True,  (255, 255, 255))
	textRect = life.get_rect()
	gameDisplay.blit(pas, (100,400))

	pygame.display.flip()		
	time.sleep(3)
				



	gameDisplay.fill(0)				
	gameDisplay.blit(pas, (500,400))
	pygame.display.flip()




##################################      for Stage2        #####################################
os.chdir('D:/PBC') #package資料夾所在目錄
from package.Class import mainCharacter,obstacle,special_obstacle,figure,text
from package.Functions import set_ColorBlock,set_River,collision,correction,set_to_origin
from package import OP_ED

display_width =  1280 
display_height = 960    
gameDisplay = pygame.display.set_mode((display_width, display_height))   
clock = pygame.time.Clock()
def stage2():
	#Opening_Trailer()
	## play song
	## https://nerdparadise.com/programming/pygame/part3

	riverDisplay = pygame.Surface((1280,960)) #建立一個river圖層
	black = (0, 0, 0)
	white = (255, 255,255)
	red = (255,0,0)
	blue0=(149,220,255)
	blue1=(138,208,255)
	blue2=(128,197,253)
	Colorlist=[blue0,blue1,blue2]

## load wave sound and background music in pygame
	pygame.mixer.music.load("下一站茶山劉.mp3")
	wave=pygame.mixer.Sound("wave.wav")
	pygame.mixer.music.play(-1)
	##uploading image of boats
	boatImg0 = pygame.image.load("boat.png") 
	boatImg1 = pygame.image.load("boat1.png")
	boatImg2 = pygame.image.load("boat2.png")
	boatImgList=[boatImg0,boatImg1,boatImg2]
	
	# uploading other obstacles
	bikeImg = pygame.image.load("bike.png")
	peopleImg = pygame.image.load("people.png")	

	bike2Img = pygame.image.load("bike2.png")
	busImg = pygame.image.load("bus.png")
	catImg = pygame.image.load("cat.png")
	dogImg = pygame.image.load("dog.png")
	fishImg = pygame.image.load("fish.png")
	dinoImg = pygame.image.load("dino.png")
	rainbowcatImg = pygame.image.load("rainbowcat.png")  
	busImg = pygame.transform.scale(busImg, (192*3, 192))


	# uploading other Images
	gpaImg = pygame.image.load("GPA.png")
	hpbarImg = pygame.image.load("HPbar.png")
	endlineImg = pygame.image.load("endline.png")
	backgroundImg = pygame.image.load("background.png")
	backgroundImg = pygame.transform.scale(backgroundImg, (480, 320))
	startoImg = pygame.image.load("starto.png")
	startoImg = pygame.transform.scale(startoImg, (580, 240))

	# defining Objects

	#define background
	background = figure(0,0,480,320)
	background2 = figure(480,0,480,320)
	background3 = figure(960,0,480,320)
	background4 = figure(1440,0,480,320)
	# main character objects
	boat = mainCharacter(display_width*0.1 , display_height*0.75 , 96 , 96 )  #set status of object

	# obstacle objects
	# special_obstacle (self,x,y,width,height,movespeed_x,movespeed_y,damage):
	## setting initial velocity for x and y
	bike2 = special_obstacle(2500,random.randrange(display_height*320/960, display_height*1-96),96,96,-10,0,-0.1) # speed: -10
	people = special_obstacle(2000,random.randrange(display_height*320/960,display_height*1-96),96,96,-7,0,-0.4) # speed: -7
	bike = special_obstacle(1280,random.randrange(display_height*320/960,display_height*1-96),96,96,-14,0,-0.1)	
	bus = special_obstacle(7000,random.randrange(display_height*320/960,display_height*1-96),192*3,192,-20,0,-0.1)# 等等要設成頁面寬	
	cat = special_obstacle(3000,random.randrange(display_height*320/960,display_height*1-96),96,96,-14,0,-0.01)
	dog = special_obstacle(4000,random.randrange(display_height*320/960,display_height*1-96),96,96,-14,0,-0.01)
	fish = special_obstacle(5000,random.randrange(display_height*320/960,display_height*1-96),96,96,-10,random.choice([-25,25]),-0.05)# 往左移10，往上移10，等等可以設random
	dino = special_obstacle(6000,random.randrange(display_height*320/960,display_height*1-96),96,96,-14,random.choice([-20,20]),-0.2)
	rainbowcat = special_obstacle(30000,random.randrange(display_height*320/960,display_height*1-144),144,144,(-1280/10),0,0)
	# rainbow_cat 144*144


	# figure / text objects	
	gpa_icon=figure(30,50,96,96)
	GPA=4.3
	now_gpa=text(str(GPA),60,black,gpa_icon.width+96,gpa_icon.height) 	
	## create ending object
	ending_message=text("You have failed your semester!",80,red,display_width*(1/2),display_height*(2/3))
	
	## create clock now_time on right upper corner.
	now_time=text(str(0.0),60,black,display_width,0)


	## create ending object of game 
	endline=obstacle(display_width,display_height*(1/3),100,display_height*2/3,-4) # width 暫設50 px 

	#obstacle list	
	obstaclelist=[bike,bike2,people,bus,cat,dog,fish,dino,rainbowcat]   


	starto=figure(350,450,192,96)

	x_change = 0 #set constent
	y_change = 0	
	# dodged=0  ## dodged ; congratulating on dodge??	
	boatImgNum=0	#控制 boat gif fps
	frame=0 #初始幀數


	# for collision ; 預設flash 的狀態是false
	flash=False
	collision_time = 0
	for frame in range(6):
		background.set(backgroundImg)
		background2.set(backgroundImg)
		background3.set(backgroundImg)
		background4.set(backgroundImg)
		set_River(riverDisplay,20,20,Colorlist)
		gameDisplay.blit(riverDisplay, (0,320))
		boat.set(boatImg0)
		if frame % 2 == 0:
			starto.set(startoImg)
		pygame.display.update()	
		time.sleep(0.2)
	
### initial_time
	time_running=0
### game exit while loop
	gameExit = False
	
	while not gameExit:
		
		frame+=1 #每跑一次while迴圈幀數+1
		###########event handling loop###########
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			

			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be pressed ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:#pressing left arrow will decrease x-axis coordinate
					x_change = -15
					wave.play()
					
				if event.key == pygame.K_RIGHT:#pressing right arrow will increase x-axis coordinate
					x_change = 15
					wave.play()
					
				if event.key == pygame.K_UP:#pressing UP arrow will decrease Y-axis coordinate
					y_change = -15
					wave.play()

				if event.key == pygame.K_DOWN:#pressing Down arrow will increase x-axis coordinate
					y_change = 15
					wave.play()
					
				if event.key == pygame.K_t:#pressing Down arrow will increase x-axis coordinate
					gameExit = True
					
			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0

		
		boat.x += x_change
		boat.y += y_change


		
		gameDisplay.fill(white)
		
		background.set(backgroundImg)
		background.x-=5
		if background.x < -480:
			background.x =1280
		background2.set(backgroundImg)
		background2.x-=5
		if background2.x < -480:
			background2.x =1280
		background3.set(backgroundImg)
		background3.x-=5
		if background3.x < -480:
			background3.x =1280
		background4.set(backgroundImg)
		background4.x-=5
		if background4.x < -480:
			background4.x =1280
			
		if frame % 20 == 1:				#將river set在 riverDisplay圖層上(每10幀改變一次riverDisplay樣貌)
			set_River(riverDisplay,20,20,Colorlist)	
		gameDisplay.blit(riverDisplay, (0,320)) #再將riverDisplay放在gameDisplay圖層
		
		'''
		#####################將boatImg 組成gif 並設定幾次畫面(frame)更新會換下一張###################
		if boatImgNum!=2:                                  
			set_MainCharacter(boat,boatImgList[boatImgNum])
			if frame % 10 == 0:     #每10幀數換下一張圖片
				boatImgNum += 1

		elif boatImgNum==2:
			set_MainCharacter(boat,boatImgList[boatImgNum])
			if frame % 10 == 0:
				boatImgNum = 0
		'''
		

		## setting obstacles moving speed and directions between each flip
		bike.set(bikeImg)
		bike.x += bike.movespeed
		bike.y += bike.movespeed_y

		people.set(peopleImg)
		people.x += people.movespeed
		people.y += people.movespeed_y

		## setting other objects
		bus.set(busImg)
		bus.x += bus.movespeed
		bus.y += bus.movespeed_y

		cat.set(catImg)		
		cat.x += cat.movespeed
		cat.y += cat.movespeed_y

		dog.set(dogImg)
		dog.x+= dog.movespeed
		dog.y+= dog.movespeed_y

		fish.set(fishImg)
		fish.x+= fish.movespeed
		fish.y+= fish.movespeed_y

		dino.set(dinoImg)
		dino.x += dino.movespeed
		dino.y += dino.movespeed_y

		rainbowcat.set(rainbowcatImg)
		rainbowcat.x += rainbowcat.movespeed
		rainbowcat.y += rainbowcat.movespeed_y



		##  correction of objects to adhere to boundaries ; 
		correction(boat,320/960)  ## 界線是設在1/3，太低可以之後再調



		if fish.y < display_height*320/960:
			fish.y = display_height*320/960
		elif fish.y > display_height:
			fish.y = display_height
		
		if dino.y < display_height*320/960:
			dino.y = display_height*320/960
		elif dino.y > display_height:
			dino.y = display_height

		## altering movespeed_x,movespeed_y for every loop
		## 每經過一輪的blit，speed要不要條整; x,y 都可以調整，現在還沒有調整

		# set_to_origin(objects,change_speed_x,change_speed_y)
		
		set_to_origin(bike,0.02,0)
		set_to_origin(people,0.01,0)
		set_to_origin(bus,0.07,0)
		set_to_origin(cat,0.01,0)
		set_to_origin(dog,0.01,0)
		set_to_origin(fish,0.01,0)
		set_to_origin(dino,0.1,0)


		#根據gpa 每0.5顯示一格hpbar
		# figure(self,x,y,width,height):
		for i in range(0,int(math.floor(float(now_gpa.content)/0.5))):
			hpbar = figure( gpa_icon.x+50*(i+1) , gpa_icon.y , 96 , 96)
			hpbar.set(hpbarImg)
			
		gpa_icon.set(gpaImg)			
		now_gpa.set("None")
		

		## flash setting when collide
		
		if flash == False: 
			if boatImgNum!=2:                                  
				boat.set(boatImgList[boatImgNum])
				if frame % 10 == 0:     #每10幀數換下一張圖片
					boatImgNum += 1

			elif boatImgNum==2:
				boat.set(boatImg0)
				if frame % 7 == 0:
					boatImgNum = 0

		elif flash == True:

			collision_time+=clock.get_time()

			if frame%10 == 0:
				boat.set(random.choice(boatImgList))

		if (collision_time/1000) >=3: ## if 超過3s
			flash = False
		



		## collision method 2 ; setting damage numbers
		for obstacles in obstaclelist:
			#def collision(object1,object2):
			if collision(boat,obstacles)==True:
				'''
				changed_gpa="%-10.2f"%(float(now_gpa.content)+obstacles.damage) ## damage目前是-0.1
				now_gpa.content=str(changed_gpa)
				flash = True
				'''
				if flash==False:
					changed_gpa="%-10.2f"%(float(now_gpa.content)+obstacles.damage) ## damage目前是-0.1
					now_gpa.content=str(changed_gpa)
				elif flash==True:
					continue

				flash = True				


				

		## GPA adjusting

		if float(now_gpa.content)<=0:
			## stop music
			now_gpa.content = 0
			pygame.mixer.music.stop()
			#display message
			ending_message.set("Center")
			pygame.display.update()
			print("printed ending message")
			time.sleep(2)
			OP_ED.Failure_screen2()
			stage2()
			OP_ED.Opening_Trailer3()
			stage3()
			OP_ED.Final_scene()
			pygame.quit()
			logging.info("Quitting.........")
			quit()
			
		if float(now_gpa.content)<2.5:
			now_gpa.color=red
		else:
			now_gpa.color=black

		if float(now_gpa.content) > 4.3:
			now_gpa.content = 4.3
		





		## set time on right upper field
		now_time.set("Right")
		dt=clock.tick(60)/1000
		time_running += dt
		now_time.content="%-10.1f"%(time_running)

		print("Game has run for ",time_running," seconds")
		#print("get_ticks is running for",float(pygame.time.get_ticks()/1000)," seconds")




		if time_running>50:
			now_time.color=red
			print("Clock turned red.......")

		now_time.set("Right")


		# endline=obstacle(display_width,display_height*(1/3),100,display_height*2/3,-4) # width 暫設50 px 
		if (time_running)>=112+30: # >60s 就讓最後一條線進來，撐過一分鐘就成功
			print("endline is appearing................")
			endline.set(endlineImg)
			#endline.x += endline.movespeed
			if endline.x <= display_width/2:
				endline.x = display_width/2
			else:
				endline.x += endline.movespeed

		## if crossed endline
		if collision(boat,endline):
			gpa_init.add(now_gpa.content)
			OP_ED.Ending_Trailer2(now_gpa.content)
			gameExit = True

		## updating pygame display
	
		pygame.display.update()
		clock.tick(60)  ## update 60 frames per second

		
		
		
		
		
		
		
		
		
		
		
		
		
##################################      for Stage3        #####################################
from package.Class import Background,Box,Circle
from package.Functions import isCollision,resetGame

def stage3():
	# 建立畫佈大小.
	BackGround = Background(0,[0,0])
	gameDisplay.fill([255, 255, 255])
	gameDisplay.blit(BackGround.image, BackGround.rect)
	canvas_width = 1280
	canvas_height = 960
	bricks_list = []
	# 時脈.
	clock = pygame.time.Clock()
	game_mode = 0 
	# 設定字型-黑體.
	font = pygame.font.SysFont('simhei', 30)
	# 底板.
	paddle_x = 0
	paddle_y = (canvas_height - 48)
	paddle = Box(pygame, gameDisplay, "paddle", [paddle_x, paddle_y, 100, 24], (0,0,0))
	 
	# 球.
	ball_x = paddle_x
	ball_y = paddle_y
	ball   = Circle(pygame, gameDisplay, "ball", [ball_x, ball_x], 8, (0,0,0))
	dx =  15
	dy = -15
	# 建立磚塊
	brick_num = 120
	brick_x = 70
	brick_y = 130
	brick_w = 0
	brick_h = 0
	for i in range( 0, 120):
		if((i % 12)==0):
			brick_w = 0
			brick_h = brick_h + 30		 
		bricks_list.append (Box(pygame, gameDisplay, "brick_"+str(i), [	brick_w + brick_x, brick_h+ brick_y, 90, 25], [255,255,255]))
		brick_w = brick_w + 95

	# 建立GPABar
	gpaImg = pygame.image.load("GPA.png")
	hpbarImg = pygame.image.load("HPbar.png")
	#初始分數.
	gpa_1 = gpa_init.allgpa[0]
	gpa_2 = gpa_init.allgpa[1]
	gpa_3 = 4.3
	final_grade=''
	# figure / text objects	
	gpa_icon=figure(30,30,96,96)
	new_gpa=text(str(gpa_3),60,(0,0,0),gpa_icon.width+96,gpa_icon.height)
	#-------------------------------------------------------------------------	  
	# 過關畫面.
	#-------------------------------------------------------------------------
	def final_screen():
		bye_1=text("You Saved The Principle",50,(227,23,13),640,200)
		bye_2=text("Your Grade: "+str(final_grade),50,(227,23,13),640,400)
		while True:
			gameDisplay.fill((0,0,0))
			bye_1.set("Center")
			bye_2.set("Center")
			pygame.display.update()
			



	# 初始遊戲.
	resetGame()

	#計時.
	time_keep=600
	#-------------------------------------------------------------------------	  
	# 主迴圈.
	#-------------------------------------------------------------------------

	running = True

	while running:
		
		
		#---------------------------------------------------------------------
		# 判斷輸入.
		#---------------------------------------------------------------------
		for event in pygame.event.get():
			# 離開遊戲.
			if event.type == pygame.QUIT:
				running = False
			# 判斷按下按鈕
			if event.type == pygame.KEYDOWN:
				# 判斷按下ESC按鈕
				if event.key == pygame.K_ESCAPE:
					running = False
					
			# 判斷Mouse.
			if event.type == pygame.MOUSEMOTION:
				paddle_x = pygame.mouse.get_pos()[0] - 50
			if event.type == pygame.MOUSEBUTTONDOWN:
				if(game_mode == 0):
					game_mode = 1
	 
		#---------------------------------------------------------------------	  
		# 清除畫面.
		#canvas.fill(block)
		gameDisplay.fill([255, 255, 255]) ##顯示背景
		gameDisplay.blit(BackGround.image, BackGround.rect) ##顯示背景
		
		# 磚塊
		for bricks in bricks_list:
			# 球碰磚塊.
			if(isCollision( ball.pos[0], ball.pos[1], bricks.rect)):
				if(bricks.visivle):				   
					# 扣除磚塊.
					brick_num = brick_num -1
					##### 初始遊戲. ##### 改成跳出頁面 #####
					if(brick_num <= 0):
						#final_gpa=float(gpa_1)+float(gpa_2)+float(gpa_3)
						gpa_init.add(gpa_3)
						print("This is stage3 gpa")
						final_gpa=float(gpa_3)

						print("GPA-1")
						print(float(gpa_1))
						print("GPA-2")
						print(float(gpa_2))
					
						#print(final_gpa)

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
						final_screen()
						
						
						
					# 球反彈.
					dy = -dy; 
				# 關閉磚塊.
				bricks.visivle = False
	 
			# 更新磚塊.		   
			bricks.update()
				
		
		#顯示磚塊數量.
		now_brick=text("You Still Have "+str(brick_num)+" bricks",30,(0,0,0),850,20)
		now_brick.set("None")
		# 秀板子.
		paddle.rect[0] = paddle_x
		paddle.update()
	 
		# 碰撞判斷-球碰板子.
		if(isCollision( ball.pos[0], ball.pos[1], paddle.rect)):		
			# 球反彈.
			dy = -dy;		  
				
		# 球.
		# 0:等待開球
		if(game_mode == 0):
			ball.pos[0] = ball_x = paddle.rect[0] + ( (paddle.rect[2] - ball.radius) >> 1 )
			ball.pos[1] = ball_y = paddle.rect[1] - ball.radius		   
		# 1:遊戲進行中
		elif(game_mode == 1):
			ball_x += dx
			ball_y += dy
			#判斷死亡.
			if(ball_y + dy > canvas_height - ball.radius):
				game_mode = 0
			# 右牆或左牆碰撞.
			if(ball_x + dx > canvas_width - ball.radius or ball_x + dx < ball.radius):
				dx = -dx
			# 下牆或上牆碰撞
			if(ball_y + dy > canvas_height - ball.radius or ball_y + dy < ball.radius):		   
				dy = -dy
			ball.pos[0] = ball_x
			ball.pos[1] = ball_y
	 
		# 更新分數.
		if (time_keep>0):
			time_keep += -1
		elif (time_keep==0):
			if gpa_3>0:
				gpa_3 += (-0.1)
				time_keep=500
			else:
				time_keep=500
		
		
		# 更新gpabar
		# 根據gpa 每0.5顯示一格hpbar
		# figure(self,x,y,width,height)
		for i in range(0,int(math.floor(float(new_gpa.content)/0.5))):
			hpbar = figure( gpa_icon.x+50*(i+1) , gpa_icon.y , 96 , 96)
			hpbar.set(hpbarImg)
		gpa_icon.set(gpaImg)
		gpa_icon=figure(30,20,96,96)
		new_gpa.set("None")
		# 更新gpa
		new_gpa=text(str(round(gpa_3,1)),50,(0,0,0),gpa_icon.width+150,gpa_icon.height-15)
		# 更新球.
		ball.update()
		# 更新畫面.
		pygame.display.update()
		clock.tick(10000000)
	
	gpa_init.add(new_gpa)
	# 離開遊戲.
	pygame.quit()
	quit()




























