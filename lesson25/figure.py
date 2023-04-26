from abc import abstractmethod


class Figure:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

    def can_move(self, xx: int, yy: int) -> bool:
        if xx < 0 or xx > 7:
            return False
        if yy < 0 or yy > 7:
            return False
        return True

    @abstractmethod
    def can_take(self, xx: int, yy: int) -> bool:
        pass

    @abstractmethod
    def char(self) -> str:
        pass

    def set_position(self, xx: int, yy: int):
        self.x = xx
        self.y = yy
