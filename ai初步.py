from 初始化 import *
# 还非常不成熟
# 棋型的评估分数
shape_score = [
                (50, (0, 1, 1, 0, 0)),
               (50, (0, 0, 1, 1, 0)),
               (200, (1, 1, 0, 1, 0)),
               (500, (0, 0, 1, 1, 1)),
               (500, (1, 1, 1, 0, 0)),
               (5000, (0, 1, 1, 1, 0)),
               (5000, (0, 1, 0, 1, 1, 0)),
               (5000, (0, 1, 1, 0, 1, 0)),
               (5000, (1, 1, 1, 0, 1)),
               (5000, (1, 1, 0, 1, 1)),
               (5000, (1, 0, 1, 1, 1)),
               (5000, (1, 1, 1, 1, 0)),
               (5000, (0, 1, 1, 1, 1)),
               (50000, (0, 1, 1, 1, 1, 0)),
               (99999999, (1, 1, 1, 1, 1))
]

# 评估函数
def evalution(turn_ai):

    total_score = 0

    if turn_ai:
        my_chess = chess1
        enemy_chess = chess2
    else:
        my_chess = chess2
        enemy_chess = chess1

    # 分数记录表
    score_all_arr = []
    my_score = 0


def cal_score(m, n, x_pos, y_pos, my_chess, enemy_chess, score_all_arr):
    add_score = 0

    max_score_shape = (0, None)

    for item in score_all_arr:
        for pt in item[1]:
