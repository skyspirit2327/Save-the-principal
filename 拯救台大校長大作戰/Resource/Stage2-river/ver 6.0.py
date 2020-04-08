import logging
import pygame
import time
import random  
import os
import math

#os.chdir('D:/SkySpiriT/NTU/PBC/Project/') #讀取檔案目錄

logging.basicConfig(level=logging.DEBUG)
pygame.init()


display_width =  1280 #960  
display_height = 960  #720   
gameDisplay = pygame.display.set_mode((display_width, display_height))    #Displays(width,length)
riverDisplay = pygame.Surface((1280,960)) #建立一個river圖層


pygame.display.set_caption('拯救台大校長大作戰')
clock = pygame.time.Clock()
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



class mainCharacter():
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
	def set(self,img):
		gameDisplay.blit(img,(self.x,self.y))
		
class obstacle():
	def __init__(self,x,y,width,height,movespeed):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.movespeed=movespeed
	def set(self,img):
		gameDisplay.blit(img,(self.x,self.y))	

class special_obstacle(obstacle):
	def __init__(self,x,y,width,height,movespeed,movespeed_y,damage):
		super().__init__(x,y,width,height,movespeed)
		self.movespeed_y=movespeed_y
		self.damage=damage
	def set(self,img):
		gameDisplay.blit(img,(self.x,self.y))

class figure():
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
	def set(self,img):
		gameDisplay.blit(img,(self.x,self.y))

## this is to display numbers in text, in this case GPA. 
class text():
	def __init__(self,content,size,color,x,y):

		self.content=content
		self.size=size
		self.color=color
		self.x=x
		self.y=y

	def set(self,position):
		now_text=pygame.font.Font("freesansbold.ttf",self.size)
		now_text=now_text.render(self.content,True,self.color)
		now_text_rect=now_text.get_rect()

		if position=="Center": ## 置中
			now_text_rect.center=(self.x-(1/2)*now_text_rect.width,self.y)
		elif position=="Right": ##如果text是在最右邊的話，要把它自己的長度扣掉，完整顯現
			now_text_rect.center=(self.x-now_text_rect.width,self.y)
		elif position=="None":  #不用管，左上角即代表x,y coordinate
			now_text_rect.center=(self.x,self.y)

		gameDisplay.blit(now_text,now_text_rect.center)

	
def set_ColorBlock(layer,color,y,x,width,height): ## set HP bar
	pygame.draw.rect(layer,color, pygame.Rect(y, x, width, height))
	
def set_River(layer,block_width,block_height,colorlist):
	for i in range(0,1281,block_width):
		for j in range(0,641,block_height):
			set_ColorBlock(layer,colorlist[random.randrange(0,len(colorlist))],i,j,block_width,block_height)
	
def collision(object1,object2):
	if object1.x+object1.width > object2.x and object1.x+object1.width < object2.x+object2.width:
		if (object1.y > object2.y and object1.y< object2.y+object2.height) or (object1.y+object1.height > object2.y and object1.y+object1.height < object2.y+object2.height):					
			print("crossed object")
			#print("Deducted",object2.damage," points")
			return True
	else:
		return False

def correction(objects,proportion): ## defines area that the object can operate
	if objects.y < display_height*proportion:
		objects.y = display_height*proportion

	if objects.y+objects.height > display_height:
		objects.y = display_height - objects.height

	if objects.x < 0:
		objects.x = 0

	if objects.x + objects.width > display_width:
		objects.x = display_width - objects.width

def set_to_origin(objects,change_speed_x,change_speed_y): ## defines area that the object can operate
	if objects.x < 0-objects.width:
		objects.y = random.randrange(display_height*320/960, display_height-objects.height)
		objects.x = random.randrange(1280,3200)
		objects.movespeed -= change_speed_x
		objects.movespeed_y -= change_speed_y



def Opening_Trailer():

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
		
def	Failure_screen():
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
			game_loop()
			
		pygame.display.update()

		
		
## Main game loop



def game_loop():
	#Opening_Trailer()
	## play song
	## https://nerdparadise.com/programming/pygame/part3
	print("play music")
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
	background=figure(0,0,480,320)
	background2=figure(480,0,480,320)
	background3=figure(960,0,480,320)
	background4=figure(1440,0,480,320)
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
			Failure_screen()
			game_loop()
			
		if float(now_gpa.content)<2.5:
			now_gpa.color=red
		else:
			now_gpa.color=black

		if float(now_gpa.content) > 4.3:
			now_gpa.content = 4.3
		


		## if crossed endline
		if collision(boat,endline):
			pygame.quit()
			quit()


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
		if (time_running)>=60.0: # >60s 就讓最後一條線進來，撐過一分鐘就成功
			print("endline is appearing................")
			endline.set(endlineImg)
			#endline.x += endline.movespeed
			if endline.x <= display_width/2:
				endline.x = display_width/2
			else:
				endline.x += endline.movespeed



		## updating pygame display

		pygame.display.update()
		clock.tick(60)  ## update 60 frames per second

Opening_Trailer()
game_loop()

pygame.quit()
logging.info("Quitting.........")
quit()