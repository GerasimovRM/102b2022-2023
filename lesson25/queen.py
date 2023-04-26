from bishop import Bishop
from common import WHITE
from rook import Rook


class Queen(Rook, Bishop):
    def can_move(self, xx, yy):
        return Rook.can_move(self, xx, yy) or Bishop.can_move(self, xx, yy)

    def can_take(self, xx, yy):
        return self.can_move(xx, yy)

    def char(self):
        return "♕" if self.color == WHITE else "♛"


if __name__ == "__main__":
    q = Queen(1, 1, WHITE)
    print(q.can_move(2, 3))
    st = 'dfg'
    st.upper()  # str.upper(st)
