import collections


class Combination:

    section_haute = {
        "part_I": {
            # "Score 1": 0,
            # "Score 2": 0,
            # "Score 3": 0,
            # "Score 4": 0,
            # "Score 5": 0,
            # "Score 6": 0,
        },
        "count_Total": {
            "total_Part_I": 0
        }
    }

    section_basse = {
        "part_II": {
            # "Score Brelan": 0,
            # "Score Carré": 0,
            # "Score Full": 0,
            # "Score petite suite": 0,
            # "Score grande suite": 0,
            # "Score Yams": 0,
            # "Score Bonus": 0,
        },
        "count_Total": {
            "total_Part_II": 0
        }
    }

    # def check_combination_has_value(self, section_haute):
    #     for

    def check_combination(self, round_values):

        round_values.sort()
        values_occurences = list(collections.Counter(round_values).values())

        if 3 in values_occurences:
            results = ["Brelan"]
            if 2 in values_occurences:
                results.append("Full")
            for result in results:
                print(result)
            return result

        if 4 in values_occurences:
            results = ["Brelan", "Carré"]
            for result in results:
                print(result)
            return result

        if 5 in values_occurences:
            results = ["Yams", "Carré", "Brelan"]
            for result in results:
                print(result)
            return result

        if (1 in round_values and 2 in round_values and 3 in round_values and 4 in round_values or 2 in round_values and 3 in round_values and 4 in round_values and 5 in round_values or 3 in round_values and 4 in round_values and 5 in round_values and 6 in round_values):
            print("\nPetite Suite")
            if (1 in round_values and 2 in round_values and 3 in round_values and 4 in round_values and 5 in round_values or 2 in round_values and 3 in round_values and 4 in round_values and 5 in round_values and 6 in round_values):
                print("Grande Suite\n")
                return ("Grande Suite")
            return ("Petite Suite")
        else:
            print("Combinaison simple")
            return (6)
