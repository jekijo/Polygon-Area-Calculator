class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, n):
        self.width = n
        
    def set_height(self, n):
        self.height = n
        
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self): 
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        if (self.height > 50) or (self.width > 50):
            return "Too big for picture."
        else:
            p = ''
            for i in range(self.height):
                p += ('*' * self.width) + '\n'
            return p
            
    def get_amount_inside(self, shape):
        w = self.width
        t = 0
        if (shape.width>self.width) or (shape.height>self.height):
            return t
        else:
            while (w-shape.width) >= 0:
                t += self.height/shape.height
                w -= shape.width
            return int(t)    
    
class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
        self.side = side
        
    def __str__(self):
        return f'Square(side={self.side})'
    
    def set_side(self, n):
        self.side = n
        self.width = n
        self.height = n
        
    def set_width(self, n):
        self.width = n
        self.height = n
        self.side = n
        
    def set_height(self, n):
        self.width = n
        self.height = n
        self.side = n
