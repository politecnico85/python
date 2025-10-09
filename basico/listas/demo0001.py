class DemoListas:
    def __init__(self):
        self.hall = 11.25
        self.kit = 18.0
        self.liv = 20.0
        self.bed = 10.75
        self.bath = 9.50

    
    def crear_lista(self, lista):
        if (type(lista) == list):
            if len(lista) == 0:
                self.lista = [self.hall, self.kit, self.liv, self.bed, self.bath]
            else:
                self.lista = lista
        else:
            self.lista = [self.hall, self.kit, self.liv, self.bed, self.bath]
         
        return self.lista
    

    def modificar_lista(self, lista, desde, hasta, values):
        if len(lista) < desde - 1:
            return lista
        lista[desde, hasta] = values
        return lista
    
    def imprimir_lista(self, lista):
        for i in lista:
            print(i)


    def obtener_elemento(self, lista, index):
        return lista[index]


    def obtener_sublista(self, lista, begin_index, end_index):
        return lista[begin_index:end_index]
  