from party import Party
# import collections
from combination import Combination
from score import Score
from display import Display


class Launch:

    game = Party(nb_dices=5)
    display = Display()
    combination = Combination()
    score = Score()

    def __init__(self):
        self.game

    def player_phase(self):
        self.turn = 0
        short_answer = ["y", "Y", "n", "N"]
        combination_answer = ["1", "2", "3", "4", "5", "6", "7",
                              "8", "9", "10", "11", "12", "13"]

        while self.turn < 13:
            self.turn += 1
            print("\nRound: " + str(self.turn) + "\n")

            self.game.roll_dice([i for i in range(0, self.game.nb_dices)])
            round_values = [i.value for i in self.game.dices]
            print(round_values)
            self.combination.check_combination(round_values)

            self.reroll = 1
            while self.reroll < 3:
                self.ask_reroll = input(
                    "Voulez-vous relancer des dés? (Y/N)\n")
                if (self.ask_reroll in short_answer and self.reroll < 3):
                    if (self.ask_reroll == "y" or self.ask_reroll == "Y"):
                        self.reroll += 1
                        self.ask_selected_dices = input(
                            "\nChoissisez vos dés? \nEx: 124 ou 145 etc... \n")
                        new_dices_values = self.game.reroll_dices(
                            self.ask_selected_dices, self.game.dices)
                        print(new_dices_values)
                        self.combination.check_combination(new_dices_values)
                    if (self.ask_reroll == "n"):
                        print("fin de tour")
                        reroll = 1
                        break
            self.display.choose_combinaison_score(
                self.combination.check_combination(round_values))
            self.write_combination = input(
                "Ecrivez le nombre de la combinaison choisi. \n").lower()
            if (self.write_combination in combination_answer):
                if (self.write_combination == "1"):
                    self.combination.section_haute["part_I"]["One"] = self.score.count_Total_One(
                        round_values)
                if (self.write_combination == "2"):
                    self.combination.section_haute["part_I"]["Two"] = self.score.count_Total_Two(
                        round_values)
                if (self.write_combination == "3"):
                    self.combination.section_haute["part_I"]["Three"] = self.score.count_Total_Three(
                        round_values)
                if (self.write_combination == "4"):
                    self.combination.section_haute["part_I"]["Four"] = self.score.count_Total_Four(
                        round_values)
                if (self.write_combination == "5"):
                    self.combination.section_haute["part_I"]["Five"] = self.score.count_Total_Five(
                        round_values)
                if (self.write_combination == "6"):
                    self.combination.section_haute["part_I"]["Six"] = self.score.count_Total_Six(
                        round_values)
                if (self.write_combination == "7"):
                    self.combination.section_basse["part_II"]["Brelan"] = self.score.count_Brelan(round_values
                                                                                                  )
                if (self.write_combination == "8"):
                    self.combination.section_basse["part_II"]["Square"] = self.score.count_Square(round_values
                                                                                                  )
                if (self.write_combination == "9"):
                    self.combination.section_basse["part_II"]["Full"] = self.score.count_Full(
                    )
                if (self.write_combination == "10"):
                    self.combination.section_basse["part_II"]["Small_suite"] = self.score.count_Little_Suite(
                    )
                if (self.write_combination == "11"):
                    self.combination.section_basse["part_II"]["High_suite"] = self.score.count_High_Suite(
                    )
                if (self.write_combination == "12"):
                    self.combination.section_basse["part_II"]["Yams"] = self.score.count_Yams(round_values
                                                                                              )
                if (self.write_combination == "13"):
                    self.combination.section_basse["part_II"]["Luck"] = self.score.count_Luck(
                        round_values)

            self.combination.section_haute["count_Total"]["total_Part_I"] = self.score.count_total_I(
                self.combination.section_haute)

            self.display.display_section_haute(
                self.combination.section_haute["part_I"])
            print("\n=================\nTotal part 1 : " +
                  str(self.score.count_total_I(self.combination.section_haute)) + "\n==================")
            self.display.display_section_basse(
                self.combination.section_basse["part_II"])
            print("\n=================\nTotal part 2 : " +
                  str(self.score.count_total_II(self.combination.section_basse)) + "\n==================")

        self.score.count_total_game(
            self.combination.section_haute, self.combination.section_basse)


run = Launch()
run.player_phase()
