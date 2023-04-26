from common import WHITE, BLACK
from figure import Figure


class Pawn(Figure):
    def can_move(self, xx, yy) -> bool:
        if super().can_move(xx, yy):
            if self.y != yy:
                return False
            if (self.x + 1 == xx and self.color == WHITE) or \
                    (self.x - 1 == xx and self.color == BLACK):
                return True
            if ((self.x == 1 and self.color == WHITE and self.x + 2 == xx) or
                (self.x == 6 and self.color == BLACK and self.x - 2 == xx)):
                return True
            return False
        return False

    def can_take(self, xx, yy):
        if (self.x + 1 == xx and (self.y + 1 == yy or self.y - 1 == yy) and self.color == WHITE) or \
                (self.x - 1 == xx and (self.y + 1 == yy or self.y - 1 == yy) and self.color == BLACK):
            return True
        if ((self.x == 1 and self.color == WHITE and self.x + 2 == xx) or
            (self.x == 6 and self.color == BLACK and self.x - 2 == xx)):
            return True
        return False

    def char(self):
        return "♙" if self.color == WHITE else "♟"


