from models.base import Base
"""Defines the rectangle models
inherited base class"""

class Rectangle(Base):
    """the parent class is Base in models/base.py"""
    """
    The init method has 4 args:
    @arg x is printing offset on the x axis
    @arg y is printing offset on the y axis
    @arg width is the width of the rectangle
    @arg height is the height of the rectangle
    @arg id is the unique id of the rectangle set by base class
    """
    def __init__(self, width, height, x =0, y=0, id=None):
         super().__init__(id)
         self.validate_size("width", width)
         self.validate_size("height", height)
         self.validate_size("x", x, 0)
         self.validate_size("y", y, 0)
         self.__width = width
         self.__height = height
         self.__x = x
         self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return  self.__y

    @width.setter
    def width(self, val):
        self.validate_size("width", val)
        self.__width = val

    @height.setter
    def height(self, val):
        self.validate_size("height", val)
        self.__height = val

    @x.setter
    def x(self, val):
        self.validate_size("x", val, 0)
        self.__x = val

    @y.setter
    def y(self, val):
        self.validate_size("y", val, 0)
        self.__y = val

    def area(self):
        """returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """print a rectangle of # """
        y_offset = '\n' *self.y
        x_offset = '' * self.x
        print (y_offset, end='')
        for i in range(self.height):
            print(x_offset, "#" * self.width, sep= '')

    def __str__(self):
        """Return the  string representation of the class"""
        name = type(self).__name__
        rep = f"{name} ({self.id}) {self.x}/{self.y} - {self.width}/{self.height} "
        return rep

    def update(self, *args, **kwargs):
        """ Update some/all attributes of the rectangle """
        n = len(args)
        if n>0:
            self.id = args[0]
        if n>1:
            self.width = args[1]
        if n>2:
            self.height = args[2]
        if n>3:
            self.x = args[3]
        if n>4:
            self.y = args[4]

        """Using key/value arguments (kwargs)"""
        checks = ("id", "width", "height", "x", "y")
        for key,val in kwargs.items():
            if key in checks:
                self.__setattr__(key, val)
            else:
                raise KeyError(f"Invalid keyword argument {key}")

