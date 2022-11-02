#!/usr/bin/env python

from tkinter.tix import Tree
import unittest

import sys

# setting path
sys.path.append("/home/s5223748/UNI/SOFTWARE_ANIMATIOŅ/SimpleImage/")

# importing
from Image import *


class TestImage(unittest.TestCase):
    def test_ctor(self):
        image = Image(128, 128)
        self.assertEqual(image.width, 128)
        self.assertEqual(image.height, 128)
        self.assertEqual(len(image.pixels), 128 * 128)

    def test_clear(self):
        image = Image(128, 128)
        image.clear(255, 128, 32, 255)
        for pixel in image.pixels:
            r, g, b, a = pixel.get_rgba()
            self.assertEqual(r, 255)
            self.assertEqual(g, 128)
            self.assertEqual(b, 32)
            self.assertEqual(a, 255)

    def test_save(self):
        image = Image(1024, 720)
        image.clear(125, 20, 222, 255)
        self.assertTrue(image.save("test.png"))

    def test_load(self):
        image = Image(100, 100)
        image.clear(255, 128, 0, 255)
        image.save("testLoad.png")
        image2 = Image(0, 0)
        image2.load("testLoad.png")
        self.assertEqual(image2.width, 100)
        self.assertEqual(image2.height, 100)
        for pixel in image2.pixels:
            self.assertEqual(pixel.red(), 255)
            self.assertEqual(pixel.green(), 128)
            self.assertEqual(pixel.blue(), 0)
            self.assertEqual(pixel.alpha(), 255)

    def test_set_get(self):
        image = Image(500, 500)
        image.clear(255, 255, 255, 255)

        for x in range(0, image.width):
            image.set_pixel(x, 250, 255, 0, 0)

        self.assertTrue(image.save("redsquare.png"))
        for y in range(image.height):
            for x in range(image.width):
                r, g, b, a = image.get_pixel(x, y)
                if y == 250:
                    # red?
                    self.assertEqual(r, 255)
                    self.assertEqual(g, 0)
                    self.assertEqual(b, 0)
                    self.assertEqual(a, 255)
                else:
                    # white?
                    self.assertEqual(r, 255)
                    self.assertEqual(g, 255)
                    self.assertEqual(b, 255)
                    self.assertEqual(a, 255)

    def test_get_average_rgba(self):
        pass

    def test_get_average_hsv(self):
        pass


TestImage().test_ctor()
TestImage().test_clear()
TestImage().test_save()
TestImage().test_set_get()
