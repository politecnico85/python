class DemoListas:
    def __init__(self):
        self.hall = 11.25
        self.kit = 18.0
        self.liv = 20.0
        self.bed = 10.75
        self.bath = 9.50


    def crear_lista(self):
        self.lista = [self.hall, self.kit, self.liv, self.bed, self.bath]
        print(self.lista)

    def imprimir_lista(self):
        for i in self.lista:
            print(i)