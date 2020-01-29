class Cars:
    color = str()
    kolesa = int()
    rul = bool()

    def __init__(self, color):
        self.color = color

    def __avito(self, flag):
        if flag == True:
            print("Тачка продана")
        elif flag == False:
            print("Тачка не продана")

class Lada(Cars):
    model = "NOMODEL"

    def __init__(self, kolesa, rul):
        self.kolesa = kolesa
        self.rul = rul
    def signal(self):
        print("Beep")

kalina = Lada(4,True)
horse = Cars("red")
try:
    kalina.Cars__avito(True)
except:
    print("Инкапсуляция")
horse._Cars__avito(True)
kalina.signal()
print(horse.color, horse.kolesa, horse.rul)
print(kalina.model, kalina.color, kalina.kolesa, kalina.rul)