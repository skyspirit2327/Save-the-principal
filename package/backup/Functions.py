import logging
import pygame
import time
import random  
import os
import math
##################################      for Stage1        #####################################

#-空-


##################################      for Stage2        #####################################
#os.chdir('D:/PBC') #package資料夾所在目錄
from package.Class import mainCharacter,obstacle,special_obstacle,figure,text
display_width =  1280 
display_height = 960    
gameDisplay = pygame.display.set_mode((display_width, display_height)) 
clock = pygame.time.Clock()  

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
###############################################################################################
##################################      for Stage3        #####################################
###############################################################################################
os.chdir('D:/PBC') #package資料夾所在目錄
import os, sys, random
import pygame 
from pygame.locals import *
import logging
import random  
import os
import math
from package.Class import Background,Box,Circle
#os.chdir('')  #圖片聲音檔所在目錄
canvas_width = 1280
canvas_height = 650
 
# 背景顏色.
#block = (255,250,240)
BackGround = Background(0,[0,0]) ####背景圖

# 磚塊數量串列.
bricks_list = []
 
# 移動速度.
dx =  7
dy = -7
 
# 遊戲狀態.
# 0:等待開球
# 1:遊戲進行中
game_mode = 0
def isCollision( x, y, boxRect):
	if (x >= boxRect[0] and x <= boxRect[0] + boxRect[2] and y >= boxRect[1] and y <= boxRect[1] + boxRect[3]):
		return True;		  
	return False;  
def resetGame():
	# 宣告使用全域變數.
	global game_mode, brick_num, bricks_list, dx, dy
 
	# 磚塊
	for bricks in bricks_list:
		# 亂數磚塊顏色
		bricks.color = [255,255,255]		  
		# 開啟磚塊.
		bricks.visivle = True
	# 0:等待開球
	game_mode = 0
	# 磚塊數量.
	brick_num = 120	 
	# 移動速度.
	dx =  7
	dy = -7












		
		
