import logging
import pygame
import time
import random  
import os
import math
display_width =  1280 
display_height = 960   
gameDisplay = pygame.display.set_mode((display_width, display_height)) 
class calculate_gpa():

	def __init__(self,allgpa):
		self.allgpa=allgpa

	def add(self,new_gpa):
		self.allgpa.append(float(new_gpa))

	def mean(self):
 		mean_gpa=sum(self.allgpa)/len(self.allgpa)
 		return mean_gpa
###############################################################################################
##################################      for Stage1        #####################################
###############################################################################################

###############################################################################################
##################################      for Stage2        #####################################  .
###############################################################################################
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
		
		
###############################################################################################		
##################################      for Stage3        #####################################
###############################################################################################

# encoding: utf-8
import pygame
#-------------------------------------------------------------------------
# 畫Background.
#-------------------------------------------------------------------------
class Background(pygame.sprite.Sprite):
	
	def __init__(self, image_file, location):
		principleofficeImg=pygame.image.load('D:/PBC/Resource/principleoffice.png')
		principleofficeImg=pygame.transform.scale(principleofficeImg, (1280,960))
		pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
		self.image = principleofficeImg
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location
#-------------------------------------------------------------------------
# 畫Box.
#-------------------------------------------------------------------------
class Box(object):
    #-------------------------------------------------------------------------
    # 建構式.
    #   pygame    : pygame.
    #   canvas    : 畫佈.
    #   name    : 物件名稱.
    #   rect      : 位置、大小.
    #   color     : 顏色.
    #-------------------------------------------------------------------------
    def __init__( self, pygame, canvas, name, rect, color):
        self.pygame = pygame
        self.canvas = canvas
        self.name = name
        self.rect = rect
        self.color = color
 
        self.visivle = True
        
    #-------------------------------------------------------------------------
    # 更新.
    #-------------------------------------------------------------------------
    def update(self):
        if(self.visivle):
            self.pygame.draw.rect( self.canvas, self.color, self.rect)
 
#-------------------------------------------------------------------------
# 畫圓.
#-------------------------------------------------------------------------
class Circle(object):
    #-------------------------------------------------------------------------
    # 建構式.
    #   pygame  : pygame.
    #   canvas  : 畫佈.
    #   name    : 物件名稱.
    #   pos     : 位置.  
    #   radius  : 大小.
    #   color   : 顏色.    
    #-------------------------------------------------------------------------
    def __init__( self, pygame, canvas, name, pos, radius, color):
        self.pygame = pygame
        self.canvas = canvas
        self.name = name
        self.pos = pos
        self.radius = radius
        self.color = color
        
        self.visivle = True
 
    #-------------------------------------------------------------------------
    # 更新.
    #-------------------------------------------------------------------------
    def update(self):
        if(self.visivle):
            self.pygame.draw.circle( self.canvas, self.color, self.pos , self.radius)

