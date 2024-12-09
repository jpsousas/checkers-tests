import pytest
from unittest.mock import Mock
from utils import get_position_with_row_col
from piece import Piece


# Mock básico para o objeto Board
class MockBoard:
    def __init__(self, color_up=True):
        self.color_up = color_up
    
    def get_col_number(self, position):
        # Exemplo de mapeamento: posição numérica para coluna (0 a 7)
        return (position - 1) % 8

    def get_row_number(self, position):
        # Exemplo de mapeamento: posição numérica para linha (0 a 7)
        return (position - 1) // 8

    def get_color_up(self):
        return 'W' if self.color_up else 'B'

    def has_piece(self, position):
        return False  # Por padrão, nenhuma peça no tabuleiro.

    def get_pieces_by_coords(self, *coords):
        return [None for _ in coords]  # Todas as coordenadas estão vazias.

@pytest.fixture
def mock_board():
    return MockBoard()

def test_piece_initialization():
    piece = Piece("16WN")
    assert piece.get_name() == "16WN"
    assert piece.get_position() == "16"
    assert piece.get_color() == "W"
    assert not piece.get_has_eaten()
    assert not piece.is_king()

def test_set_position():
    piece = Piece("16WN")
    piece.set_position("24")
    assert piece.get_position() == "24"

def test_set_is_king():
    piece = Piece("16WN")
    piece.set_is_king(True)
    assert piece.is_king()
    assert piece.get_name() == "16WY"

def test_set_has_eaten():
    piece = Piece("16WN")
    piece.set_has_eaten(True)
    assert piece.get_has_eaten()

def test_get_adjacent_squares_king(mock_board):
    piece = Piece("16WY")  # Peça é uma dama (rei).
    adj_squares = piece.get_adjacent_squares(mock_board)
    assert len(adj_squares) == 2  # Todas as direções diagonais são válidas.

def test_get_adjacent_squares_non_king(mock_board):
    piece = Piece("16WN")  # Peça não é uma dama.
    adj_squares = piece.get_adjacent_squares(mock_board)
    assert len(adj_squares) == 1  # Apenas duas direções diagonais.

''' def test_get_moves_no_obstacles(mock_board):
    piece = Piece("16WN")
    moves = piece.get_moves(mock_board)
    assert len(moves) == 2  # Duas casas vazias para mover.
    assert all(not move["eats_piece"] for move in moves)

def test_get_moves_with_obstacles(mock_board):
    # Mockando a presença de uma peça adversária
    mock_board.get_pieces_by_coords = Mock(return_value=[Piece("24BN"), None])
    piece = Piece("16WN")
    moves = piece.get_moves(mock_board)
    assert len(moves) == 1  # Apenas uma jogada disponível (comer a peça).
    assert moves[0]["eats_piece"]

def test_get_moves_with_blocked_obstacles(mock_board):
    # Mockando um cenário onde uma peça está bloqueada
    mock_board.has_piece = Mock(return_value=True)
    piece = Piece("16WN")
    moves = piece.get_moves(mock_board)
    assert len(moves) == 0  # Nenhum movimento possível.
'''