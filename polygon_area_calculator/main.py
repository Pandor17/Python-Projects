class Rectangle:
    def set_width(self, width:int):
        self.__width = width

    def set_height(self, height:int):
        self.__height = height

    def get_width(self)-> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height

    def __init__(self, width:int, height:int):
        self.set_width(width)
        self.set_height(height)

    def get_area(self)-> float:
        area = self.get_width() * self.get_height()
        return area

    def get_perimeter(self)-> int:
        perimeter = self.get_width() * 2 + self.get_height() * 2
        return perimeter

    def get_diagonal(self)-> float:
        diagonal = (self.get_width() ** 2 + self.get_height() ** 2) ** .5
        return diagonal

    def get_picture(self)->str:
        shape = ""
        if not self.get_height() > 50 and not self.get_width() > 50:
            for altura in range(self.get_height()):
                fila = ""
                for anchura in range(self.get_width()):
                    fila += "*"
                shape += fila
                shape += "\n"
        else:
            return "Too big for picture."
        return shape

    def get_amount_inside(self, other: "Rectangle")-> int:
        if not isinstance(other, Rectangle):
            raise TypeError("El parámetro debe ser un objeto de tipo Rectangle o Square")
        repeticiones_al_ancho = int(self.get_width() / other.get_width())
        repeticiones_al_largo = int(self.get_height() / other.get_height())
        return repeticiones_al_ancho * repeticiones_al_largo

    def __str__(self)->str:
        return f"Rectangle(width={self.get_width()}, height={self.get_height()})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)

    def get_side(self):
        return super().get_height()

    def __str__(self):
        return f"Square(side={self.get_side()})"

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))