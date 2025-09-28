import itertools
import math

class CalculatePlates:
    def __init__(self, availabe_plates, total_net_weight, bar_weight, used_plates):
        self.availabe_plates = availabe_plates
        self.total_net_weight = total_net_weight
        self.bar_weight = bar_weight
        self.used_plates = used_plates
        
    def calculation(self):
        objetive_weight = (self.total_net_weight - self.bar_weight) / 2
        combinations = []
        best_gap = float('inf')
        
        for i in range(1, len(self.availabe_plates)+ 1):
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
        return self.used_plates
        
availabe_plates = [20.4, 20.4, 20.4, 15, 11.3, 11.3, 10, 5, 5, 2.5, 1.1, 1.1, 1.1]
total_net_weight = 40.8
BAR_WEIGHT = 20
used_plates = []

underneath = CalculatePlates(availabe_plates, total_net_weight, BAR_WEIGHT, used_plates)
#above = Exceed(availabe_plates, total_net_weight, BAR_WEIGHT, used_plates)

#print(f"Weight: {underneath.calculation()} kg")
#print(f"Plates to use: {underneath.used_plates}\n")
print(f"Plates to use: {underneath.calculation()}\n")

#print(above.exceeded_case())

