from demo0001 import DemoListas
class TestListas:
    def setup(self):
        self.instancia = DemoListas()
        self.hall = 11.25
        self.kit = 18.0
        self.liv = 20.0
        self.bed = 10.75
        self.bath = 9.50
        self.lista_simple = ["hallaway", self.hall, "kitchen", self.kit, "Living room", self.liv, "bedroom", self.bed, "bathroom", self.bath]
        self.lista_de_listas  = [ ["hallaway", self.hall], ["kittchen", self.kit], ["Living room", self.liv], ["bedroom", self.bed], ["bathroom", self.bath] ]
        

    def demo_crear_lista(self):
        resultado = self.instancia.crear_lista([])
        print(resultado)

    def demo_crear_lista_con_etiquetas(self):
        
        resultado = self.instancia.crear_lista(self.lista_simple)
        print(resultado)


    def demo_crear_lista_de_listas(self):
        #house = [ ["hallaway", self.hall], ["kittchen", self.kit], ["Living room", self.liv], ["bedroom", self.bed], ["bathroom", self.bath] ]
        resultado = self.instancia.crear_lista(self.lista_de_listas)
        print(resultado)


    def demo_get_element_from_list(self, index):
        #lista_parametros = ["hallaway", self.hall, "kitt}chen", self.kit, "Living room", self.liv, "bedroom", self.bed, "bathroom", self.bath]
        resultado = self.instancia.obtener_elemento(self.lista_simple, index)
        print(f" el elemnto encontrado en la posicion {index} es {resultado}")

    def demo_get_sublist(self, begin_index, end_index):
        try:
            resultado = self.instancia.obtener_sublista(self.lista_simple, begin_index, end_index)
            print(f" la sublista encontrada es {resultado}")

        except Exception as e:
            print(f"Error: {e}")

    def demo_slicing_list(self):
        try:
            resultado1 = self.lista_simple[:6]
            print(f" el slicing de la lista es {resultado1}")

            resultado2 = self.lista_simple[3:]
            print(f" el slicing de la lista es {resultado2}")

            resultado3 = self.lista_simple[2:7]
            print(f" el slicing de la lista es {resultado3}")

        except Exception as e:
            print(f"Error: {e}")
        
    """
    my_list[start:end]
    Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
    Create upstairs, as the last 4 elements of areas. This time, simplify the slicing by omitting the end index.
    Print both downstairs and upstairs using print().
    """

    def demo_slicing_dicing(self):
        
   
        try:
            # Use slicing to create downstairs
            upstairs = self.lista_simple[6:]
            downstairs = self.lista_simple[:6]
            print(f" upstairs es {downstairs}")
            print(f" downstairs es {upstairs}")

            resultado1 = self.lista_simple[::2]
            print(f" el slicing de la lista es {resultado1}")

            resultado2 = self.lista_simple[1::2]
            print(f" el slicing de la lista es {resultado2}")

            resultado3 = self.lista_simple[2:7:2]
            print(f" el slicing de la lista es {resultado3}")

        except Exception as e:
            print(f"Error: {e}")


    def demo_subsetting_list_of_list(self):
        resultado1 = self.lista_de_listas[4][1]
        print(f" subsetting lista de lista es {resultado1}")


if __name__ == '__main__':
    test = TestListas()
    test.setup()
    test.demo_crear_lista()
    test.demo_crear_lista_con_etiquetas()
    test.demo_crear_lista_de_listas()
    test.demo_get_element_from_list(2)
    test.demo_get_sublist(2, 5)
    test.demo_slicing_list()
    test.demo_slicing_dicing()
    test.demo_subsetting_list_of_list()