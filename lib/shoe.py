#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size
        self.condition = "Used"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"


class TestShoe:
    def test_has_brand_and_size(self):
        stan_smith = Shoe("Adidas", 9)

    def test_requires_int_size(self):
        stan_smith = Shoe("Adidas", 9)
        captured_out = self.capture_output(stan_smith.size, "not an integer")
        assert captured_out == "size must be an integer\n"

    def test_can_cobble(self):
        stan_smith = Shoe("Adidas", 9)
        captured_out = self.capture_output(stan_smith.cobble)
        assert captured_out == "Your shoe is as good as new!\n"

    def test_cobble_makes_new(self):
        stan_smith = Shoe("Adidas", 9)
        stan_smith.cobble()