from 初始化 import *
import pygame
from 主函数 import *

screen_size = (grid_size, grid_size)

# 初始化pygame句柄
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption('五子棋')

# ui资源加载
background = pygame.image.load(chessboard).convert()
black = pygame.image.load(piece_black).convert_alpha()
white = pygame.image.load(piece_white).convert_alpha()

def draw_chess(chess_arr):
    # 棋盘
    screen.blit(background, (0, 0))
    # 棋子
    for x, y, z in chess_arr:
        if z == 0:
            try:
                screen.blit(white, (x * cell_size + space - 16, y * cell_size + space - 16))
            except Exception:
                print(chess_arr, '白棋有问题')
        else:
            try:
                screen.blit(black, (x * cell_size + space - 16, y * cell_size + space - 16))
            except Exception:
                print(chess_arr, '黑棋有问题')

def get_pos(x, y, flag, game_instance):
    xi = int(round((x - space) * 1.0 / cell_size))
    yi = int(round((y - space) * 1.0 / cell_size))
    if 0 <= xi < cell_num and 0 <= yi < cell_num and (xi, yi, 1) not in chess_arr and (xi, yi, 0) not in chess_arr:
        chess_arr.append((xi, yi, flag))
        if check_win(chess_arr, flag):
            if flag == 1:
                game_instance = 3
            else:
                game_instance = 2
        else:
            if flag == 1:
                flag = 0
            else:
                flag = 1
    return flag, game_instance

def draw_result(game_instance):
    myfont = pygame.font.Font('simsun.ttc', 45)
    white = 255, 0, 0
    # 游戏状态 1进行中 2白赢 3黑赢
    if game_instance == 2:
        win_text = "五子连珠，白棋获胜!"
    else:
        win_text = "五子连珠，黑棋获胜!"
    textImage = myfont.render(win_text, True, white)
    height = textImage.get_height()
    weight = textImage.get_width()
    try:
        screen.blit(textImage, ((grid_size - weight) / 2, (grid_size - height) / 2))
    except Exception:
        print('结果输出有问题', weight, height)
