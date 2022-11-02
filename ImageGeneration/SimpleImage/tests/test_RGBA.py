import unittest
import sys

sys.path.append("/home/s5223748/UNI/SOFTWARE_ANIMATIOŅ/SimpleImage/")

import RGBA


class TestRGBA(unittest.TestCase):
    def test_ctor(self):
        pixel = RGBA.RGBA()
        r, g, b, a = pixel.get_rgba()
        self.assertEqual(r, 0)
        self.assertEqual(g, 0)
        self.assertEqual(b, 0)
        self.assertEqual(a, 255)
