import unittest
from demo0001 import DemoListas

class TestDemoListas(unittest.TestCase):
    def setUp(self):
        self.demo_listas = DemoListas()

    def test_crear_lista(self):
        lista = [20.5, 31, 8, 5, 6]
        created_list = self.demo_listas.crear_lista(lista)
        expected_list = [11.25, 18.0, 20.0, 10.75, 9.50]
        self.assertEqual(created_list, expected_list)

    def test_modificar_lista(self):
        lista = [20.5, 31, 8, 5, 65]
        modified_list = self.demo_listas.modificar_lista(lista, 1, 3, [1, 2, 3])
        expected_list = [20.5, 1, 2, 3, 5, 65]
        self.assertEqual(modified_list, expected_list)  
        

    def test_imprimir_lista(self):
        lista = [20.5, 31, 8, 5, 6]
        self.demo_listas.crear_lista(lista)
        with self.assertLogs(level='INFO') as log:
            self.demo_listas.imprimir_lista()
            output = "\n".join(log.output)
            for value in [11.25, 18.0, 20.0, 10.75, 9.50]:
                self.assertIn(str(value), output)

    def test_create_list(self):
        created_list = self.demo_listas.crear_lista(None)
        print(created_list)
        expected_list = [11.25, 18.0, 20.0, 10.75, 9.50]
        self.assertEqual(created_list, expected_list)

if __name__ == '__main__':
    unittest.main()