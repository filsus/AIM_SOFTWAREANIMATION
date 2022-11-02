#!/user/bin/env python
import sys

# setting path make sure you are in the directory below /SimpleImage
sys.path.insert(0, "./SimpleImage")
# sys.path.append("/home/s5223748/UNI/SOFTWARE_ANIMATIOŅ/ImageGeneration/SimpleImage")
import Image
import random
import math


def splat(image, r, g, b, splat_size):
    x = random.randint(0, image.width - 1)
    y = random.randint(0, image.height - 1)
    size = (image.width + image.height) / 10

    for i in range(random.randint(size, size * 5000)):
        alpha = 2 * math.pi * random.random()
        radius = splat_size * math.sqrt(random.random())
        rx = int(radius * math.cos(alpha))
        ry = int(radius * math.sin(alpha))
        image.set_pixel(x + rx, y + ry, r, g, b)


def create_images(number, width, height):
    for frame in range(0, number):
        image = Image.Image(width, height)
        image.clear(255, 255, 255, 255)

        for i in range(0, 2):
            r = random.randint(0, 0)
            g = random.randint(0, 0)
            b = random.randint(0, 255)

            for _ in range(1, random.randint(1, 10)):
                splat(image, r, g, b, splat_size=random.randint(1, 20))

        image.save(f"image.{frame:04}.png")


if __name__ == "__main__":
    create_images(10, width=250, height=250)
