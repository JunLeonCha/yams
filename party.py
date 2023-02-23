from dice import Dice


class Party:

    def __init__(self, nb_dices):
        self.nb_dices = nb_dices
        self.dices = [Dice() for i in range(0, nb_dices)]

    def roll_dice(self, dice_indices):
        for i in dice_indices:
            self.dices[int(i)].roll()

    def reroll_dices(self, ask_reroll, dices_value):
        self.selected_dice = self.roll_dice(
            [int(i) - 1 for i in ask_reroll])
        self.new_dices_value = [i.value for i in dices_value]
        return self.new_dices_value
