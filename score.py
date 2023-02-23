class Score:

    def count_Total_One(self, round_values):
        total = round_values.count(1) * 1
        return total

    def count_Total_Two(self, round_values):
        total = round_values.count(2) * 2
        return total

    def count_Total_Three(self, round_values):
        total = round_values.count(3) * 3
        return total

    def count_Total_Four(self, round_values):
        total = round_values.count(4) * 4
        return total

    def count_Total_Five(self, round_values):
        total = round_values.count(5) * 5
        return total

    def count_Total_Six(self, round_values):
        total = round_values.count(6) * 6
        return total

    def count_Brelan(self, round_values):
        brelan = sum(round_values)
        return brelan

    def count_Square(self, round_values):
        square = sum(round_values)
        return square

    def count_Full(self):
        return 30

    def count_Little_Suite(self):
        return 30

    def count_High_Suite(self):
        return 40

    def count_Yams(self):
        return 50

    def count_Luck(self, round_values):
        luck = sum(round_values)
        return luck

    def count_total_I(self, section_haute):
        list_values = list(section_haute["part_I"].values())
        return sum(list_values)

    def count_total_II(self, section_basse):
        list_values = list(section_basse["part_II"].values())
        return sum(list_values)

    def count_total_game(self, section_haute, section_basse):
        value = int(section_haute["count_Total"]["total_Part_I"])
        value2 = int(section_basse["count_Total"]["total_Part_II"])
        print(value + value2)
