from typeguard import typechecked
from rectangulo_cuadrado_herencia import Rectangle
from punto import Point


@typechecked
class Cuadrado(Rectangle):
    def __init__(self, side:int, punto:Point):
        super().__init__(side, side)
        self.__punto = punto

    @property
    def side(self):
        self.width = self.side

    def __repr__(self):
        return f"{self.__class__.__name__}({self.side})"
