# a=1
# A=0
# while a==1:
#     print(A)
#     A+=1
#     if A == 11:
#         A=0
#####################匯入模組#####################
import pygame
import sys
import os
from pygame.locals import *
####################初始化#########################
os.chdir(sys.path[0])
pygame.init()
LIMIT_LOW=140#地面高度
clock=pygame.time.Clock()
####################載入圖片物件####################
img=pygame.image.load("image/bg.png")#加載背景
img_dinosaur=[
    pygame.image.load("image/小恐龍1.png"),
    pygame.image.load("image/小恐龍2.png"),
]
img_cacti=pygame.image.load("image/cacti.png")
bg_x=img.get_width()
bg_y=img.get_height()
bg_roll_x=0#背景圖片滾動位置
####################恐龍物件################
ds_x=50#恐龍x位置
ds_y=LIMIT_LOW#恐龍y位置
ds_index=0#恐龍圖片編號
jumpState=False#跳躍狀態
jumpValue=0#跳躍值
jump_height=13#跳躍高度
####################仙人掌物件###############
caciti_x=bg_x-100
caciti_y=LIMIT_LOW
caciti_shift=10



####################建立視窗####################
screen=pygame.display.set_mode([bg_x,bg_y])#設定窗口
pygame.display.set_caption("Dinosour")
####################定義函式####################
def bg_update():
    """更新背景"""
    global bg_roll_x
    bg_roll_x=(bg_roll_x-10)%bg_x
    screen.blit(img,(bg_roll_x-bg_x,0))
    screen.blit(img,(bg_roll_x,0))
def move_dinosour():
    """移動恐龍"""
    global ds_y,jumpState,jumpValue,ds_index
    if jumpState:
        if ds_y >=LIMIT_LOW:
            jumpValue=-jump_height
            if ds_y<=0:
                jumpValue=jump_height
            ds_y+=jumpValue
            jumpValue +=1
            if ds_y <= LIMIT_LOW:
                jumpState=False
                ds_y=LIMIT_LOW
    #計算恐龍圖片編號
    ds_index=(ds_index-1)%len(img_dinosaur)
    screen.blit(img_dinosaur[ds_index],(ds_x,ds_y))
def move_caciti():
    global caciti_x
    caciti_x=(caciti_x-caciti_shift)%(bg_x-100)
    screen.blit(img_cacti,(caciti_x,caciti_y))
####################循環偵測####################
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==KEYDOWN:
            if event.key == pygame.K_SPACE and ds_y <= LIMIT_LOW:
                jumpState=True
    bg_update()
    move_caciti()
    move_dinosour()
    pygame.display.update()