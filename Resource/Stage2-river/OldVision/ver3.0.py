import logging
import pygame
import time
import random  
import os

#os.chdir('D:/SkySpiriT/NTU/PBC/Project/') #讀取檔案目錄

logging.basicConfig(level=logging.DEBUG)
pygame.init()


display_width = 1280
display_height = 960
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
def set_Text(text):
	now_text=pygame.font.Font("freesansbold.ttf",text.size)
	now_text=now_text.render(text.content,True,text.color)
	now_text_rect=now_text.get_rect()
	now_text_rect.center=(text.x,text.y)
	gameDisplay.blit(now_text,now_text_rect.center)
	pygame.display.update()	
	
def set_ColorBlock(layer,color,y,x,width,height):
	pygame.draw.rect(layer,color, pygame.Rect(y, x, width, height))
	
def set_River(layer,block_width,block_height,colorlist):
		for i in range(0,1281,block_width):
			for j in range(0,641,block_height):
				set_ColorBlock(layer,colorlist[random.randrange(0,len(colorlist))],i,j,block_width,block_height)



def game_loop():

	boatImg0 = pygame.image.load("boat.png")  ##uploading image
	boatImg1 = pygame.image.load("boat1.png")
	boatImg2 = pygame.image.load("boat2.png")
	boatList=[boatImg0,boatImg1,boatImg2]
	
	bikeImg = pygame.image.load("bike.png")
	peopleImg = pygame.image.load("people.png")	
	gpaImg= pygame.image.load("GPA.png")

	boat = mainCharacter(display_width*0.1 , display_height*0.75 , 96 , 96 )  #set status of object
	
	bike = obstacle(1280,random.randrange(display_height*320/960, display_height*1-96),96,96,-10)
	people = obstacle(1280,random.randrange(display_height*320/960, display_height*1-96),96,96,-5)
	obstaclelist=[bike,people]## estabilish a obstacle list
	
	gpa_icon=figure(30,50,96,96)

	GPA=4.3
	# def __init__(self,text,size,color,x,y):
	now_gpa=text(str(GPA),60,black,0+gpa_icon.width+40,0+gpa_icon.height) 

	## create ending object
	ending_message=text("You have failed your semester!",100,red,display_width*(1/2),display_height*(2/3))


	x_change = 0 #set constent
	y_change = 0	
	# dodged=0  ## dodged ; congratulating on dodge??

	
	boatImgNum=0	#控制 boat gif fps
	frame=0 
	
	gameExit = False
	
	while not gameExit:
	###########event handling loop###########
		
		for event in pygame.event.get():    #it gets any event that happens...movenment of mouse or clicking etc
			if event.type == pygame.QUIT:   # when we will click X it will quit the window
				logging.info("X is pressed")
				pygame.quit()
				quit()

			################This event will handle situation when ever any key will be pressed ##################################
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:#pressing left arrow will decrease x-axis coordinate
					x_change = -7
					
				if event.key == pygame.K_RIGHT:#pressing right arrow will increase x-axis coordinate
					x_change = 7
					
				if event.key == pygame.K_UP:#pressing UP arrow will decrease Y-axis coordinate
					y_change = -7

				if event.key == pygame.K_DOWN:#pressing Down arrow will increase x-axis coordinate
					y_change = 7
					
			################This event will handle situation when ever any key will be released ##################################
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0

		
		boat.x += x_change
		boat.y += y_change

		gameDisplay.fill(white)
		if frame % 20 ==0:				#將river set在 riverDisplay圖層上(每10幀改變一次riverDisplay樣貌)
			set_River(riverDisplay,20,20,Colorlist)	
		gameDisplay.blit(riverDisplay, (0,320)) #再將riverDisplay放在gameDisplay圖層
		
		
		#####################將boatImg 組成gif 並設定幾次畫面(frame)更新會換下一張###################
		if boatImgNum!=2:                                  
			set_MainCharacter(boat,boatList[boatImgNum])
			frame+=1
			if frame % 10 == 0:
				boatImgNum += 1

		elif boatImgNum==2:
			set_MainCharacter(boat,boatList[boatImgNum])
			frame+=1
			if frame % 10 == 0:
				boatImgNum = 0

		
		set_Obstacle(bike,bikeImg)
		bike.x += bike.movespeed
		set_Obstacle(people,peopleImg)
		people.x += people.movespeed
		
		
		
		#things_dodged(dodged)
		
		
		if boat.y < display_height*320/960:
			boat.y = display_height*320/960 
			
		if boat.y + boat.height> display_height:
			boat.y = display_height - boat.height
			
		if boat.x < 0:
			boat.x = 0
		
		if boat.x +boat.width > display_width :
			boat.x = display_width - boat.width
		
		
		if bike.x < 0:
			bike.y = random.randrange(display_height*320/960, display_height-bike.height)
			bike.x = 1280
			bike.movespeed -= 0.5	
			
		if people.x < 0:
			people.y = random.randrange(display_height*320/960, display_height-people.width)
			people.x = 1280
			people.movespeed -= 0.5				
		
		set_Figure(gpa_icon,gpaImg)
		set_Text(now_gpa)
		
		## 還需要想辦法把這個ending message output出來
		if float(now_gpa.content)<=0:
			#display message
			#gameDisplay.fill(white)
			set_Text(ending_message)
			time.sleep(2)
			game_loop()
			#gameExit()

		for obstacles in obstaclelist:
			crossed_times=0

			if boat.x+boat.width > obstacles.x and boat.x+boat.width < obstacles.x+obstacles.width:

				if (boat.y > obstacles.y and boat.y< obstacles.y+obstacles.y+obstacles.height) or (boat.y+boat.height > obstacles.y and boat.y+boat.height < obstacles.y+obstacles.y+obstacles.height):
					if crossed_times==1:
						continue
					else:
						changed_gpa="%-10.2f"%(float(now_gpa.content)-0.1) ## 測試0.02是減少最好的
						now_gpa.content=str(changed_gpa)
						crossed_times+=1

					print("crossed obeject")
					print("-0.03"," 1 time")
			
		
		if float(now_gpa.content)<2.5:
			now_gpa.color=red
		else:
			now_gpa.color=black
			

		pygame.display.update()
		clock.tick(60)  ## it will just make thing move faster

logging.info("calling the game loop")
game_loop()
logging.info("calling the quit function")
pygame.quit()
logging.info("I am the last line of the code")
quit()