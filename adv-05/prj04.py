######################匯入模組######################
import pygame
import sys
import math
import os
import sys
import time
import random 
####################定義函式######################
def gophers_update():
    global tick,pos,score
    if tick>max_tick:
        new_pos=random.randint(0,5)
        pos=pos6[new_pos]
        tick=0
    else:
        tick+=1
    screen.blit(gopher,(pos[0]-gopher.get_width()/2,pos[1]-gopher.get_height()/2))
    screen.blit(gopherB,(posB[0]-gopherB.get_width()/2,pos[1]-gopherB.get_height()/2))


def gopher_update():
    global tick,pos,score
    if tick > max_tick:
        now_pos=random.randint(0,5)
        pos=pos6[now_pos]
        tick=0
def gopherB_update():
    global tick,pos,score
    if tick > max_tick:
        now_posB=random.randint(0,5)
        posB=pos6[now_posB]
        tickB=0

        
    else:
        tickB+=1

    
    



def score_update():
    score_sur=score_font.render(str(score),False,red)
    screen.blit(score_sur,(10,10))
def check_clickB(posB,x_mixB,y_mixB,x_maxB,y_maxB):
    x_matchB=x_mixB<posB[0]<x_maxB
    y_matchB=y_mixB<posB[1]<y_maxB
    if x_matchB and y_matchB:
        return True
    else:
        return False
def check_click(pos,x_mix,y_mix,x_max,y_max):
    x_match=x_mix<pos[0]<x_max
    y_match=y_mix<pos[1]<y_max
    if x_match and y_match:
        return True
    else:
        return False
    screen.blit(gophers,(pos[0]-gophers.get_width()/2,pos[1].gophers.get_height()/2))
    screen.blit(gopher,[pos6])
#    screen.blit(gopherB,[pos6])
####################初始化######################
os.chdir(sys.path[0])
pygame.init()
blue = (0,0,255)
white=(255,255,255)
black = (0,0,0)
red = (255,0,0)
clock = pygame.time.Clock()
tick = 0
tickB = 0
max_tick = 20
max_tickB = 20
bg_img='Gophers_BG_800x600.png'
bg=pygame.image.load(bg_img)
bg_x=bg.get_width()
bg_y=bg.get_height()

######################建立視窗######################
bg_x = 800
bg_y = 600
screen = pygame.display.set_mode([bg_x,bg_y])
pygame.display.set_caption("打地鼠")
######################背景物件######################
######################地鼠物件######################
pos6=[[195,305],[400,305],[610,305],[195,450],[400,450],[610,450]]

# pos6=[[200,200],[300,200],[400,200],[200,300],[300,300],[400,300]]
posB=pos6[0]
pos=pos6[0]
sb="Gophers150.png"
gophers=pygame.image.load(sb)
gophers=pygame.image.load('Gophers_BG_800x600.png')
gopher = pygame.image.load("大熊.jpg") # 地鼠圖片
gopherB = pygame.image.load("胖虎.jpg")
        
    
######################分數物件######################
score=0
typeface=pygame.font.get_default_font()
score_font=pygame.font.Font(typeface,24)
######################滑鼠物件######################

######################循環偵測######################
while True:
    clock.tick(30)
    mouse_pos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos,pos[0]-50,pos[1]-50,pos[0]+50,pos[1]+50):
                tick=max_tick+1
                score -= 3
            if check_click(mouse_pos,pos[0]-50,pos[1]-50,pos[0]+50,pos[1]+50):
                tickB=max_tickB+1
                # score +=1
        screen.blit(bg,(0,0))
        gophers_update()
        gophers_update()
        score_update()
    pygame.display.update()
Gophers_BG_800x600.png