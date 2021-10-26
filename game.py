import pygame
import os

pygame.init()
width, height = 900, 550
win= pygame.display.set_mode((width,height))
green=(0,230,50)
white=(255,255,255)
Soccer_Player=pygame.image.load(os.path.join('Assets','soccer-player.png'))
Ball_Image=pygame.image.load(os.path.join('Assets','ball.png'))
Resize_Ball=pygame.transform.scale(Ball_Image,(40,50))
Resize_SoccerPlayer= pygame.transform.scale(Soccer_Player,(40,50))
fps=60
move_speed=5
Top_Horiz_Outline=pygame.Rect(0,10,width,10)
R_Vert_Outline=pygame.Rect(width-10,10,10,height-15)
Bot_Horiz_Outline=pygame.Rect(0,height-15,width,10)
clock=pygame.time.Clock()




def d_win(player,shown_time):
	font=pygame.font.Font('freesansbold.ttf', 64)
	text=font.render(str(shown_time/1000), True, green, white)
	win.fill(green)
	win.blit(text,(width/2,100))
	pygame.draw.rect(win,white,Top_Horiz_Outline)
	pygame.draw.rect(win,white,R_Vert_Outline)
	pygame.draw.rect(win,white,Bot_Horiz_Outline)
	pygame.draw.circle(win,white,(width,height/2),25)
	pygame.draw.circle(win,white,(width,height/2),150,15)
	if player.x<0:
		player.x=0
	if player.x>width-40:
		player.x=width-40
	if player.y<0:
		player.y=0
	if player.y>height-50:
		player.y=height-50
	win.blit(Resize_SoccerPlayer,(player.x,player.y))
	win.blit(Resize_Ball,(300,400))
	pygame.display.update()
	
def main():
	player=pygame.Rect(width/2,height/2,40,50)
	Move_Start_Time=0
	ctime=0
	run= True
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
		if keys[pygame.K_f]  and (player.x>300-50 and player.x<300+50) and (player.y<400+50 and player.y>400-50):
			print('yes')
		if Move_Start_Time!=0:
			ctime=pygame.time.get_ticks() #gets the running time from when the player started moving
			if shown_time-(ctime- Move_Start_Time) <= 0:
				shown_time=0
			else:
				shown_time=shown_time-(ctime- Move_Start_Time)
		#if ctime- Move_Start_Time>10000: #subtracts the start time from the running time, if it is greater than 30s then time is up
			#print('10 seconds')

		


		
		d_win(player,shown_time)
	
	
	
	pygame.quit()


if __name__ == "__main__":
	main()	