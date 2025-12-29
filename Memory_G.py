# # import random

# # # --- מחלקות שחקנים (הורשה) ---
# # class Player:
# #     def __init__(self, name, symbol):
# #         self.name = name
# #         self.symbol = symbol

# #     def get_move(self, board):
# #         raise NotImplementedError("Subclasses must implement get_move")

# # class HumanPlayer(Player):
# #     def get_move(self, board):
# #         while True:
# #             try:
# #                 col = int(input(f"שחקן {self.name} ({self.symbol}), בחר עמודה (0-6): "))
# #                 if 0 <= col <= 6 and board.is_valid_location(col):
# #                     return col
# #                 print("עמודה מלאה או לא חוקית.")
# #             except ValueError:
# #                 print("אנא הכנס מספר בלבד.")

# # class ComputerPlayer(Player):
# #     def get_move(self, board):
# #         print(f"המחשב ({self.name}) חושב...")
# #         valid_moves = [c for c in range(7) if board.is_valid_location(c)]
# #         return random.choice(valid_moves)

# # # --- מחלקת הלוח ---
# # class ConnectFourBoard:
# #     def __init__(self):
# #         self.rows = 6
# #         self.cols = 7
# #         self.grid = [[" " for _ in range(self.cols)] for _ in range(self.rows)]

# #     def print_board(self):
# #         print("\n 0 1 2 3 4 5 6")
# #         for row in self.grid:
# #             print("|" + "|".join(row) + "|")
# #         print("-" * 15)

# #     def is_valid_location(self, col):
# #         return self.grid[0][col] == " "

# #     def drop_piece(self, col, symbol):
# #         for r in range(self.rows-1, -1, -1):
# #             if self.grid[r][col] == " ":
# #                 self.grid[r][col] = symbol
# #                 return r, col

# #     def check_win(self, r, c, s):
# #         # בדיקה פשוטה לכל הכיוונים (אופקי, אנכי, אלכסוני)
# #         directions = [(0,1), (1,0), (1,1), (1,-1)]
# #         for dr, dc in directions:
# #             count = 1
# #             for i in [1, -1]:
# #                 nr, nc = r + dr*i, c + dc*i
# #                 while 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == s:
# #                     count += 1
# #                     nr += dr*i
# #                     nc += dc*i
# #             if count >= 4: return True
# #         return False

# # # --- הרצת המשחק ---
# # def play_terminal_game():
# #     board = ConnectFourBoard()
# #     p1 = HumanPlayer("יוסי", "X")
# #     p2 = ComputerPlayer("רובוט", "O")
    
# #     current_player = p1
# #     while True:
# #         board.print_board()
# #         col = current_player.get_move(board)
# #         row, col = board.drop_piece(col, current_player.symbol)
        
# #         if board.check_win(row, col, current_player.symbol):
# #             board.print_board()
# #             print(f"מזל טוב! {current_player.name} ניצח!")
# #             break
        
# #         current_player = p2 if current_player == p1 else p1

# # if __name__ == "__main__":
# #     play_terminal_game()


# import pygame
# import sys
# import random

# # צבעים
# BLUE = (0, 0, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# YELLOW = (255, 255, 0)

# class Player:
#     def __init__(self, symbol, color):
#         self.symbol = symbol # 1 או 2
#         self.color = color

# class GameGraphics:
#     def __init__(self):
#         pygame.init()
#         self.SQUARESIZE = 100
#         self.width = 7 * self.SQUARESIZE
#         self.height = 7 * self.SQUARESIZE # שורה אחת נוספת לתצוגה
#         self.screen = pygame.display.set_mode((self.width, self.height))
#         self.font = pygame.font.SysFont("arial", 75)

#     def draw_board(self, grid):
#         for c in range(7):
#             for r in range(6):
#                 pygame.draw.rect(self.screen, BLUE, (c*self.SQUARESIZE, r*self.SQUARESIZE+self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE))
#                 color = BLACK
#                 if grid[r][c] == 1: color = RED
#                 elif grid[r][c] == 2: color = YELLOW
#                 pygame.draw.circle(self.screen, color, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), int(r*self.SQUARESIZE+self.SQUARESIZE+self.SQUARESIZE/2)), int(self.SQUARESIZE/2-5))
#         pygame.display.update()

# def play_pygame_game():
#     ui = GameGraphics()
#     grid = [[0 for _ in range(7)] for _ in range(6)]
#     p1 = Player(1, RED)   # שחקן אנושי
#     p2 = Player(2, YELLOW) # מחשב
    
#     turn = 0 # 0 לשחקן 1, 1 לשחקן 2
#     game_over = False

#     while not game_over:
#         ui.draw_board(grid)
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()

#             if event.type == pygame.MOUSEBUTTONDOWN and turn == 0:
#                 posx = event.pos[0]
#                 col = posx // ui.SQUARESIZE
                
#                 # לוגיקת נפילה (במציאות זה היה בתוך Class של Board)
#                 for r in range(5, -1, -1):
#                     if grid[r][col] == 0:
#                         grid[r][col] = 1
#                         turn = 1
#                         break
            
#         # תור המחשב (פשוט מאוד)
#         if turn == 1 and not game_over:
#             pygame.time.wait(500)
#             col = random.randint(0, 6)
#             for r in range(5, -1, -1):
#                 if grid[r][col] == 0:
#                     grid[r][col] = 2
#                     turn = 0
#                     break

# if __name__ == "__main__":
#     play_pygame_game()


