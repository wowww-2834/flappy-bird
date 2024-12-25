import pygame
from pygame.locals import*
import random

pygame.init()

p = 0.1 # trọng lực
bird_y = 0 # tọa độ của chim
score = 0 # diem
game_play = True
hscore = 0

# score
game_font = pygame.font.Font(f'04B_19.TTF',40)
def score_view():
    if game_play:
        score_f =game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_hcn = score_f.get_rect(center = (200,100))
        screen.blit(score_f,score_hcn)
    if game_play==False:
        score_f =game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_hcn = score_f.get_rect(center = (200,30))
        screen.blit(score_f,score_hcn)
        hscore_f =game_font.render(f'High Score: {int(hscore)}', True, (255, 255, 255))
        hscore_hcn = hscore_f.get_rect(center = (200,100))
        screen.blit(hscore_f,hscore_hcn)


#khung
HEIGHT = 768
WIDTH = 432
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("flappy bird")
icon = pygame.image.load(f'assets/yellowbird-midflap.ico')
pygame.display.set_icon(icon)

#background
bg = pygame.image.load(f'assets/background-night.png') 
bg = pygame.transform.scale2x(bg)
fl = pygame.image.load(f'assets/floor.png')
fl = pygame.transform.scale2x(fl)
fl_x = 0

# nhân vật
xbird = 100
ybird = 334
bird = pygame.image.load(f'assets/yellowbird-midflap.png')
bird = pygame.transform.scale2x(bird)
bird_hcn = bird.get_rect(center = (xbird,ybird))

#ống cống
tube = pygame.image.load(f'assets/pipe-green.png')
tube = pygame.transform.scale(tube, (82, 506))
pipe = pygame.image.load(f'assets/tube-green.png')
pipe = pygame.transform.scale(pipe, (82, 506))


tube_x = 432



#game over
end = pygame.image.load(f'assets/message.png')
end = pygame.transform.scale2x(end)
end_hcn = end.get_rect(center = (216,334))

def check_var():
    if pygame.Rect.colliderect(bird_hcn,tube_hcn):
        return False
    if pygame.Rect.colliderect(bird_hcn,pipe_hcn):
        return False
    if pygame.Rect.colliderect(bird_hcn,tube_hcm):
        return False
    if pygame.Rect.colliderect(bird_hcn,pipe_hcm):
        return False 
    if bird_hcn.bottom >= 670 or bird_hcn.top <= 0:
        return False
    else:
        return True

height = random.randint(500,700)
Height = random.randint(500,700)
 

run = True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_play:
                bird_y = -3
        if event.type == pygame.MOUSEBUTTONDOWN and game_play==False:
            bird_y = 0
            bird_hcn.center = (100,334)
            score = 0
            game_play = True
           

    screen.blit(bg,(0,0))
    tube_x -= 1 
    tube_hcn = tube.get_rect(center = (tube_x,height))
    tube_hcm = tube.get_rect(center = (tube_x+300,Height))
    pipe_hcn = pipe.get_rect(center = (tube_x,-750+height))
    pipe_hcm = pipe.get_rect(center = (tube_x+300,-750+height))
    screen.blit(tube,tube_hcn)
    screen.blit(tube,tube_hcm)
    screen.blit(pipe,pipe_hcn)
    screen.blit(pipe,pipe_hcm)
    if tube_x <= -340:
        tube_x = 432
        height = random.randint(500,700)
        Height = random.randint(500,700)
    fl_x -= 1
    screen.blit(fl,(fl_x,670))
    screen.blit(fl,(fl_x+432,670))
    if fl_x == -432:
       fl_x = 0
    if game_play:
       screen.blit(bird,bird_hcn)
       bird_y += p
       bird_hcn.centery += bird_y
       if bird_hcn.centerx == tube_x or bird_hcn.centerx == tube_x+300:
           score += 1
       if score > hscore: hscore=score
       
       score_view()
       game_play = check_var()
    else:
        screen.blit(end,end_hcn)
        score_view()

    pygame.display.update()

pygame.quit()