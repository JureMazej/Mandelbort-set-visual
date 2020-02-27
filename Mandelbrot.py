class Mandelbrot:
    def mandel_eq(self, x, y, a=0, b=0, counter=0):  # !! lahko je static !!
        if abs(a) + abs(b) > 100:  # Or some value that tends to infinity
            return counter
        if counter >= 100:  # Doesn't go to infinity
            return 0
        a = a ** 2 - b ** 2 + x  # Real component on x axis
        b = 2 * a * b + y  #Imaginary component y axis
        counter += 1
        return Mandelbrot.mandel_eq(self, x, y, a, b, counter)
