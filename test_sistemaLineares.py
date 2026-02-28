from unittest.mock import patch
import pytest
from sistemaLineares import resolver_sistema


class TestResolverSistema:
    @patch('builtins.input', side_effect=[
        '2',        # matriz 2x2
        '1', '0',   # linha 1: [1, 0]
        '0', '1',   # linha 2: [0, 1]
        '5', '3',   # resultado: [5, 3]
    ])
    def test_identidade_2x2(self, mock_input, capsys):
        resolver_sistema()
        captured = capsys.readouterr()
        # I * [x, y] = [5, 3] => x=5, y=3
        assert "5." in captured.out
        assert "3." in captured.out

    @patch('builtins.input', side_effect=[
        '2',        # matriz 2x2
        '2', '1',   # linha 1: [2, 1]
        '1', '3',   # linha 2: [1, 3]
        '5', '10',  # resultado: [5, 10]
    ])
    def test_sistema_2x2(self, mock_input, capsys):
        resolver_sistema()
        captured = capsys.readouterr()
        # 2x + y = 5, x + 3y = 10 => x=1, y=3
        assert "1." in captured.out
        assert "3." in captured.out

    @patch('builtins.input', side_effect=[
        '3',                    # matriz 3x3
        '1', '0', '0',         # linha 1
        '0', '1', '0',         # linha 2
        '0', '0', '1',         # linha 3
        '7', '8', '9',         # resultado
    ])
    def test_identidade_3x3(self, mock_input, capsys):
        resolver_sistema()
        captured = capsys.readouterr()
        assert "7." in captured.out
        assert "8." in captured.out
        assert "9." in captured.out
