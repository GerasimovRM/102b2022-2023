from common import WHITE
from figure import Figure


class Rook(Figure):
    def can_move(self, xx, yy) -> bool:
        if super().can_move(xx, yy):
            if self.x == xx and self.y != yy:
                return True
            elif self.x != xx and self.y == yy:
                return True
            return False
        return False

    def can_take(self, xx, yy):
        return self.can_move(xx, yy)

    def char(self):
        return "♖" if self.color == WHITE else "♜"