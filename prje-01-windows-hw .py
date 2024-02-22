###################匯入模組###################
import pygame
import sys
import math
###################初始化###################
pygame.init()
width = 500
height= 500
###################建立視窗及物件###################
#設定窗大小
s=pygame.display.set_mode((width,height))
pygame.display.set_caption("Minecraft")
###################建立畫布###################
bg=pygame.Surface((width,height))
bg.fill((255,255,255))
###################循環偵測###################
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        s.blit(bg,(0,0))
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