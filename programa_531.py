import calculadora_de_discos as cdd

class MakePorcentagesList: #Devuelve una lista con los porcentajes a usar en cada semana --> [[], [], []]
    def __init__(self):
        self.all_porcentages = [0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]
        self.sorted_porcentages = []

    def porcentages_list(self): # Ordena los porcentajes para cada semana.
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

class Structure: # Calcula los pesos a partir de los porcentajes.
    def __init__(self, porcentages, tm):
        self.porcentages = porcentages
        self.tm = tm
        self.lift_weights_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def calculate_weights(self):
        for week_index in range(len(self.porcentages)):
            for porcentage_index, porcentage in enumerate(self.porcentages[week_index]):
                self.lift_weights_list[week_index][porcentage_index] = self.tm * porcentage
        return self.lift_weights_list

    def deload_week(self):
        return self.tm * 0.5, self.tm *0.6

def measurement_unit(weight, unit: str): # Trabajar todo en Kg
    unit = unit.lower()
    if unit == "kg":
        return weight
    elif unit == "lbs":  
        weight = weight / 2.20462
        return weight 

porcentages = MakePorcentagesList().porcentages_list()

def get_data(): # Pregunta 1RM/TM y sistema de medida.
    print("Recomendado en ejercicios compuestos como: Press de banca, Sentadilla y Peso Muerto.\n")
    verification = str(input("¿Conoce su máximo de trabajo(TM)?: ")).lower()

    while verification != "si" and verification != "no":
        print("No existe esta opción.")
        verification = str(input("¿Conoce su máximo de trabajo(TM)?: ")).lower()

    if verification == "si":
        tm = float(input("Máximo de trabajo: "))
        unit = input("kg/lbs: ")
        tm = measurement_unit(tm, unit)
    else:
        one_RM = float(input("1RM real: "))    
        unit = input("kg/lbs: ")
        one_RM = measurement_unit(one_RM, unit)
        tm = one_RM * 0.90

    return tm, unit

tm, unit = get_data()
excercise = Structure(porcentages, tm)

def show_plan(excercise: Structure, tm, unit, porcentages: MakePorcentagesList): # Muestra en terminal.
    if unit == "kg":
        display_unit = "kg"
        availabe_plates = [20, 20, 20, 20, 20, 15, 15, 10, 10, 5, 5, 5, 3, 3, 3]
        bar_weight = 20
    else:
        display_unit = "lbs"
        availabe_plates = [44.0924, 44.0924, 44.0924, 44.0924, 44.0924, 33.0693, 33.0693, 22.0493, 22.0462, 11.0231, 11.0231, 11.0231, 6.6138, 6.6138, 6.6138]
        bar_weight = 44.09

    conv = 1.0 if unit == "kg" else 2.20462
    print(f"\nTM: {round(tm * conv, 2)} {display_unit}.\n")

    weights = excercise.calculate_weights()
    excercise_deload = excercise.deload_week()

    week_counter = 1
    for week_index in range(len(weights)):
        print(f"Week {week_counter}:")
        week_counter = week_counter + 1 
        for weight_index, weight in enumerate(weights[week_index]): 
            display_weight = round(weight * conv, 2)
            plates_to_use = cdd.CalculatePlates(availabe_plates, display_weight, bar_weight)
            print(f"{porcentages[week_index][weight_index] * 100:.0f}% : {display_weight} {display_unit}. {plates_to_use.calculation()}")

    print("\nDeload week:")
    dis_1 = round(excercise_deload[0] * conv, 2)
    dis_2 = round(excercise_deload[1] * conv, 2)
    plates_use1 = cdd.CalculatePlates(availabe_plates, dis_1, bar_weight)
    plates_use2 = cdd.CalculatePlates(availabe_plates, dis_2, bar_weight)
    print(f"3x50-60%: {dis_1} - {dis_2} {display_unit}. {plates_use1.calculation()}-{plates_use2.calculation()}")

show_plan(excercise, tm, unit, porcentages)