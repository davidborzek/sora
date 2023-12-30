import re
from abc import ABC, abstractmethod


class Unit(ABC):
    """
    Abstract class for size units.
    """

    @abstractmethod
    def to_pixel_relative(self, pixels: int) -> int:
        """
        Converts the unit to a pixel value relative to the given pixel value.

        :param pixels: The pixel value to convert the unit to.
        """
        pass


class Percent(Unit):
    """
    Represents a percentage value.
    """

    pattern = re.compile(r"(\d.*)%")

    def __init__(self, value: float):
        """
        Creates a new percentage value.

        :param value: The percentage value.
        """

        self.value = value
        pass

    def to_pixel_relative(self, pixels: int):
        """
        Converts the percentage to a pixel value relative to the given pixel value.

        :param pixel: The pixel relative to which the percentage should be converted.
        :return: The converted pixel value.
        """

        return int((pixels / 100) * self.value)

    def __str__(self) -> str:
        return f"{self.value}%"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, self.__class__):
            return self.value == __value.value

        return super().__eq__(__value)

    @staticmethod
    def from_string(value: str):
        """
        Creates a new percentage value from a string (e.g. "56%").

        :param value: The string to create the percentage value from.
        :return: The created percentage value.
        """

        if match := Percent.pattern.fullmatch(value):
            return Percent(float(match.group(1)))


class Pixel(Unit):
    """
    Represents a pixel value.
    """

    pattern = re.compile(r"(\d.*)px")

    def __init__(self, value: int):
        """
        Creates a new pixel value.

        :param value: The pixel value.
        """

        self.value = value
        pass

    def __str__(self) -> str:
        return f"{self.value}px"

    def to_pixel_relative(self, _: int):
        """
        Returns the pixel value.

        :param _: Unused pixel value.
        :return: The pixel value.
        """

        return self.value

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, self.__class__):
            return self.value == __value.value

        return super().__eq__(__value)

    @staticmethod
    def from_string(value: str):
        """
        Creates a new pixel value from a string (e.g. "56px").

        :param value: The string to create the pixel value from.
        :return: The created pixel value.
        """

        if match := Pixel.pattern.fullmatch(value):
            return Pixel(int(match.group(1)))


class Coordinates:
    """
    Represents a coordinate pair.
    """

    def __init__(self, x: Unit = Pixel(0), y: Unit = Pixel(0)):
        """
        Creates a new coordinate pair.

        :param x: The x coordinate.
        :param y: The y coordinate.
        """

        self.x = x
        self.y = y

    @staticmethod
    def from_strings(x: str | None, y: str | None):
        """
        Creates a new coordinate pair from two strings (e.g. "56px", "56%").

        :param x: The string to create the x coordinate from.
        :param y: The string to create the y coordinate from.
        :return: The created coordinate pair.
        """

        return Coordinates(
            x=Pixel.from_string(x) or Percent.from_string(x) if x else Pixel(0),
            y=Pixel.from_string(y) or Percent.from_string(y) if y else Pixel(0),
        )

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, self.__class__):
            return self.x == __value.x and self.y == __value.y

        return super().__eq__(__value)

    def __str__(self) -> str:
        return f"({self.x},{self.y})"


class Geometry:
    """
    Represents a geometry of an element.
    """

    def __init__(
        self,
        x: str | None = None,
        y: str | None = None,
        width: str | None = None,
        height: str | None = None,
    ):
        """
        Creates a new geometry.

        :param x: The x coordinate.
        :param y: The y coordinate.
        :param width: The width.
        :param height: The height.
        """

        self.offset = Coordinates.from_strings(x, y)
        self.size = Coordinates.from_strings(width, height)

    def __str__(self) -> str:
        return f"Offset: {self.offset} | Size: {self.size}"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, self.__class__):
            return self.offset == __value.offset and self.size == __value.size

        return super().__eq__(__value)
