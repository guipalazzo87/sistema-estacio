import unittest
from controle_energia import ligar_equipamento, desligar_equipamento

class TestControleEnergia(unittest.TestCase):
    def test_ligar_equipamento(self):
        resposta = ligar_equipamento(1)
        self.assertEqual(res
