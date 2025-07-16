from abc import ABC, abstractmethod

#Devuelve una lista con los porcentajes a usar en cada semana --> [[], [],[]]
class CrearListaPorcentajes:
    def __init__(self):
        self.porcentajes_todos = [0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]
        self.porcentajes_ordenados = []

    def porcentajes_lista(self):
        for i in range(1, 4):
            if i == 1:
                agregar = self.porcentajes_todos[0:5:2]
                self.porcentajes_ordenados.append(agregar)
                
            elif i == 2:
                agregar = self.porcentajes_todos[1::2]
                self.porcentajes_ordenados.append(agregar)
                
            else:
                agregar = self.porcentajes_todos[2::2]
                self.porcentajes_ordenados.append(agregar)
        return self.porcentajes_ordenados
  
class Estructura(ABC):#nomas para usar lo de metodos abstractos ¯\_(ツ)_/¯
    def __init__(self, porcentajes, tm):
        self.porcentajes = porcentajes
        self.tm = tm
        
    @abstractmethod
    def calcular_pesos_semana_1(self):
        porcentajes = self.porcentajes[0]
        for porcentaje in porcentajes:
           print(f"{round(porcentaje * 100)}%: {round((self.tm * porcentaje), 2)}kg.")
    
    @abstractmethod
    def calcular_pesos_semana_2(self):
        porcentajes = self.porcentajes[1]
        for porcentaje in porcentajes:
           print(f"{round(porcentaje * 100)}%: {round((self.tm * porcentaje), 2)}kg.")
    
    @abstractmethod
    def calcular_pesos_semana_3(self):
        porcentajes = self.porcentajes[2]
        for porcentaje in porcentajes:
           print(f"{round(porcentaje * 100)}%: {round((self.tm * porcentaje), 2)}kg.")
    
    @abstractmethod
    def calcular_pesos_semana_deload(self):
        print(f"3 series con 50-60%, es decir: {round(self.tm/2)}-{round(self.tm*0.6)} kg")
    
class Ejercicio(Estructura):
    def calcular_pesos_semana_1(self):
        return super().calcular_pesos_semana_1()
        
    def calcular_pesos_semana_2(self):
        return super().calcular_pesos_semana_2()
        
    def calcular_pesos_semana_3(self):
        return super().calcular_pesos_semana_3()
        
    def calcular_pesos_semana_deload(self):
        return super().calcular_pesos_semana_deload()
    
#no cambian
porcentaje = CrearListaPorcentajes()
porcentajes = porcentaje.porcentajes_lista()        

print("Recomendado en ejercicios compuestos como: Press de banca, Sentadilla y Peso Muerto.")
unorm = int(input("1RM real(kg): "))    
tm = unorm * 0.90

ejercicio = Ejercicio(porcentajes, tm)

def mostrar_plan(ejercicio, tm):
    print(f"""TM: {tm}
      """)
    print("Semana 1 ")
    ejercicio.calcular_pesos_semana_1()
    print("Semana 2")
    ejercicio.calcular_pesos_semana_2()
    print("Semana 3")
    ejercicio.calcular_pesos_semana_3()
    print("Semana 4")
    ejercicio.calcular_pesos_semana_deload()
    
mostrar_plan(ejercicio, tm)

#No le entendi