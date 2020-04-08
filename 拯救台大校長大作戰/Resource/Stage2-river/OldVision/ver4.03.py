## 12/26
# 1. 碰撞bug修正，如果在上面會扣分，撞到會扣分，obstacle在下面不會扣分

# 2. 碰到obstacle，boat 會閃，且如果再撞到另一個東西，不會扣分
# 3. 最後, ending message的位置要調整  ; done.
# 4. 調整人物和障礙物大小與數量 並設計關卡結束條件(稱幾秒會結束)

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


class mainCharacter():
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height

		
class obstacle():
	def __init__(self,x,y,width,height,movespeed):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.movespeed=movespeed

class figure():
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height


## this is to display numbers in text, in this case GPA. 
class text():
	def __init__(self,content,size,color,x,y):

		self.content=content
		self.size=size
		self.color=color
		self.x=x
		self.y=y
		


#######  text
## dodged 想要之後再隨機出現在螢幕上恭喜他dodged了幾人

'''
def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("dodged" + str(count), True, black)
	gameDisplay.blit(text,(0,0))
'''

def set_MainCharacter(character,img):
	gameDisplay.blit(img,(character.x,character.y))
	
def set_Obstacle(obstacle,img):
	gameDisplay.blit(img,(obstacle.x,obstacle.y))
	
def set_Figure(figure,img):
	gameDisplay.blit(img,(figure.x,figure.y))

## setting text on screen
def set_Text(text,position):
	now_text=pygame.font.Font("freesansbold.ttf",text.size)
	now_text=now_text.render(text.content,True,text.color)
	now_text_rect=now_text.get_rect()

	if position=="Center": ## 置中
		now_text_rect.center=(text.x-(1/2)*now_text_rect.width,text.y)
	elif position=="Right": ##如果text是在最右邊的話，要把它自己的長度扣掉，完整顯現
		now_text_rect.center=(text.x-now_text_rect.width,text.y)
	elif position=="None":  #不用管，左上角即代表x,y coordinate
		now_text_rect.center=(text.x,text.y)

	gameDisplay.blit(now_text,now_text_rect.center)
	pygame.display.update()	
	
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
			return True

def correction(objects,proportion): ## defines area that the object can operate
	if objects.y < display_height*proportion:
		objects.y = display_height*proportion

	if objects.y+objects.height > display_height:
		objects.y = display_height - objects.height

	if objects.x < 0:
		objects.x = 0

	if objects.x + objects.width > display_width:
		objects.x = display_width - objects.width

'''
def flash():
	set_MainCharacter(nothing,nothingImg)
'''
def Opening_Trailer():

	stage2 = obstacle(1280,280,192,96,-1)
	button = figure(640,480,192,96)
	startText= text('press Space to start',20,red,680,480)
	stage2Img = pygame.image.load("stage2.png") 
	buttonImg = pygame.image.load("button.png") 
	Exit = False
	stop = True
	logging.info("start loop")
	
	while not Exit:	
	
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed, will quit")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					stop = False


					
		gameDisplay.fill(black)	
		
		set_Obstacle(stage2,stage2Img)
		stage2.x += stage2.movespeed
		

		if stage2.x < 640 and stop == True:

			stage2.movespeed =0
			set_Figure(button,buttonImg)
			set_Text(startText,'Center')
			
		elif stop == False:
			stage2.movespeed = -10
			if stage2.x + stage2.width < 0:
					Exit = True
		
		


def game_loop():

	## load / play song
	## play song
	## https://nerdparadise.com/programming/pygame/part3
	pygame.mixer.music.load("下一站茶山劉.mp3")
	print("play music")
	pygame.mixer.music.play(-1)

	# load wave sound
	wave=pygame.mixer.Sound("wave.wav")



	##uploading image of boats
	boatImg0 = pygame.image.load("boat.png") 
	boatImg1 = pygame.image.load("boat1.png")
	boatImg2 = pygame.image.load("boat2.png")
	boatImgList=[boatImg0,boatImg1,boatImg2]
	
	# uploading other Images
	bikeImg = pygame.image.load("bike.png")
	peopleImg = pygame.image.load("people.png")	
	gpaImg = pygame.image.load("GPA.png")
	hpbarImg = pygame.image.load("HPbar.png")
	nothingImg = pygame.image.load("nothing.png") ## 不知道怎麼做flash的產物，可以不用理他，是一張空白的png檔
	endlineImg = pygame.image.load("endline3.png")
	backgroundImg = pygame.image.load("background.png")
	backgroundImg = pygame.transform.scale(backgroundImg, (1280, 320))



	# defining Objects
	background=figure(0,0,1280,320)
	background2=figure(1280,0,1280,320)
	
	boat = mainCharacter(display_width*0.1 , display_height*0.75 , 96 , 96 )  #set status of object
	nothing = mainCharacter(display_width*0.1 , display_height*0.75 , 96 , 96 )

	bike = obstacle(1280,random.randrange(display_height*320/960, display_height*1-96),96,96,-10)
	people = obstacle(1280,random.randrange(display_height*320/960, display_height*1-96),96,96,-5)
	obstaclelist=[bike,people]## estabilish a obstacle list	
	gpa_icon=figure(30,50,96,96)
	GPA=4.3
	# (self,content,size,color,x,y)
	now_gpa=text(str(GPA),60,black,gpa_icon.width+96,gpa_icon.height) 	
	## create ending object
	ending_message=text("You have failed your semester!",80,red,display_width*(1/2),display_height*(2/3))
	now_time=text(str(0.0),60,black,display_width,0)
	## create ending object of game 

	# figure(x,y,width,height,movespeed)
	endline=obstacle(display_width,display_height*(1/3),50,display_height*2/3,-2) # width 暫設50 px 


	x_change = 0 #set constent
	y_change = 0	
	# dodged=0  ## dodged ; congratulating on dodge??	
	boatImgNum=0	#控制 boat gif fps
	frame=0 #初始幀數

### game exit while loop
	gameExit = False
	
	while not gameExit:
		
		## set time on right upper field
		set_Text(now_time,"Right")
		now_time.content="%-10.1f"%(pygame.time.get_ticks()/1000)
		# print("Game has run for ",float(pygame.time.get_ticks()/1000)," seconds")
		
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
					x_change = -7
					wave.play()
					
				if event.key == pygame.K_RIGHT:#pressing right arrow will increase x-axis coordinate
					x_change = 7
					wave.play()
					
				if event.key == pygame.K_UP:#pressing UP arrow will decrease Y-axis coordinate
					y_change = -7
					wave.play()

				if event.key == pygame.K_DOWN:#pressing Down arrow will increase x-axis coordinate
					y_change = 7
					wave.play()
					
			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0

		
		boat.x += x_change
		boat.y += y_change

		'''
		## define the same object, but is invisible
		nothing.x += x_change
		nothing.y += y_change
		'''
		
		gameDisplay.fill(white)
		
		set_Figure(background,backgroundImg)
		background.x-=10
		if background.x < -1280:
			background.x =1280
		set_Figure(background2,backgroundImg)
		background2.x-=10
		if background2.x < -1280:
			background2.x =1280
		
		if frame % 20 == 1:				#將river set在 riverDisplay圖層上(每10幀改變一次riverDisplay樣貌)
			set_River(riverDisplay,20,20,Colorlist)	
		gameDisplay.blit(riverDisplay, (0,320)) #再將riverDisplay放在gameDisplay圖層
		
		
		#####################將boatImg 組成gif 並設定幾次畫面(frame)更新會換下一張###################
		if boatImgNum!=2:                                  
			set_MainCharacter(boat,boatImgList[boatImgNum])
			if frame % 10 == 0:     #每10幀數換下一張圖片
				boatImgNum += 1

		elif boatImgNum==2:
			set_MainCharacter(boat,boatImgList[boatImgNum])
			if frame % 10 == 0:
				boatImgNum = 0

		
		set_Obstacle(bike,bikeImg)
		bike.x += bike.movespeed
		set_Obstacle(people,peopleImg)
		people.x += people.movespeed
		
		##  correction of boundaries ; 
		correction(boat,320/960)  ## 界線是設在1/3，太低可以之後再調

		
		if bike.x < 0:
			bike.y = random.randrange(display_height*320/960, display_height-bike.height)
			bike.x = display_width
			bike.movespeed -= 0.5	
			
		if people.x < 0:
			people.y = random.randrange(display_height*320/960, display_height-people.width)
			people.x = display_width
			people.movespeed -= 0.5				
		
		if (pygame.time.get_ticks()/1000)>=10.0: # >60s 就讓最後一條線進來
			# print("endline is appearing................")
			set_Obstacle(endline,endlineImg)
			endline.x += endline.movespeed


		#根據gpa 每0.5顯示一格hpbar
		# figure(self,x,y,width,height):
		for i in range(0,int(math.floor(float(now_gpa.content)/0.5))):
			hpbar = figure( gpa_icon.x+50*(i+1) , gpa_icon.y , 96 , 96)
			set_Figure(hpbar,hpbarImg)
			
		set_Figure(gpa_icon,gpaImg)			
		set_Text(now_gpa,"None")
		
		if float(now_gpa.content)<=0:
			## stop music
			pygame.mixer.music.stop()
			#display message
			set_Text(ending_message,"Center")
			print("printed ending message")
			time.sleep(3)
			game_loop()
		

		## if collision then set nothing.png on top of boat for ? s


		## collision method 2 ; true/false & glitter
		for obstacles in obstaclelist:
			#def collision(object1,object2):
			if collision(boat,obstacles):

				changed_gpa="%-10.2f"%(float(now_gpa.content)-0.1) ## 測試0.02是減少最好的，等等改
				now_gpa.content=str(changed_gpa)
				

		if float(now_gpa.content)<2.5:
			now_gpa.color=red
		else:
			now_gpa.color=black
			

		## if crossed endline
		if collision(boat,endline):
			pygame.quit()
			quit()






		pygame.display.update()
		clock.tick(60)  ## it will just make thing move faster

Opening_Trailer()
game_loop()

pygame.quit()
logging.info("I am the last line of the code")
quit()