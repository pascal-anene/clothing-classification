{
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Inheritance Exercise Clothing\n",
                "\n",
                "The following code contains a Clothing parent class and two children classes: Shirt and Pants.\n",
                "\n",
                "Your job is to code a class called Blouse. Read through the code and fill out the TODOs. Then check your work with the unit tests at the bottom of the code."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "class Clothing:\n",
                "\n",
                "    def __init__(self, color, size, style, price):\n",
                "        self.color = color\n",
                "        self.size = size\n",
                "        self.style = style\n",
                "        self.price = price\n",
                "        \n",
                "    def change_price(self, price):\n",
                "        self.price = price\n",
                "        \n",
                "    def calculate_discount(self, discount):\n",
                "        return self.price * (1 - discount)\n",
                "        \n",
                "class Shirt(Clothing):\n",
                "    \n",
                "    def __init__(self, color, size, style, price, long_or_short):\n",
                "        \n",
                "        Clothing.__init__(self, color, size, style, price)\n",
                "        self.long_or_short = long_or_short\n",
                "    \n",
                "    def double_price(self):\n",
                "        self.price = 2*self.price\n",
                "    \n",
                "class Pants(Clothing):\n",
                "\n",
                "    def __init__(self, color, size, style, price, waist):\n",
                "        \n",
                "        Clothing.__init__(self, color, size, style, price)\n",
                "        self.waist = waist\n",
                "        \n",
                "    def calculate_discount(self, discount):\n",
                "        return self.price * (1 - discount / 2)\n",
                "    \n",
                "# TODO: Write a class called Blouse, that inherits from the Clothing class\n",
                "# and has the the following attributes and methods:\n",
                "#   attributes: color, size, style, price, country_of_origin\n",
                "#     where country_of_origin is a string that holds the name of a \n",
                "#     country\n",
                "#\n",
                "#   methods: triple_price, which has no inputs and returns three times\n",
                "#     the price of the blouse\n",
                "#\n",
                "#\n",
                "\n",
                "# TODO: Add a method to the clothing class called calculate_shipping.\n",
                "#   The method has two inputs: weight and rate. Weight is a float\n",
                "#   representing the weight of the article of clothing. Rate is a float\n",
                "#   representing the shipping weight. The method returns weight * rate\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Unit tests to check your solution\n",
                "\n",
                "import unittest\n",
                "\n",
                "class TestClothingClass(unittest.TestCase):\n",
                "    def setUp(self):\n",
                "        self.clothing = Clothing('orange', 'M', 'stripes', 35)\n",
                "        self.blouse = Blouse('blue', 'M', 'luxury', 40, 'Brazil')\n",
                "        self.pants = Pants('black', 32, 'baggy', 60, 30)\n",
                "        \n",
                "    def test_initialization(self): \n",
                "        self.assertEqual(self.clothing.color, 'orange', 'color should be orange')\n",
                "        self.assertEqual(self.clothing.price, 35, 'incorrect price')\n",
                "        \n",
                "        self.assertEqual(self.blouse.color, 'blue', 'color should be blue')\n",
                "        self.assertEqual(self.blouse.size, 'M', 'incorrect size')\n",
                "        self.assertEqual(self.blouse.style, 'luxury', 'incorrect style')\n",
                "        self.assertEqual(self.blouse.price, 40, 'incorrect price')\n",
                "        self.assertEqual(self.blouse.country_of_origin, 'Brazil', 'incorrect country of origin')\n",
                "\n",
                "    def test_calculateshipping(self):\n",
                "        self.assertEqual(self.clothing.calculate_shipping(.5, 3), .5 * 3,\\\n",
                "         'Clothing shipping calculation not as expected') \n",
                "\n",
                "        self.assertEqual(self.blouse.calculate_shipping(.5, 3), .5 * 3,\\\n",
                "         'Clothing shipping calculation not as expected') \n",
                "    \n",
                "tests = TestClothingClass()\n",
                "\n",
                "tests_loaded = unittest.TestLoader().loadTestsFromModule(tests)\n",
                "\n",
                "unittest.TextTestRunner().run(tests_loaded)"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.9.1"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}
