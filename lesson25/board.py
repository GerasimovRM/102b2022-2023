from typing import Tuple, Optional

from bishop import Bishop
from figure import Figure
from king import King
from knight import Knight
from pawn import Pawn
from common import WHITE, BLACK
from queen import Queen
from rook import Rook


class Board:
    def __init__(self):
        self.field = [[None] * 8 for _ in range(8)]
        # WHITE
        for i in range(8):
            self.field[1][i] = Pawn(1, i, WHITE)

        self.field[0][0] = Rook(0, 0, WHITE)
        self.field[0][7] = Rook(0, 7, WHITE)

        self.field[0][1] = Knight(0, 1, WHITE)
        self.field[0][6] = Knight(0, 6, WHITE)

        self.field[0][2] = Bishop(0, 2, WHITE)
        self.field[0][5] = Bishop(0, 5, WHITE)

        self.field[0][4] = King(0, 4, WHITE)
        self.field[0][3] = Queen(0, 3, WHITE)

        # BLACK
        for i in range(8):
            self.field[6][i] = Pawn(6, i, BLACK)

        self.field[7][0] = Rook(7, 0, BLACK)
        self.field[7][7] = Rook(7, 7, BLACK)

        self.field[7][1] = Knight(7, 1, BLACK)
        self.field[7][6] = Knight(7, 6, BLACK)

        self.field[7][2] = Bishop(7, 2, BLACK)
        self.field[7][5] = Bishop(7, 5, BLACK)

        self.field[7][4] = King(7, 4, BLACK)
        self.field[7][3] = Queen(7, 3, BLACK)

        self.current_player_color = WHITE

    # 1 3 5 7 9 11 13 15 -> 0 .. 8
    def print_board(self):
        for i in range(17):
            for j in range(17):
                if i % 2 == 0:
                    print("—", end='')
                elif j % 2 == 0:
                    print("|", end='')
                else:
                    figure = self.get_figure_by_pos(*self.from_print_pos_to_board_pos(i, j))
                    # TODO: после добавления символа фигур, доделать
                    if figure is None:
                        print(" ", end='')
                    elif isinstance(figure, Figure):
                        print(figure.char(), end='')
            print()

    @staticmethod
    def from_print_pos_to_board_pos(x: int, y: int) -> Tuple[int, int]:
        return (x - 1) // 2, (y - 1) // 2

    # TODO: typing
    def get_figure_by_pos(self, i: int, j: int):
        return self.field[i][j]

    @staticmethod
    def from_letters_to_indexes_notation(letters: str) -> Tuple[int, int]:
        let1, let2 = letters.lower()
        pos1 = ord(let1) - ord('a')
        pos2 = int(let2) - 1
        if 7 >= max([abs(pos1), abs(pos2)]) >= 0:
            return pos2, pos1

    def check_figures_on_path(self, x, y, xx, yy):
        if isinstance(self.field[x][y], Knight):
            return True
        if x == xx:
            gg, jj = sorted([yy, y])
            for y_ in range(gg + 1, jj):
                if self.field[x][y_] is not None:
                    return False
        elif y == yy:
            gg, jj = sorted([x, xx])
            for x_ in range(gg + 1, jj):
                if self.field[x_][y] is not None:
                    return False
        else:
            step_x = 1 if xx > x else -1
            step_y = 1 if yy > y else -1
            for i in range(1, xx - x):
                x_, y_ = x + i * step_x, y + i * step_y
                if self.field[x_][y_] is not None:
                    return False
        return True

    def game(self):
        while True:
            board.print_board()
            print(f"Ходит игрок: {self.current_player_color}")
            pos_from = Board.from_letters_to_indexes_notation(input("Возьмите фигуру: "))
            if not pos_from:
                continue
            from_1, from_2 = pos_from
            tmp_figure: Figure | None = self.field[from_1][from_2]
            if tmp_figure and tmp_figure.color != self.current_player_color:
                print('Играй своим цветом')
                continue
            if not tmp_figure:
                print("??")
                continue

            pos_to = Board.from_letters_to_indexes_notation(input("Поставьте фигуру: "))
            if not pos_to:
                continue
            to_1, to_2 = pos_to

            if from_1 == to_1 and from_2 == to_2:
                print('Так ходить нельзя')
                continue

            field_for_move: Figure | None = self.field[to_1][to_2]
            if field_for_move and field_for_move.color == self.current_player_color:
                print('Нельзя есть своих')
                continue

            if field_for_move is None:
                if not tmp_figure.can_move(to_1, to_2):
                    print('Так ходить нельзя')
                    continue
            else:
                if not tmp_figure.can_take(to_1, to_2):
                    print('Так брать нельзя')
                    continue

            if not self.check_figures_on_path(from_1, from_2, to_1, to_2):
                print('на пути мешаются фигуры')
                continue

            self.field[from_1][from_2] = None
            self.field[to_1][to_2] = tmp_figure
            tmp_figure.set_position(to_1, to_2)

            self.current_player_color = BLACK if self.current_player_color == WHITE else WHITE


board = Board()
board.game()
