from 初始化 import *


def get_one_dire_num(lx, ly, dx, dy, m):
    tx = lx
    ty = ly
    s = 0
    while True:
        tx += dx
        ty += dy
        if tx < 0 or tx >= cell_num or ty < 0 or ty >= cell_num or m[ty][tx] == 0:
            return s
        s += 1

def check_win(chess_arr, flag):
    m = [[0] * 15 for i in range(cell_num)]
    for x, y, z in chess_arr:
        if z == flag:
            m[y][x] = 1
    # 最后一个棋子的位置
    lx = chess_arr[-1][0]
    ly = chess_arr[-1][1]
    dire_arr = [
        [(-1, 0), (1, 0)],
        [(0, -1), (0, 1)],
        [(-1, -1), (1, 1)],
        [(-1, 1), (1, -1)]
    ]
    for dire1, dire2 in dire_arr:
        dx, dy = dire1
        num1 = get_one_dire_num(lx, ly, dx, dy, m)
        dx, dy = dire2
        num2 = get_one_dire_num(lx, ly, dx, dy, m)
        if num1 + num2 + 1 >= 5:
            return True
    return False