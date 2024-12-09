import pytest
from unittest.mock import MagicMock
from board import Board

@pytest.fixture
def mock_piece():
    """Mocka uma peça genérica."""
    piece = MagicMock()
    piece.get_position.return_value = "12"
    piece.get_color.return_value = "W"
    piece.is_king.return_value = False
    return piece

@pytest.fixture
def mock_pieces(mock_piece):
    """Mocka uma lista de peças."""
    return [mock_piece for _ in range(5)]

@pytest.fixture
def board_with_mocked_pieces(mock_pieces):
    """Cria um tabuleiro com peças mockadas."""
    return Board(mock_pieces, "W")

def test_get_color_up(board_with_mocked_pieces):
    assert board_with_mocked_pieces.get_color_up() == "W"

def test_get_pieces(board_with_mocked_pieces, mock_pieces):
    assert board_with_mocked_pieces.get_pieces() == mock_pieces

def test_get_piece_by_index(board_with_mocked_pieces, mock_pieces):
    assert board_with_mocked_pieces.get_piece_by_index(0) == mock_pieces[0]

def test_has_piece(board_with_mocked_pieces, mock_piece):
    mock_piece.get_position.return_value = "12"
    assert board_with_mocked_pieces.has_piece(12) is True
    assert board_with_mocked_pieces.has_piece(25) is False

def test_get_row_number(board_with_mocked_pieces):
    assert board_with_mocked_pieces.get_row_number(1) == 0
    assert board_with_mocked_pieces.get_row_number(8) == 2

'''def test_get_col_number(board_with_mocked_pieces):
    assert board_with_mocked_pieces.get_col_number(1) == 0
    assert board_with_mocked_pieces.get_col_number(9) == 2
    assert board_with_mocked_pieces.get_col_number(14) == 7

    def test_get_pieces_by_coords(board_with_mocked_pieces, mock_piece):
    mock_piece.get_position.return_value = "12"
    assert board_with_mocked_pieces.get_pieces_by_coords((3, 2)) == [mock_piece]
    assert board_with_mocked_pieces.get_pieces_by_coords((1, 1)) == [None]

    def test_move_piece(board_with_mocked_pieces, mock_piece):
    mock_piece.get_position.return_value = "12"
    mock_piece.get_color.return_value = "W"
    mock_piece.set_position = MagicMock()

    board_with_mocked_pieces.move_piece(0, "20")

    mock_piece.set_position.assert_called_with("20")

    def test_get_winner_no_winner(board_with_mocked_pieces, mock_pieces):
    mock_pieces[0].get_color.return_value = "W"
    mock_pieces[1].get_color.return_value = "B"
    assert board_with_mocked_pieces.get_winner() is None

'''
def test_get_row(board_with_mocked_pieces, mock_piece):
    mock_piece.get_position.return_value = "12"
    assert len(board_with_mocked_pieces.get_row(3)) == 1



def test_get_winner_single_color(board_with_mocked_pieces, mock_pieces):
    for piece in mock_pieces:
        piece.get_color.return_value = "W"
    assert board_with_mocked_pieces.get_winner() == "W"

