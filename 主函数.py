# coding : utf-8
import random
import pygame
from pygame.locals import *
from 胜负判断 import check_win
from 初始化 import *
from 绘制函数 import *
from pygame.locals import *
import time

if __name__ == '__main__':
    # pygame初始化
    pygame.init()
    pygame.mixer.init()

    # 落子资源加载
    chess_bgm = pygame.mixer.Sound(chess_video)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_instance == 1 and event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                #  获取棋子坐标
                flag, game_instance = get_pos(x, y, flag, game_instance)
                chess_bgm.play()

        # 绘制棋盘
        draw_chess(chess_arr)

        if game_instance != 1:
            draw_result(game_instance)

        pygame.display.update()

