import unittest

from sora import geometry


class TestPercent(unittest.TestCase):
    def test_should_parse_string(self):
        percent = geometry.Percent.from_string("22%")
        self.assertEqual(percent.value, 22)

    def test_should_return_none_for_invalid_string(self):
        percent = geometry.Percent.from_string("invalid")
        self.assertIsNone(percent)

    def test_should_format_string(self):
        self.assertEqual(str(geometry.Percent(22)), "22%")

    def test_to_pixel(self):
        pixel = geometry.Percent(50).to_pixel_relative(500)
        self.assertEqual(pixel, 250)

    def test_to_pixel_negative(self):
        pixel = geometry.Percent(50).to_pixel_relative(-500)
        self.assertEqual(pixel, -250)


class TestPixel(unittest.TestCase):
    def test_should_parse_string(self):
        percent = geometry.Pixel.from_string("100px")
        self.assertEqual(percent.value, 100)

    def test_should_return_none_for_invalid_string(self):
        percent = geometry.Pixel.from_string("invalid")
        self.assertIsNone(percent)

    def test_should_format_string(self):
        self.assertEqual(str(geometry.Pixel(100)), "100px")

    def test_to_pixel(self):
        pixel = geometry.Pixel(50).to_pixel_relative(0)
        self.assertEqual(pixel, 50)


class TetsCoordinates(unittest.TestCase):
    def test_should_parse_string(self):
        coordinates = geometry.Coordinates.from_strings("100px", "30%")

        self.assertIsInstance(coordinates.x, geometry.Pixel)
        self.assertEqual(coordinates.x.value, 100)

        self.assertIsInstance(coordinates.y, geometry.Percent)
        self.assertEqual(coordinates.y.value, 30)

    def test_should_parse_string_with_none(self):
        coordinates = geometry.Coordinates.from_strings(None, None)

        self.assertIsInstance(coordinates.x, geometry.Pixel)
        self.assertEqual(coordinates.x.value, 0)

        self.assertIsInstance(coordinates.y, geometry.Pixel)
        self.assertEqual(coordinates.y.value, 0)

    def test_should_format_string(self):
        coordinates = geometry.Coordinates.from_strings("100px", "30%")
        self.assertEqual(str(coordinates), "(100px,30.0%)")


class TestGeometry(unittest.TestCase):
    def test_init(self):
        g = geometry.Geometry("100px", "30%", "50px", "40%")

        self.assertEqual(
            g.offset, geometry.Coordinates(geometry.Pixel(100), geometry.Percent(30))
        )

        self.assertEqual(
            g.size, geometry.Coordinates(geometry.Pixel(50), geometry.Percent(40))
        )

    def test_init_with_none(self):
        g = geometry.Geometry(None, None, None, None)

        self.assertEqual(
            g.offset, geometry.Coordinates(geometry.Pixel(0), geometry.Pixel(0))
        )

        self.assertEqual(
            g.size, geometry.Coordinates(geometry.Pixel(0), geometry.Pixel(0))
        )

    def test_should_format_string(self):
        g = geometry.Geometry("100px", "30%", "50px", "40%")
        self.assertEqual(str(g), "Offset: (100px,30.0%) | Size: (50px,40.0%)")


if __name__ == "__main__":
    unittest.main()
