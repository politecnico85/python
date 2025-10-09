import unittest
from demoTuplas import DemoTuplas

class TestDemoTuplas(unittest.TestCase):
    def setUp(self):
        self.demo_tuplas = DemoTuplas() 
    
    def test_crear_tupla_fromString(self):
        cadena = 'Nabucodonosor'
        created_tupla = self.demo_tuplas.crear_tupla_fromString(cadena)
        expected_tupla = ('N', 'a', 'b', 'u', 'c', 'o', 'd', 'o', 'n', 'o', 's', 'o', 'r')
        self.assertEqual(created_tupla, expected_tupla) 

    def test_mostrar_tupla(self):
        tupla = ('N', 'a', 'b', 'u', 'c', 'o', 'd', 'o', 'n', 'o', 's', 'o', 'r') 
        with self.assertLogs(level='INFO') as log:
            self.demo_tuplas.mostrar_tupla(tupla)
            output = "\n".join(log.output)
            for value in ['N', 'a', 'b', 'u', 'c', 'o', 'd', 'o', 'n', 'o', 's', 'o', 'r']:
                self.assertIn(value, output)


if __name__ == '__main__':
    unittest.main()

