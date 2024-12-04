class Shape:
    def area(self, length, width=None):
        if width is None:
            return 3.14 * length * length
        else:
            return length * width
shape = Shape()
circle_area = shape.area(8)
print(f"Area of the circle: {circle_area}")
rectangle_area = shape.area(5, 3)
print(f"Area of the rectangle: {rectangle_area}")
