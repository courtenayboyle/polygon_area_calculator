
class Rectangle:
    
		#object
		def __init__(self, width, height):
				self.width = width
				self.height = height

		#methods
		def set_width(self, width):
				self.width = width

		def set_height(self, height):
				self.height = height

		def get_area(self):
				return (self.width * self.height)
		
		def get_perimeter(self):
				return ((2 * self.width + 2 * self.height))
		
		#print(get_perimeter)
		def get_diagonal(self):
				return ((self.width ** 2 + self.height ** 2) ** .5)
					
		# Get No of times a shape(sqaure or rectangle) can fit into that shape
		def get_amount_inside(self, other_shape):
				return ((self.width // other_shape.width) * (self.height // other_shape.height))

		def __str__(self):
				return f"Rectangle(width={self.width}, height={self.height})"
		
		#Get * picture
		def get_picture(self):
				if self.height > 50 or self.width > 50:
						return("Too big for picture.")
				if self.width == 0 or self.height == 0:
						return ""
				else: return ((("*" * self.width) + "\n") * self.height)


class Square(Rectangle):
		def __init__(self, side):
				self.width = side
				self.height = side

		#get methods
		def set_side(self, side):
				self.width = side
				self.height = side

		def get_width(self, side):
				self.width = side

		def get_height(self, side):
				self.height = side

		def __str__(self):
				return f"Square(side={self.width})"
				
		def get_picture(self):
				if self.width > 50 or self.height > 50:
						return("Too big for picture.")
				if self.width == 0 or self.height == 0:
						return ""
				else: return ((("*" * self.width) + "\n") * self.height)


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