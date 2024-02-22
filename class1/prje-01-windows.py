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

    s.blit(bg,(0,0))
    pygame.display.update()
    ###################繪製圖形###################
    pygame.draw.circle(bg, (255,0,250),(70,100),30,0)
    pygame.draw.circle(bg, (255,0,250),(280,100),30,0)
    # 畫矩形, (畫布, 顏色, [x, y, 寬, 高], 線寬)
    pygame.draw.rect(bg, (100,50,125),[100,207,150,70],5)
    # 畫橢圓, (畫布, 顏色, [x, y, 寬, 高], 線寬)
    pygame.draw.ellipse(bg, (255,0,0),[130,160,60,35],5)
    # 畫線, (畫布, 顏色, 起點, 終點, 線寬)
    pygame.draw.line(bg, (255,0,250),(50,50),(114,234),3)
    # 畫多邊形, (畫布, 顏色, [[x1, y1], [x2, y2], [x3, y3]], 線寬)
    pygame.draw.polygon(bg, (255,0,255),[[100,100],[0,200],[200,200]],0)
    pygame.draw.arc(bg, (255,0,255),[100,100,100,50],math.radians(180),math.radians(0),2)










    pygame.mouse.get_pos()
    x,y=pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        print("click!")
        print(pygame.mouse.get_pos())