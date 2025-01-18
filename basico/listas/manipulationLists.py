class ManipulationLists:
    def __init__(self):

    def change_value_list(self, lista, index, value ):
        try:
            print(f" el valor acual de la lista es {lista[index]}")
            self.lista[index] = 10.5
            print(f" el valor cambiado de la lista es {lista[index]}")
        except Exception as e:
            print(f"Error: {e}")
        