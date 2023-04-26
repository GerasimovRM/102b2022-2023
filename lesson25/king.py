from common import WHITE
from figure import Figure


class King(Figure):
    def char(self):
        return "♔" if self.color == WHITE else "♚"

    def can_move(self, xx: int, yy: int) -> bool:
        if super().can_move(xx, yy):
            if max([abs(self.x - xx), abs(self.y - yy)]) == 1:
                return True
        return False

    def can_take(self, xx: int, yy: int) -> bool:
        return self.can_move(xx, yy)

