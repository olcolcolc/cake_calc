import math


class Cake:
    def __init__(self, portion, price_per_person, box_price, gf):
        self.portion = portion
        self.price_per_person = price_per_person
        self.box_price = box_price
        self.gf = gf

    def price_calc(self):  # Price for the cake
        price_calc = self.portion * self.price_per_person
        box_price = self.box_price
        gf = 0

        if gf is True:
            price_calc += (portion * 2)

        if box_price is True:
            if portion <= 20:
                box_price = 7  # TODO sprawdzić ceny opakowań
            elif portion <= 30:
                box_price = 10
            elif portion <= 40:
                box_price = 15
            elif portion > 40:
                box_price = 20
            price_calc += box_price

        return [price_calc, box_price]

    def round_calc(self):  # Round cake size calculator
        portion = self.portion
        pi = round(math.pi, 2)
        one_piece = 22.8
        cake_size_1 = "-"  # d size of first layer
        cake_size_2 = "-"  # d size of second layer
        cake_size_3 = "-"  # d size of third layer

        def circle_field_calc(portion):
            circle_field = portion * one_piece
            return circle_field

        def d_calc(portion, circle_field):
            d = 2 * math.sqrt(circle_field / pi)
            d = round(d)
            return [d, circle_field]

        if portion < 31:  # cake with one layer
            cake_size_1 = round(d_calc(portion, circle_field_calc(portion))[0])

        elif 31 <= portion <= 50:  # cake with two layers
            layer_1 = d_calc(portion, circle_field_calc(portion))[
                              1] * 0.65  # 65 % of cake field is first layer field
            layer_2 = d_calc(portion, circle_field_calc(portion))[
                               1] * 0.35  # 35 % of cake field is second layer field
            cake_size_1 = d_calc(portion, layer_1)[0]  # calculating d in first layer
            cake_size_2 = d_calc(portion, layer_2)[0]  # calculating d in second layer

        elif 51 <= portion <= 75:  # cake with three layers
            layer_1 = d_calc(portion, circle_field_calc(portion))[
                              1] * 0.465  # ~46,5 % of cake field is first layer field
            layer_2 = d_calc(portion, circle_field_calc(portion))[
                               1] * 0.32  # ~32 % of cake field is second layer field
            layer_3 = d_calc(portion, circle_field_calc(portion))[
                              1] * 0.24  # ~24 % of cake field is third layer field
            cake_size_1 = d_calc(portion, layer_1)[0]  # calculating d in first layer
            cake_size_2 = d_calc(portion, layer_2)[0]  # calculating d in second layer
            cake_size_3 = d_calc(portion, layer_3)[0]  # calculating d in third layer

        return [cake_size_1, cake_size_2, cake_size_3]

    def one_portion_field(self, side):  # With this function you can set side size of one portion
        one_portion_field = side ** 2
        return one_portion_field  # Field size of portion for one person

    def square_calc(self):
        portion = self.portion
        square_cake_size = Cake.one_portion_field(self, 6) * portion
        cake_side_1 = "-"
        cake_side_2 = "-"
        cake_side_3 = "-"

        if portion <= 30:  # 1 layers
            cake_side_1 = round(math.sqrt(square_cake_size))


        elif 31 < portion <= 50:  # 2 layers
            layer_1 = square_cake_size * 0.65
            layer_2 = square_cake_size * 0.35
            cake_side_1 = round(math.sqrt(layer_1))
            cake_side_2 = round(math.sqrt(layer_2))


        elif 51 <= portion <= 75:  # 3 layers
            layer_1 = square_cake_size * 0.46
            layer_2 = square_cake_size * 0.32
            layer_3 = square_cake_size * 0.24
            cake_side_1 = round(math.sqrt(layer_1))
            cake_side_2 = round(math.sqrt(layer_2))
            cake_side_3 = round(math.sqrt(layer_3))

        return [cake_side_1, cake_side_2, cake_side_3]

    def rectangle_calc(self):
        portion = self.portion
        # Cake.one_portion_field(6)
        cake_size = Cake.one_portion_field(self, 6) * portion
        cake_side_a_1 = "-"
        cake_side_b_1 = "-"
        cake_side_a_2 = "-"
        cake_side_b_2 = "-"
        cake_side_a_3 = "-"
        cake_side_b_3 = "-"

        if portion <= 25:  # one layer
            cake_side_a_1 = round(math.sqrt(cake_size / 0.7))
            cake_side_b_1 = round(cake_side_a_1 - 0.3 * cake_side_a_1)

        elif 26 <= portion <= 45:  # 2 layers
            layer_1 = cake_size * 0.65
            layer_2 = cake_size * 0.35
            cake_side_a_1 = round(math.sqrt(layer_1 / 0.7))
            cake_side_b_1 = round(cake_side_a_1 - 0.3 * cake_side_a_1)
            cake_side_a_2 = round(math.sqrt(layer_2 / 0.7))
            cake_side_b_2 = round(cake_side_a_2 - 0.3 * cake_side_a_2)

        elif 46 <= portion <= 75:  # 3 layers
            layer_1 = cake_size * 0.46
            layer_2 = cake_size * 0.32
            layer_3 = cake_size * 0.24
            cake_side_a_1 = round(math.sqrt(layer_1 / 0.7))
            cake_side_b_1 = round(cake_side_a_1 - 0.3 * cake_side_a_1)
            cake_side_a_2 = round(math.sqrt(layer_2 / 0.7))
            cake_side_b_2 = round(cake_side_a_2 - 0.3 * cake_side_a_2)
            cake_side_a_3 = round(math.sqrt(layer_3 / 0.7))
            cake_side_b_3 = round(cake_side_a_3 - 0.3 * cake_side_a_3)
        return [(cake_side_a_1, "x", cake_side_b_1), (cake_side_a_2, "x", cake_side_b_2),
                (cake_side_a_3, "x", cake_side_b_3)]
