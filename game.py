import pygame
import os
import random

pygame.init()
width, height = 900, 550
win= pygame.display.set_mode((width,height))
green=(0,230,50)
white=(255,255,255)
transparent=(0,0,0,0)
Soccer_Player=pygame.image.load(os.path.join('Assets','soccer-player.png'))
Ball_Image=pygame.image.load(os.path.join('Assets','ball.png'))
Player_Ball=pygame.image.load(os.path.join('Assets','soccer-player-and-ball.png'))
Resize_Ball=pygame.transform.scale(Ball_Image,(60,70))
Resize_SoccerPlayer= pygame.transform.scale(Soccer_Player,(40,50))
Resize_Player_Ball=pygame.transform.scale(Player_Ball,(40,50))
fps=60
move_speed=5
Top_Horiz_Outline=pygame.Rect(40,10,width,10)
R_Vert_Outline=pygame.Rect(width-10,10,10,height-15)
Bot_Horiz_Outline=pygame.Rect(40,height-15,width,10)
Goalline=pygame.Rect(40,10,10,height-15)
Bot_Goalline=pygame.Rect(0,(height/2)+60,40,10)
Top_Goalline=pygame.Rect(0,(height/2)-70,40,10)
clock=pygame.time.Clock()




def d_win(player,shown_time, Player_Model,Has_Ball,ball_x,ball_y,goals):
	font=pygame.font.Font('freesansbold.ttf', 64)
	sfont=pygame.font.Font('freesansbold.ttf', 30)
	timer_text=font.render(str(shown_time/1000), True, green, white)
	goal_text=sfont.render("Goals: "+str(goals),True,green,white)
	win.fill(green)
	win.blit(timer_text,((width/2)-50,50))
	win.blit(goal_text,((width/2)+300,30))
	pygame.draw.rect(win,white,Top_Horiz_Outline)
	pygame.draw.rect(win,white,R_Vert_Outline)
	pygame.draw.rect(win,white,Bot_Horiz_Outline)
	pygame.draw.circle(win,white,(width,height/2),25)
	pygame.draw.circle(win,white,(width,height/2),150,15)
	pygame.draw.rect(win,white,Goalline)
	pygame.draw.rect(win,white,Bot_Goalline)
	pygame.draw.rect(win,white,Top_Goalline)
	if player.x<0:
		player.x=0
	if player.x>width-40:
		player.x=width-40
	if player.y<0:
		player.y=0
	if player.y>height-50:
		player.y=height-50
	win.blit(Player_Model,(player.x,player.y))
	if Has_Ball==False:
		win.blit(Resize_Ball,(ball_x,ball_y))
	pygame.display.update()
	
def main():
	player=pygame.Rect(width/2,height/2,40,50)
	Move_Start_Time=0
	ctime=0
	run= True
	Player_Model=Resize_SoccerPlayer
	Has_Ball=False
	ball_x=random.randint(40,width-40)
	ball_y=random.randint(10,height-50)
	print(ball_x,ball_y)
	goals=0
	while run:
		shown_time=30000
		clock.tick(fps)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False
			if event.type==pygame.KEYDOWN:
				if Move_Start_Time==0:
					Move_Start_Time= pygame.time.get_ticks() #gets the time for when the player first moves
					
		keys=pygame.key.get_pressed()
		if keys[pygame.K_a]: #moving left
			player.x-=move_speed
		if keys[pygame.K_d]: #moving right
			player.x+=move_speed
		if keys[pygame.K_w]: #moving up
			player.y-=move_speed
		if keys[pygame.K_s]: #moving down
			player.y+=move_speed
		if keys[pygame.K_f]:   
			if (player.x>ball_x-30 and player.x<ball_x+30) and (player.y<ball_y+30 and player.y>ball_y-30) and Has_Ball==False:
				print('yes')
				Player_Model=Resize_Player_Ball
				Has_Ball=True
			if (player.x>-5 and player.x<42) and (player.y>(height/2)-105 and player.y<(height/2)+50) and Has_Ball==True:
				print("goal")
				Player_Model=Resize_SoccerPlayer
				Has_Ball=False
				ball_x=random.randint(40,width-40)
				ball_y=random.randint(10,height-50)
				print(ball_x,ball_y)
				goals+=1

		if Move_Start_Time!=0:
			ctime=pygame.time.get_ticks() #gets the running time from when the player started moving
			if shown_time-(ctime- Move_Start_Time) <= 0:
				shown_time=0
			else:
				shown_time=shown_time-(ctime- Move_Start_Time)
		#if ctime- Move_Start_Time>10000: #subtracts the start time from the running time, if it is greater than 30s then time is up
			#print('10 seconds')

		


		
		d_win(player,shown_time, Player_Model,Has_Ball,ball_x,ball_y,goals)
	
	
	
	pygame.quit()


if __name__ == "__main__":
	main()	