import unittest
from test_parcial import notas
class TestMyModule(unittest.TestCase):
    
    def test_sum(self):
        lista = [5,5,5,5,5]
        self.assertEqual(test_parcial.calcular_notas(lista), 5)

unittest.main()