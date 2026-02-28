import math
from unittest.mock import patch, call
import pytest
from transformacaoLinear import (
    converterGrausParaRad,
    seno,
    coseno,
    entrar,
    escolher_eixo,
    transformar_eixo,
    dilatacaoXeY,
    dilatacaoXouY,
    reflexaoXouY,
    rotacao,
    cisalhamento,
)


# --- converterGrausParaRad ---

class TestConverterGrausParaRad:
    def test_zero(self):
        assert converterGrausParaRad(0) == 0

    def test_90_graus(self):
        assert converterGrausParaRad(90) == pytest.approx(math.pi / 2)

    def test_180_graus(self):
        assert converterGrausParaRad(180) == pytest.approx(math.pi)

    def test_360_graus(self):
        assert converterGrausParaRad(360) == pytest.approx(2 * math.pi)

    def test_negativo(self):
        assert converterGrausParaRad(-90) == pytest.approx(-math.pi / 2)


# --- coseno ---

class TestCoseno:
    def test_zero(self):
        assert coseno(0) == pytest.approx(1.0)

    def test_90(self):
        assert coseno(90) == pytest.approx(0.0, abs=1e-6)

    def test_180(self):
        assert coseno(180) == pytest.approx(-1.0)

    def test_60(self):
        assert coseno(60) == pytest.approx(0.5, abs=1e-5)

    def test_45(self):
        assert coseno(45) == pytest.approx(math.cos(math.radians(45)), abs=1e-5)


# --- seno ---

class TestSeno:
    def test_90(self):
        assert seno(90) == pytest.approx(1.0, abs=1e-5)

    def test_30(self):
        assert seno(30) == pytest.approx(0.5, abs=1e-5)

    def test_45(self):
        assert seno(45) == pytest.approx(math.sin(math.radians(45)), abs=1e-5)


# --- entrar ---

class TestEntrar:
    @patch('builtins.input', side_effect=['2', '1', '2', '3', '4'])
    def test_dois_pontos(self, mock_input):
        resultado = entrar()
        assert resultado == [[1.0, 2.0], [3.0, 4.0]]

    @patch('builtins.input', side_effect=['1', '5', '10'])
    def test_um_ponto(self, mock_input):
        resultado = entrar()
        assert resultado == [[5.0, 10.0]]


# --- escolher_eixo ---

class TestEscolherEixo:
    @patch('builtins.input', return_value='X')
    def test_x_maiusculo(self, mock_input):
        assert escolher_eixo() == 0

    @patch('builtins.input', return_value='x')
    def test_x_minusculo(self, mock_input):
        assert escolher_eixo() == 0

    @patch('builtins.input', return_value='Y')
    def test_y_maiusculo(self, mock_input):
        assert escolher_eixo() == 1

    @patch('builtins.input', return_value='y')
    def test_y_minusculo(self, mock_input):
        assert escolher_eixo() == 1

    @patch('builtins.input', side_effect=['z', 'X'])
    def test_entrada_invalida_e_retry(self, mock_input):
        assert escolher_eixo() == 0


# --- transformar_eixo ---

class TestTransformarEixo:
    def test_transformar_x(self):
        matriz = [[2.0, 3.0], [4.0, 5.0]]
        transformar_eixo(matriz, 0, lambda p: p[0] * 10)
        assert matriz == [[20.0, 3.0], [40.0, 5.0]]

    def test_transformar_y(self):
        matriz = [[2.0, 3.0], [4.0, 5.0]]
        transformar_eixo(matriz, 1, lambda p: p[1] + 1)
        assert matriz == [[2.0, 4.0], [4.0, 6.0]]


# --- dilatacaoXeY ---

class TestDilatacaoXeY:
    @patch('builtins.input', side_effect=['2', '1', '2', '3', '4', '3'])
    def test_dilatacao(self, mock_input):
        dilatacaoXeY()
        # pontos [1,2],[3,4] * 3 => [3,6],[9,12]
        # verificamos via mock que a funcao roda sem erro

    @patch('builtins.input', side_effect=['1', '5', '10', '2'])
    def test_dilatacao_resultado(self, mock_input, capsys):
        dilatacaoXeY()
        captured = capsys.readouterr()
        assert "10.0" in captured.out
        assert "20.0" in captured.out


# --- dilatacaoXouY ---

class TestDilatacaoXouY:
    @patch('builtins.input', side_effect=['1', '3', '4', 'Y', '2'])
    def test_dilatacao_y(self, mock_input, capsys):
        dilatacaoXouY()
        captured = capsys.readouterr()
        # y=4 * 2 = 8
        assert "8.0" in captured.out

    @patch('builtins.input', side_effect=['1', '3', '4', 'X', '2'])
    def test_dilatacao_x(self, mock_input, capsys):
        dilatacaoXouY()
        captured = capsys.readouterr()
        # x=3 * 2 = 6
        assert "6.0" in captured.out


# --- reflexaoXouY ---

class TestReflexaoXouY:
    @patch('builtins.input', side_effect=['1', '3', '4', 'Y'])
    def test_reflexao_y(self, mock_input, capsys):
        reflexaoXouY()
        captured = capsys.readouterr()
        # y=4 * -1 = -4
        assert "-4.0" in captured.out

    @patch('builtins.input', side_effect=['1', '3', '4', 'X'])
    def test_reflexao_x(self, mock_input, capsys):
        reflexaoXouY()
        captured = capsys.readouterr()
        # x=3 * -1 = -3
        assert "-3.0" in captured.out


# --- rotacao ---

class TestRotacao:
    @patch('builtins.input', side_effect=['1', '1', '0', '90'])
    def test_rotacao_90_graus(self, mock_input, capsys):
        rotacao()
        captured = capsys.readouterr()
        # (1,0) rotacionado 90 graus => (0, 1)
        assert "0" in captured.out
        assert "1" in captured.out

    @patch('builtins.input', side_effect=['1', '1', '0', '180'])
    def test_rotacao_180_graus(self, mock_input, capsys):
        rotacao()
        captured = capsys.readouterr()
        # (1,0) rotacionado 180 graus => (-1, 0)
        assert "-1" in captured.out


# --- cisalhamento ---

class TestCisalhamento:
    @patch('builtins.input', side_effect=['1', '1', '0', 'X', '2'])
    def test_cisalhamento_x(self, mock_input, capsys):
        cisalhamento()
        captured = capsys.readouterr()
        # x = x + cisa*y = 1 + 2*0 = 1, y stays 0
        assert "1.0" in captured.out

    @patch('builtins.input', side_effect=['1', '0', '1', 'Y', '3'])
    def test_cisalhamento_y(self, mock_input, capsys):
        cisalhamento()
        captured = capsys.readouterr()
        # y = y + cisa*x = 1 + 3*0 = 1, x stays 0
        assert "1.0" in captured.out

    @patch('builtins.input', side_effect=['1', '2', '3', 'Y', '4'])
    def test_cisalhamento_y_com_valores(self, mock_input, capsys):
        cisalhamento()
        captured = capsys.readouterr()
        # y = 3 + 4*2 = 11
        assert "11.0" in captured.out
