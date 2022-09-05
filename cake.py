import math

class Cake:
    def __init__(self, portion, price_per_person, box, gf):
        self.portion = portion
        self.price_per_person = price_per_person
        self.box = box
        self.gf = gf

    SIDE_OF_ONE_SQUARE_PORTION = 5

    @staticmethod
    def calculate_layer_ratios(portion):           # pl: oblicz podział pola na warstwy
        layer_ratio = [0, 0, 0]
        if portion < 31:
            layer_ratio[0] = 1
        elif 31 <= portion <= 50:
            layer_ratio[0] = 0.65
            layer_ratio[1] = 0.35
        elif 51 <= portion < 76:
            layer_ratio[0] = 0.465
            layer_ratio[1] = 0.32
            layer_ratio[2] = 0.24
        return layer_ratio

    def price_calc(self):  # Price for the cake
        if self.gf == 1:
            price = self.portion * (self.price_per_person + 2)
        else:
            price = self.portion * self.price_per_person

        box_price = 0

        if self.box == 1:
            if self.portion <= 20:
                box_price = 7
            elif self.portion <= 30:
                box_price = 10
            elif self.portion <= 40:
                box_price = 15
            elif self.portion > 40:
                box_price = 20
            price += box_price

        return [price, box_price]

    def round_calc(self):  # Round cake size calculator
        ONE_PORTION_FIELD = 22.8
        layer_ratios = self.calculate_layer_ratios(self.portion)
        round_cake_field = ONE_PORTION_FIELD * self.portion
        pi = round(math.pi, 2)

        def calculate_d(round_cake_field, layer_ratio):
            return round(2 * math.sqrt(round_cake_field * layer_ratio / pi))

        diameters = []

        for layer_ratio in layer_ratios:
            diameters.append(calculate_d(round_cake_field, layer_ratio))

        return diameters

    def calculate_one_portion_field(self, side):  # With this function you can set side size of one portion
        return side ** 2  # Field size of portion for one person

    def square_calc(self):
        cake_size = self.calculate_one_portion_field(self.SIDE_OF_ONE_SQUARE_PORTION) * self.portion
        layer_ratios = self.calculate_layer_ratios(self.portion)

        def calculate_side(cake_size, layer_ratio):
            return round(math.sqrt(cake_size * layer_ratio))

        square_sides = []

        for layer_ratio in layer_ratios:
            square_sides.append(calculate_side(cake_size, layer_ratio))

        return square_sides

    def rectangle_calc(self):
        cake_size = self.calculate_one_portion_field(self.SIDE_OF_ONE_SQUARE_PORTION) * self.portion
        layer_ratios = self.calculate_layer_ratios(self.portion)

        def calculate_side_a(cake_size, layer_ratio):
            return round(math.sqrt((cake_size * layer_ratio) / 0.7))

        def calculate_side_b(cake_side_a_1):
            return round(cake_side_a_1 * 0.7)

        cake_sides_a = []
        cake_sides_b = []

        for layer_ratio in layer_ratios:
            cake_side_a = calculate_side_a(cake_size, layer_ratio)
            cake_side_b = calculate_side_b(cake_side_a)
            cake_sides_a.append(cake_side_a)
            cake_sides_b.append(cake_side_b)

        return cake_sides_a, cake_sides_b
