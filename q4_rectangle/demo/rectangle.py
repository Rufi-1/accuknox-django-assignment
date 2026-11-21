class Rectangle:
    # needs length and width (both ints) to create an object
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # __iter__ makes the object iterable (so we can use a for loop on it)
    # first we give the length, then the width
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}
