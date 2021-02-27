# 资源路径
chessboard = 'pictures/chessboard.jpg'
piece_black = 'pictures/piece_black.png'
piece_white = 'pictures/piece_white.png'
chess_video = 'videos/棋子音效e.wav'

# 照片像素 540*540 边缘22

# 像素计算
grid_size = 540
# 落子坐标矩阵
chess_arr = []
# 棋盘间距
space = 22
# 棋盘网格数量
cell_num = 15
# 棋盘格子尺寸
cell_size = round((grid_size - space * 2) / (cell_num - 1))

# 1为黑 0为白
flag = 1
# 游戏状态 1进行中 2白赢 3黑赢
game_instance = 1


