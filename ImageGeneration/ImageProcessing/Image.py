from cmath import pi
import RGBA
import PIL.Image


class Image:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pixels = list()

        for i in range(width * height):
            self.pixels.append(RGBA.RGBA())

    def clear(self, r: int, g: int, b: int, a: int):
        for pixel in self.pixels:
            pixel.set(r, g, b, a)

    def save(self, filename) -> bool:
        buffer = list()

        for pixel in self.pixels:
            buffer.append(pixel.pixel)

        image = PIL.Image.new("RGBA", (self.width, self.height))
        image.putdata(buffer)

        try:
            image.save(filename)
        except IOError:
            return False
        return True

    def set_pixel(self, x, y, r, g, b, a=255):
        index = (y * self.width) + x
        try:
            self.pixels[index].set(r, g, b, a)
        except:
            print("out of range")

    def get_pixel(self, x, y):
        index = (y * self.width) + x
        try:
            pixel = self.pixels[index]
            return pixel.red(), pixel.green(), pixel.blue(), pixel.alpha()
        except:
            print("out of range")

    def load(self, filename):
        try:
            with PIL.Image.open(filename) as im:
                self.width = im.size[0]
                self.height = im.size[1]
                # remove old pixels and load from pile
                self.pixels = []
                for pixel in im.getdata():
                    self.pixels.append(
                        RGBA.RGBA(pixel[0], pixel[1], pixel[2], pixel[3])
                    )

        except IOError:
            return False
        return True

    def get_average_rgba(self):
        average_pixel = int(sum(x.pixel for x in self.pixels) / len(self.pixels))
        new_pixel = RGBA.RGBA.from_pixel(average_pixel)

        r = new_pixel.red()
        g = new_pixel.green()
        b = new_pixel.blue()
        a = new_pixel.alpha()

        return r, g, b, a
