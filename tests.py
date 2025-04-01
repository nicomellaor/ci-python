import unittest
from unittest.mock import patch
from sistema import leer_datos_sensor, convertir_a_fahrenheit, registrar_datos

class TestSistemaSensores(unittest.TestCase):

    @patch('sistema.leer_datos_sensor')
    def test_mock_lectura_sensor(self, mock_sensor):
        mock_sensor.return_value = 25.0
        valor = leer_datos_sensor()
        self.assertEqual(valor, 25.0)

    def test_conversion_fahrenheit(self):
        self.assertEqual(convertir_a_fahrenheit(0), 32.0)
        self.assertEqual(convertir_a_fahrenheit(100), 212.0)
        self.assertAlmostEqual(convertir_a_fahrenheit(-10), 14.0, places=1)

    def test_conversion_error(self):
        with self.assertRaises(ValueError):
            convertir_a_fahrenheit("veinte")

    def test_registro_datos(self):
        resultado = registrar_datos(20)
        self.assertEqual(resultado["celsius"], 20)
        self.assertEqual(resultado["fahrenheit"], 68.0)

if __name__ == '__main__':
    unittest.main()