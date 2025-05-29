import unittest
from calculadora import calcular, CalculadoraBinariaError


class TestCalculadoraBinaria(unittest.TestCase):

    def test_soma_basica(self):
        self.assertEqual(calcular("00000001", "00000001", "+"), "00000010")  # 1+1=2

    def test_soma_negativa(self):
        self.assertEqual(calcular("11111111", "00000001", "+"), "00000000")  # -1+1=0

    def test_soma_overflow(self):
        with self.assertRaises(CalculadoraBinariaError):
            calcular("01111111", "00000001", "+")

    def test_subtracao_basica(self):
        self.assertEqual(calcular("00000010", "00000001", "-"), "00000001")  # 2-1=1

    def test_subtracao_negativa(self):
        self.assertEqual(calcular("00000001", "00000010", "-"), "11111111")  # 1-2=-1

    def test_subtracao_overflow(self):
        with self.assertRaises(CalculadoraBinariaError):
            calcular("10000000", "00000001", "-")

    def test_multiplicacao_basica(self):
        self.assertEqual(calcular("00000011", "00000010", "x"), "00000110")  # 3*2=6

    def test_multiplicacao_negativa(self):
        self.assertEqual(calcular("11111110", "00000011", "x"), "11111010")  # -2*3=-6

    def test_multiplicacao_overflow(self):
        with self.assertRaises(CalculadoraBinariaError):
            calcular("01111111", "00000010", "x")  # 127*2 overflow

    def test_valor_invalido_caracter(self):
        with self.assertRaises(CalculadoraBinariaError):
            calcular("0000000A", "00000001", "+")

    def test_valor_invalido_operacao(self):
        with self.assertRaises(CalculadoraBinariaError):
            calcular("00000001", "00000001", "/")

    def test_tamanho_invalido_curto(self):
        with self.assertRaises(CalculadoraBinariaError):
            calcular("00001", "00000001", "+")

    def test_tamanho_invalido_longo(self):
        with self.assertRaises(CalculadoraBinariaError):
            calcular("000000001", "00000001", "+")

    def test_entrada_nao_string(self):
        with self.assertRaises(CalculadoraBinariaError):
            calcular(123, "00000001", "+")

    def test_entrada_vazia(self):
        with self.assertRaises(CalculadoraBinariaError):
            calcular("", "", "+")

    def test_operacao_nao_string(self):
        with self.assertRaises(CalculadoraBinariaError):
            calcular("00000001", "00000001", 123)

    def test_zero(self):
        self.assertEqual(calcular("00000000", "00000000", "+"), "00000000")

    def test_max_pos(self):
        self.assertEqual(calcular("01111111", "00000000", "+"), "01111111")

    def test_min_neg(self):
        self.assertEqual(calcular("10000000", "00000000", "+"), "10000000")

    def test_multiplicacao_zero(self):
        self.assertEqual(calcular("00000000", "11111111", "x"), "00000000")

    def test_multiplicacao_negativo_negativo(self):
        self.assertEqual(calcular("11111111", "11111111", "x"), "00000001")  # -1 * -1 = 1


if __name__ == '__main__':
    unittest.main()
