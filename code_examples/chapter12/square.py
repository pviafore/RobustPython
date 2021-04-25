class Rectangle:
    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width
    
    def set_width(self, new_width):
        self._width = new_width

    def set_height(self, new_height):
        self._height = new_height

    def get_width(self) -> int:
        return self._width
    
    def get_height(self) -> int:
            return self._height

class Square(Rectangle):
    def __init__(self, length: int):
        super().__init__(length, length)

    def set_side_length(self, new_length):
        super().set_width(new_length)
        super().set_height(new_length)

    def set_width(self, new_width):
        self.set_side_length(new_width)

    def set_height(self, new_height):
        self.set_side_length(new_height)

def double_width(rectangle: Rectangle):
    old_height = rectangle.get_height()
    rectangle.set_width(rectangle.get_width() * 2)
    # check that the height is unchanged
    assert rectangle.get_height() == old_height

try:
    double_width(Square(5))
    raise RuntimeError("This should not pass")
except AssertionError:
    print("Expected assert")
