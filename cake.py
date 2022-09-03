import math

class Cake:
    def __init__(self, portion, price_per_person, box, gf):
        self.portion = portion
        self.price_per_person = price_per_person
        self.box = box
        self.gf = gf

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

    def calculate_multiplier(self, portion):
        multiplier = {
            "layer1": 0,
            "layer2": 0,
            "layer3": 0}
        if portion < 31:
            multiplier["layer1"] = 1
        elif 31 <= portion <= 50:
            multiplier["layer1"] = 0.65
            multiplier["layer2"] = 0.35
        elif 51 <= portion < 76:
            multiplier["layer1"] = 0.465
            multiplier["layer2"] = 0.32
            multiplier["layer3"] = 0.24
        return multiplier

    def round_calc(self):  # Round cake size calculator
        ONE_PORTION_FIELD = 22.8
        multiplier = self.calculate_multiplier(self.portion)
        round_cake_field = ONE_PORTION_FIELD * self.portion
        pi = round(math.pi, 2)

        d_1 = round(2 * math.sqrt(round_cake_field * multiplier["layer1"] / pi))
        d_2 = round(2 * math.sqrt(round_cake_field * multiplier["layer2"] / pi))
        d_3 = round(2 * math.sqrt(round_cake_field * multiplier["layer3"] / pi))

        return [d_1, d_2, d_3]

    def one_portion_field(self, side):  # With this function you can set side size of one portion
        one_portion_field = side ** 2
        return one_portion_field  # Field size of portion for one person

    def square_calc(self):
        cake_size = Cake.one_portion_field(self, 6) * self.portion
        multiplier = self.calculate_multiplier(self.portion)
        cake_side_1 = round(math.sqrt(cake_size * multiplier["layer1"]))
        cake_side_2 = round(math.sqrt(cake_size * multiplier["layer2"]))
        cake_side_3 = round(math.sqrt(cake_size * multiplier["layer3"]))

        return [cake_side_1, cake_side_2, cake_side_3]

    def rectangle_calc(self):
        cake_size = Cake.one_portion_field(self, 6) * self.portion
        multiplier = self.calculate_multiplier(self.portion)
        cake_side_a_1 = round(math.sqrt((cake_size * multiplier["layer1"]) / 0.7))
        cake_side_b_1 = round(cake_side_a_1 * 0.7)
        cake_side_a_2 = round(math.sqrt((cake_size * multiplier["layer2"]) / 0.7))
        cake_side_b_2 = round(cake_side_a_2 * 0.7)
        cake_side_a_3 = round(math.sqrt((cake_size * multiplier["layer3"]) / 0.7))
        cake_side_b_3 = round(cake_side_a_3 * 0.7)

        # if self.portion <= 25:  # one layer
        #     cake_side_a_1 = round(math.sqrt(cake_size / 0.7))
        #     cake_side_b_1 = round(cake_side_a_1 - 0.3 * cake_side_a_1)
        #
        # elif 26 <= self.portion <= 45:  # 2 layers
        #     layer_1 = cake_size * 0.65
        #     layer_2 = cake_size * 0.35
        #     cake_side_a_1 = round(math.sqrt(layer_1 / 0.7))
        #     cake_side_b_1 = round(cake_side_a_1 - 0.3 * cake_side_a_1)
        #     cake_side_a_2 = round(math.sqrt(layer_2 / 0.7))
        #     cake_side_b_2 = round(cake_side_a_2 - 0.3 * cake_side_a_2)
        #
        # elif 46 <= self.portion <= 75:  # 3 layers
        #     layer_1 = cake_size * 0.46
        #     layer_2 = cake_size * 0.32
        #     layer_3 = cake_size * 0.24
        #     cake_side_a_1 = round(math.sqrt(layer_1 / 0.7))
        #     cake_side_b_1 = round(cake_side_a_1 - 0.3 * cake_side_a_1)
        #     cake_side_a_2 = round(math.sqrt(layer_2 / 0.7))
        #     cake_side_b_2 = round(cake_side_a_2 - 0.3 * cake_side_a_2)
        #     cake_side_a_3 = round(math.sqrt(layer_3 / 0.7))
        #     cake_side_b_3 = round(cake_side_a_3 - 0.3 * cake_side_a_3)
        return [(cake_side_a_1, "x", cake_side_b_1), (cake_side_a_2, "x", cake_side_b_2),
                (cake_side_a_3, "x", cake_side_b_3)]
