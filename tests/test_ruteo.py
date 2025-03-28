import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.sistema_ruteo import SistemaRuteo

class TestSistemaRuteo(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaRuteo()
    
    def test_ruta_directa(self):
        pasos, tiempo = self.sistema.encontrar_ruta("Suba Av Boyacá", "Suba Calle 100")
        self.assertEqual(len(pasos), 1)
        self.assertGreater(tiempo, 0)
    
    def test_ruta_con_transbordo(self):
        pasos, tiempo = self.sistema.encontrar_ruta("Portal Suba", "Av Jimenez")
        self.assertEqual(len(pasos), 2)
        self.assertTrue(pasos[1]['transbordo'])
        self.assertGreater(tiempo, 0)

if __name__ == '__main__':
    unittest.main()
    