import itertools
import math

class CalculatePlates:
    def __init__(self, availabe_plates, total_net_weight, bar_weight):
        self.availabe_plates = availabe_plates
        self.total_net_weight = total_net_weight
        self.bar_weight = bar_weight
        self.used_plates = []

    def calculation(self):
        objetive_weight = (self.total_net_weight - self.bar_weight) / 2
        combinations = []
        best_gap = float('inf')

        if objetive_weight <= 0:
            return 0, 0

        for i in range(1, len(self.availabe_plates) + 1):
            for comb in itertools.combinations(self.availabe_plates, i):
                combs_addition = sum(comb)
                gap = abs(combs_addition - objetive_weight)

                if gap < best_gap:
                    best_gap = gap
                    combinations = [comb]
                elif math.isclose(gap, best_gap, abs_tol=1e-10):
                    combinations.append(comb)

        self.used_plates = [list(tupla) for tupla in combinations]
        unique_combinations = list(dict.fromkeys([tuple(sorted(comb)) for comb in self.used_plates]))
        self.used_plates = [list(tupla) for tupla in unique_combinations]
        if len(self.used_plates) >= 2:
            return [round(x, 1) for x in self.used_plates[0]], [round(x, 1) for x in self.used_plates[1]]
        elif len(self.used_plates) == 1:
            return [round(x, 1) for x in self.used_plates[0]], []
        else:
            return [], []