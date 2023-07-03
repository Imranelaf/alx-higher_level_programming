#!/usr/bin/python3

'''
This module defines the Rectangle class.
'''


class Rectangle:
    '''
    This class represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__: Initializes a new rectangle instance.
        width: Getter method for the width attribute.
        width.setter: Setter method for the width attribute.
        height: Getter method for the height attribute.
        height.setter: Setter method for the height attribute.
    '''

    def __init__(self, width=0, height=0):
        '''
        Initializes a rectangle instance with the specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Sets the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Sets the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value
