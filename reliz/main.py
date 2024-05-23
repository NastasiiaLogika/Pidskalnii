import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CROSS_WIDTH = 15
SPACE = SQUARE_SIZE // 4

BG_COLOR = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
CIRCLE_COLOR = (255, 0, 0)
CROSS_COLOR = (0, 0, 255)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
win.fill(BG_COLOR)

board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def draw_grid():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(win, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(win, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(win, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), CIRCLE_RADIUS)
            elif board[row][col] == 'X':
                pygame.draw.line(win, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(win, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def check_winner(piece):
    for row in range(BOARD_ROWS):
        if board[row][0] == piece and board[row][1] == piece and board[row][2] == piece:
            return True
    for col in range(BOARD_COLS):
        if board[0][col] == piece and board[1][col] == piece and board[2][col] == piece:
            return True
    if board[0][0] == piece and board[1][1] == piece and board[2][2] == piece:
        return True
    if board[0][2] == piece and board[1][1] == piece and board[2][0] == piece:
        return True
    return False

turn = 'X'
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE
            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = turn
                if check_winner(turn):
                    game_over = True
                turn = 'O' if turn == 'X' else 'X'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                turn = 'X'
                game_over = False
                board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
                win.fill(BG_COLOR)

    win.fill(BG_COLOR)
    draw_grid()
    draw_figures()
    if game_over:
        pygame.time.wait(3000)
        turn = 'X'
        game_over = False
        board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        win.fill(BG_COLOR)
    pygame.display.update()