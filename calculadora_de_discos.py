class CalculatePlates:
    def __init__(self, availabe_plates, total_net_weight, bar_weight, used_plates):
        self.availabe_plates = availabe_plates
        self.total_net_weight = total_net_weight
        self.bar_weight = bar_weight
        self.used_plates = used_plates
        
    def calculation(self):
        current_weight = self.bar_weight
        counter = 0
        
        while current_weight < self.total_net_weight and counter < len(self.availabe_plates):
            weight_to_add = self.availabe_plates[counter] * 2
            
            if current_weight + weight_to_add <= self.total_net_weight: 
                current_weight += weight_to_add
                self.used_plates.append(self.availabe_plates[counter])
  
            counter += 1    

        return round(current_weight, 2)
        
class Exceed(CalculatePlates):
    def __init__(self, availabe_plates, total_net_weight, bar_weight, used_plates):
        super().__init__(availabe_plates, total_net_weight, bar_weight, used_plates)
      
    def exceeded_case(self):
        add_more_plates = self.used_plates.copy()

        current_weight = super().calculation()

        exceeded_weight = current_weight + (self.availabe_plates[-1] * 2)

        if (exceeded_weight - self.total_net_weight) <= (self.total_net_weight - current_weight):#abs() could be better
            add_more_plates.append(self.availabe_plates[-1])
            return f"""Recomended weight: {exceeded_weight} kg
Plates to use: {add_more_plates}"""

        else:
            return 0
                   
availabe_plates = [20.4, 20.4, 20.4, 15, 11.3, 11.3, 10, 5, 5, 2.5, 1.1, 1.1, 1.1]
total_net_weight = 103
BAR_WEIGHT = 20
used_plates = []

underneath = CalculatePlates(availabe_plates, total_net_weight, BAR_WEIGHT, used_plates)
above = Exceed(availabe_plates, total_net_weight, BAR_WEIGHT, used_plates)

print(f"Weight: {underneath.calculation()} kg")
print(f"Plates to use: {underneath.used_plates}\n")

print(above.exceeded_case())

