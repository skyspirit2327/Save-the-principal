import logging
import pygame
import time
import random  
import os
import math
os.chdir('D:/PBC') #package資料夾所在目錄
from package.OP_ED import Opening_Trailer1,Opening_Trailer2,Opening_Trailer3,First_scene,Final_scene
from package.game_loop import stage1,stage2,stage3
from package.Class import calculate_gpa




#all_gpa=[]

logging.basicConfig(level=logging.DEBUG)
pygame.init()
display_width =  1280 
display_height = 960    
gameDisplay = pygame.display.set_mode((display_width, display_height))    
pygame.display.set_caption('拯救台大校長大作戰')
clock = pygame.time.Clock()
os.chdir('D:/PBC/Resource') #resource資料夾所在目錄


##################################      for starting      #####################################
First_scene()

##################################      for Stage1        #####################################
Opening_Trailer1()
stage1()
#Ending_Trailer1()

##################################      for Stage2        #####################################
Opening_Trailer2()
stage2()


##################################      for Stage3        #####################################
Opening_Trailer3()
stage3()
#Ending_Trailer3()

##################################      for ending        #####################################
#Final_scene() #我把他加入stage3後面了

pygame.quit()
logging.info("Quitting.........")
quit()