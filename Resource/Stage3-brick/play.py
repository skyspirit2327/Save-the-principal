# encoding: utf-8
 
import os, sys, random
import pygame 
from pygame.locals import *
from drew import *
import logging
import random  
import os
import math


# 視窗大小.
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
#-------------------------------------------------------------------------
# 函數 : GPA 顯示.
#-------------------------------------------------------------------------
display_width =  1280 
display_height = 960 
gameDisplay = pygame.display.set_mode((display_width, display_height))
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
		elif position=="None":	#不用管，左上角即代表x,y coordinate
			now_text_rect.center=(self.x,self.y)

		gameDisplay.blit(now_text,now_text_rect.center)

	
def set_ColorBlock(layer,color,y,x,width,height): ## set HP bar
	pygame.draw.rect(layer,color, pygame.Rect(y, x, width, height))
#-------------------------------------------------------------------------
# 函數:碰撞判斷.
#	x		: x 
#	y		: y 
#	boxRect : 矩形
#-------------------------------------------------------------------------
def isCollision( x, y, boxRect):
	if (x >= boxRect[0] and x <= boxRect[0] + boxRect[2] and y >= boxRect[1] and y <= boxRect[1] + boxRect[3]):
		return True;		  
	return False;  
 
#-------------------------------------------------------------------------
# 函數:初始遊戲.
#-------------------------------------------------------------------------
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
 
# 初始.
pygame.init()
# 顯示Title.
pygame.display.set_caption(u"打磚塊遊戲")

# 建立畫佈大小.
canvas = pygame.display.set_mode((canvas_width, canvas_height))
BackGround = Background(0,[0,0])
canvas.fill([255, 255, 255])
canvas.blit(BackGround.image, BackGround.rect)

# 時脈.
clock = pygame.time.Clock()
 
# 設定字型-黑體.
font = pygame.font.SysFont('simhei', 30)
# 底板.
paddle_x = 0
paddle_y = (canvas_height - 48)
paddle = Box(pygame, canvas, "paddle", [paddle_x, paddle_y, 100, 24], (0,0,0))
 
# 球.
ball_x = paddle_x
ball_y = paddle_y
ball   = Circle(pygame, canvas, "ball", [ball_x, ball_x], 8, (0,0,0))
 
# 建立磚塊
brick_num = 0
brick_x = 70
brick_y = 130
brick_w = 0
brick_h = 0
for i in range( 0, 120):
	if((i % 12)==0):
		brick_w = 0
		brick_h = brick_h + 30		 
	bricks_list.append (Box(pygame, canvas, "brick_"+str(i), [	brick_w + brick_x, brick_h+ brick_y, 90, 25], [255,255,255]))
	brick_w = brick_w + 95

# 建立GPABar
gpaImg = pygame.image.load("D:/PBC/Resource/GPA.png")
hpbarImg = pygame.image.load("D:/PBC/Resource/HPbar.png")
#初始分數.
gpa_1=4.0
gpa_2=4.0
gpa_3=4.3
final_grade=''
# figure / text objects	
gpa_icon=figure(30,30,96,96)
new_gpa=text(str(gpa_3),60,(0,0,0),gpa_icon.width+96,gpa_icon.height)
#-------------------------------------------------------------------------	  
# 過關畫面.
#-------------------------------------------------------------------------
def final_screen():
	bye_1=text("You Save The Principle",50,(227,23,13),640,200)
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
	canvas.fill([255, 255, 255]) ##顯示背景
	canvas.blit(BackGround.image, BackGround.rect) ##顯示背景
	
	# 磚塊
	for bricks in bricks_list:
		# 球碰磚塊.
		if(isCollision( ball.pos[0], ball.pos[1], bricks.rect)):
			if(bricks.visivle):				   
				# 扣除磚塊.
				brick_num = brick_num -1
				##### 初始遊戲. ##### 改成跳出頁面 #####
				if(brick_num <= 0):
					final_gpa=gpa_1+gpa_2+gpa_3
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
	
	
 
# 離開遊戲.
pygame.quit()
quit()
