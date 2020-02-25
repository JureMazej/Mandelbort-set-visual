class Mandelbrot:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def mandel_eq(self, x, y, a=0, b=0, counter=0):
        if abs(a) + abs(b) > 20:
            return False
        if counter > 100:
            return True
        a = a ** 2 - b ** 2 + x
        b = 2 * a * b + y
        counter += 1
        return Mandelbrot.mandel_eq(self, x, y, a, b, counter)
