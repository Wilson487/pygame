###################匯入模組###################
import pygame
import sys
import math
##################定義函式##################
def check_click(pos,x_mix,y_mix,x_max,y_max):
    x_match=x_mix<pos[0]<x_max
    y_match=y_mix<pos[0]<y_max
    if x_match and y_match:
        return True
    else:
        return False
###################初始化####################
pygame.init()
width = 500
height= 500
###################建立視窗及物件###################
#設定窗大小
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Minecraft")
###################設定文字###################
typeface=pygame.font.get_default_font()
font=pygame.font.Font(typeface,24)
title=font.render("Start",True,(0,0,0))
tw=title.get_width()
th=title.get_height()
###################建立畫布###################
bg=pygame.Surface((width,height))
bg.fill((0,0,0))
###################循環偵測###################
paint=False
while True:
    screen.blit(bg,(0,0))
    mouse_pos=pygame.mouse.get_pos()
    # print(mouse_pos)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if check_click(mouse_pos,0,0,tw,th):
            paint=not paint
    if paint:
        pygame.draw.circle(bg, (255,0,250),(200,100),30,0)
        pygame.draw.circle(bg, (255,0,250),(400,100),30,0)
        pygame.draw.rect(bg, (100,50,125),[270,130,60,40],5)
        pygame.draw.ellipse(bg, (255,0,0),[130,160,60,35],5)
        pygame.draw.ellipse(bg, (255,0,0),[400,160,60,35],5)
        pygame.draw.line(bg, (255,0,250),(200,220),(320,220),3)

        pygame.display.update()
        ###################繪製圖形###################
        pygame.draw.circle(bg, (255,0,250),(70,100),30,0)
        pygame.draw.circle(bg, (255,0,250),(280,100),30,0)
        # 畫矩形, (畫布, 顏色, [x, y, 寬, 高], 線寬)
        pygame.draw.rect(bg, (100,50,125),[100,207,150,70],5)
        # 畫橢圓, (畫布, 顏色, [x, y, 寬, 高], 線寬)
        pygame.draw.ellipse(bg, (255,0,0),[20,240,60,35],5)
        pygame.draw.ellipse(bg, (255,0,0),[310,240,60,35],5)
        # 畫線, (畫布, 顏色, 起點, 終點, 線寬)
        pygame.draw.line(bg, (255,0,250),(114,299),(234,299),3)