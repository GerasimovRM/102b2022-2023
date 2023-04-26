from common import WHITE
from figure import Figure


class Bishop(Figure):
    def can_move(self, xx: int, yy: int) -> bool:
        if super().can_move(xx, yy):
            if abs(xx - self.x) != abs(yy - self.y):
                return False
            return True
        return False

    def can_take(self, xx: int, yy: int):
        return self.can_move(xx, yy)

    def char(self):
        return "♗" if self.color == WHITE else "♝"