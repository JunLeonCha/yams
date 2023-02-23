class Display:

    choose_dict = {"1": "Un",
                   "2": "Deux",
                   "3": "Trois",
                   "4": "Quatre",
                   "5": "Cinq",
                   "6": "Six",
                   "7": "Brelan",
                   "8": "Carré",
                   "9": "Full",
                   "10": "Petite Suite",
                   "11": "Grande Suite",
                   "12": "Yams",
                   "13": "Bonus"
                   }

    # def choose_combinaison_score(self):
    #     for k, v in self.choose_dict.items():
    #         print("({}) : {}".format(k, v))

    def choose_combinaison_score(self, parameters):
        if parameters is None or (isinstance(parameters, int) and 1 <= parameters <= 6):
            for k, v in self.choose_dict.items():
                if int(k) <= 6:
                    print("({}) : {}".format(k, v))
        else:
            for k, v in self.choose_dict.items():
                if (v == parameters):
                    print("({}) : {}".format(k, v))

    def display_section_haute(self, section_haute):
        print("\n")
        for k, v in section_haute.items():
            print("{} = {}".format(k, v))

    def display_section_basse(self, section_basse):
        for k, v in section_basse.items():
            print("{} = {}".format(k, v))
