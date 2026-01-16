#Devuelve una lista con los porcentajes a usar en cada semana --> [[], [],[]]
class MakePorcentagesList:
    def __init__(self):
        self.all_porcentages = [0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]
        self.sorted_porcentages = []

    def porcentagesList(self):
        for i in range(3):
            if i == 0:
                agregar = self.all_porcentages[0:5:2]
                self.sorted_porcentages.append(agregar)
                
            elif i == 1:
                agregar = self.all_porcentages[1::2]
                self.sorted_porcentages.append(agregar)
            else:
                agregar = self.all_porcentages[2::2]
                self.sorted_porcentages.append(agregar)
        return self.sorted_porcentages

class Structure:
    def __init__(self, porcentages, tm):
        self.porcentages = porcentages
        self.tm = tm
        self.lift_weights_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def calculateWeights(self):
        for week_index in range(len(self.porcentages)):
            for porcentage_index, porcentage in enumerate(self.porcentages[week_index]):
                self.lift_weights_list[week_index][porcentage_index] = self.tm * porcentage
        return self.lift_weights_list

    def deloadWeek(self):
        return self.tm * 0.5, self.tm *0.6

# Trabajar todo en Kg
def measurementUnit(weight, unit: str):
    unit = unit.lower()
    if unit == "kg":
        return weight
    elif unit == "lbs":  
        weight = weight / 2.20462
        return weight 

#no cambian
porcentages = MakePorcentagesList().porcentagesList()
def getData():
    print("Recomendado en ejercicios compuestos como: Press de banca, Sentadilla y Peso Muerto.\n")
    verification = str(input("¿Conoce su máximo de trabajo(TM)?: ")).lower()

    while verification != "si" and verification != "no":
        print("No existe esta opción.")
        verification = str(input("¿Conoce su máximo de trabajo(TM)?: ")).lower()

    if verification == "si":
        tm = float(input("Máximo de trabajo: "))
        unit = input("kg/lbs: ")
        tm = measurementUnit(tm, unit)
    else:
        one_RM = float(input("1RM real: "))    
        unit = input("kg/lbs: ")
        one_RM = measurementUnit(one_RM, unit)
        tm = one_RM * 0.90

    return tm, unit
tm, unit = getData()
excercise = Structure(porcentages, tm)

def show_plan(excercise: Structure, tm, unit, porcentages: MakePorcentagesList):  
    display_unit = "kg" if unit == "kg" else "lbs"
    conv = 1.0 if unit == "kg" else 2.20462
    print(f"\nTM: {round(tm * conv, 2)} {display_unit}.\n")

    weights = excercise.calculateWeights()
    excercise_deload = excercise.deloadWeek()
    
    c = 1
    for week_index in range(len(weights)):
        print(f"Week {c}:")
        c = c + 1 
        for weight_index, weight in enumerate(weights[week_index]): 
            display_weight = round(weight * conv, 2)
            print(f"{porcentages[week_index][weight_index] * 100:.0f}% : {display_weight} {display_unit}")

    print("\nDeload week:")
    print(f"3x50-60%: {round((excercise_deload[0] * conv), 2)} - {round((excercise_deload[1] * conv), 2)} {display_unit}")

show_plan(excercise, tm, unit, porcentages)