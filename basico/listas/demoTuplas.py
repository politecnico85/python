class DemoTuplas:
    def __init__(self):
        self.tupla = (1, 2, 3, 4, 5)
        self.tupla2 = (6, 7, 8, 9, 10)
        self.tupla3 = self.tupla + self.tupla2
        self.tupla4 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.tupla5 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.tupla6 = tuple('Nabucodonosor')
        

    def crear_tupla_fromString(self, cadena):
        return tuple(cadena)

    def mostrar_tupla(self, tupla):
        print(tupla)
        for i in tupla:
            print(i)


    