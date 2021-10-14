import pygame
import os

width, height = 900, 550
win= pygame.display.set_mode((width,height))
green=(0,230,50)
white=(255,255,255)
Soccer_Player=pygame.image.load(os.path.join('Assets','soccer-player.png'))
Ball_Image=pygame.image.load(os.path.join('Assets','ball.png'))
Resize_Ball=pygame.transform.scale(Ball_Image,(40,50))
Resize_SoccerPlayer= pygame.transform.scale(Soccer_Player,(40,50))
fps=30
move_speed=5
Top_Horiz_Outline=pygame.Rect(0,10,width,10)
R_Vert_Outline=pygame.Rect(width-10,10,10,height-15)
Bot_Horiz_Outline=pygame.Rect(0,height-15,width,10)

def d_win(player):
	win.fill(green)
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

	clock = pygame.time.Clock()
	run= True
	while run:
		clock.tick(fps)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False
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


		
		d_win(player)
	
	
	
	pygame.quit()


if __name__ == "__main__":
	main()	