#!/usr/bin/python3

"""Defines a square model from rectangle
The rectangle c lass is also the super classof square"""

from models.rectangle import Rectangle
"""Import Rectangle from models/rectangle.py"""

class Square(Rectangle):
    """A square i s rectangle with width == height"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance variables"""
        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        """return size  == width"""
        return self.width

    @size.setter
    def size(self, val):
        """Set val as width and height"""
        self.width = val
        self.height = val

    def __str__(self):
        """Overloading of rectangles representation"""
        name = type(self).__name__
        tmp = super().__str__()
        """Slicing the tmp to remove height"""
        rep = [:tmp.rfind('/')]
        return rep

    def update(self, *args, **kwargs):
        """Update square attributes"""
        n = len(args)
        if n:
            if n>1:
                 args = list(args)
                 args.insert(1, args[1])
            return super().update(*args)
         if kwargs != {}:
             if 'size' in kwargs:
                 """Check if there's need to update size"""
                 _w = kwargs['size']
                 """save size into temp variable and delete size from keyworded args"""
                 del kwargs['size']
                 """set width and height as a keyword in kwargs to have same value as size"""
                 kwargs['width'] = _w
                 kwargs['height'] = _w
                 """Update the super method"""
                 super().update(**kwargs)

    def to_dictionary(self):
        """Provides a 'dict' representtion of the object"""
        return {
             "id": self.id,
             "size": self.size,
            "x": self.x, "y": self.y
        }

    def to_csv_str(self):
        """Provides a 'dict' representtion of the object"""
        fmt = "{},{},{},{}"
        return fmt.format(*(
            self.id, self.size,
             self.x, self.y
        ))
