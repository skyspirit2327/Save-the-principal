
def Opening_Trailer():

	stage2 = obstacle(1280,180,192,96,-4)
	ZhoushanRiver = obstacle (1280+500,265,192,96,-4)
	
	button = figure(420,510,192,96)
	startText= text('press Space to start',20,red,640,780)
	
	stage2Img = pygame.image.load("stage2.png") 
	stage2Img = pygame.transform.scale(stage2Img, (500, 400))
	ZhoushanRiverImg = pygame.image.load("ZhoushanRiver.png")
	ZhoushanRiverImg = pygame.transform.scale(ZhoushanRiverImg, (400, 240))
	buttonImg = pygame.image.load("button.png") 
	buttonImg = pygame.transform.scale(buttonImg, (450, 215))
	
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


		
		gameDisplay.fill(black)	
		
		set_Obstacle(stage2,stage2Img)
		set_Obstacle(ZhoushanRiver,ZhoushanRiverImg)
		stage2.x += stage2.movespeed
		ZhoushanRiver.x += ZhoushanRiver.movespeed

		if stage2.x < 200 and Start_Play == True:

			stage2.movespeed =0
			ZhoushanRiver.movespeed=0
			set_Figure(button,buttonImg)
			set_Text(startText,'Center')
			
		elif Start_Play == False: #如果按下空白建 Start_Play 就會變成 False
			stage2.movespeed = -4
			ZhoushanRiver.movespeed=-4
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
		set_Text(failText,'Center')
		set_Text(YNText,'Center')
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
