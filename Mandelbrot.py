class Mandelbrot:
    def __init__(self, width, height, size):  # square window
        self.width = width
        self.height = height

        self.minX = -size  # Start of
        self.minY = -size  # Coordinate system

        self.maxX = size  # End of
        self.maxY = size  # Coordintae system

        self.incriment = size / width  # Inkrement of coordinate system

    def mandel_eq(self, x, y, a=0, b=0, counter=0):
        if abs(a) + abs(b) > 20:  # Or some value that tends to infinity
            return False
        if counter > 100:  # Doesn't go to infinity
            return True
        a = a ** 2 - b ** 2 + x  # Real component on x axis
        b = 2 * a * b + y  #Imaginary component y axis
        counter += 1
        return Mandelbrot.mandel_eq(self, x, y, a, b, counter)

    def interations(self):
        x = self.minX
        while x < self.maxX:
            y = self.minY
            while y < self.maxY:
                Mandelbrot.mandel_eq(self, x, y)
                y += self.incriment
            x += self.incriment
