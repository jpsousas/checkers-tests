import pytest
from unittest.mock import MagicMock, patch
from board_gui import BoardGUI
import pygame

@pytest.fixture
def mock_board():
    """Mocka um tabuleiro genérico com métodos necessários."""
    board = MagicMock()
    board.get_pieces.return_value = [
        MagicMock(get_position=lambda: "12", get_color=lambda: "B", is_king=lambda: False),
        MagicMock(get_position=lambda: "14", get_color=lambda: "W", is_king=lambda: True),
    ]
    board.get_row_number.side_effect = lambda pos: int(pos) // 4
    board.get_col_number.side_effect = lambda pos: (int(pos) % 4) * 2
    return board

@pytest.fixture
def mock_display_surface():
    """Mocka uma superfície do Pygame para simular a tela."""
    return MagicMock()

@pytest.fixture
def board_gui(mock_board):
    """Cria uma instância do BoardGUI com um tabuleiro mockado."""
    return BoardGUI(mock_board)


def test_get_piece_properties(board_gui, mock_board):
    pieces = board_gui.get_piece_properties(mock_board)
    assert len(pieces) == len(mock_board.get_pieces())
    assert all("rect" in piece for piece in pieces)
    assert all("color" in piece for piece in pieces)
    assert all("is_king" in piece for piece in pieces)


def test_get_piece_by_index(board_gui):
    piece = board_gui.get_piece_by_index(0)
    assert "rect" in piece
    assert "color" in piece
    assert "is_king" in piece


def test_hide_and_show_piece(board_gui):
    board_gui.hide_piece(0)
    assert board_gui.hidden_piece == 0

    revealed_piece = board_gui.show_piece()
    assert revealed_piece == 0
    assert board_gui.hidden_piece == -1


def test_get_piece_on_mouse(board_gui):
    # Simula um clique no retângulo da primeira peça
    rect = board_gui.pieces[0]["rect"]
    mouse_pos = (rect.x + 10, rect.y + 10)

    result = board_gui.get_piece_on_mouse(mouse_pos)
    assert result["index"] == 0
    assert result["piece"] == board_gui.pieces[0]

    # Simula um clique fora de qualquer peça
    assert board_gui.get_piece_on_mouse((0, 0)) is None


def test_set_and_get_move_marks(board_gui):
    board_gui.set_move_marks([(0, 0), (1, 1)])
    move_marks = board_gui.get_move_marks()

    assert len(move_marks) == 2
    assert all(isinstance(mark, pygame.Rect) for mark in move_marks)


@patch("board_gui.get_piece_position", return_value=(1, 2))
def test_get_position_by_rect(mock_get_position, board_gui):
    rect = pygame.Rect(10, 10, 44, 44)
    position = board_gui.get_position_by_rect(rect)

    mock_get_position.assert_called_once_with((10, 10), 56, (34, 34))
    assert position == (1, 2)

'''@patch("board_gui.BLACK_PIECE_SURFACE", MagicMock(name="BLACK_PIECE_SURFACE"))
@patch("board_gui.WHITE_PIECE_SURFACE", MagicMock(name="WHITE_PIECE_SURFACE"))
@patch("board_gui.BLACK_KING_PIECE_SURFACE", MagicMock(name="BLACK_KING_PIECE_SURFACE"))
@patch("board_gui.WHITE_KING_PIECE_SURFACE", MagicMock(name="WHITE_KING_PIECE_SURFACE"))
def test_get_surface(mock_black_king, mock_white_king, mock_black_piece, mock_white_piece, board_gui):
    piece_black = MagicMock()  # Simula uma peça preta não coroada
    piece_black.get_color.return_value = "B"
    piece_black.is_king.return_value = False

    piece_white_king = MagicMock()  # Simula uma peça branca coroada
    piece_white_king.get_color.return_value = "W"
    piece_white_king.is_king.return_value = True

    # Testa peça preta
    surface_black = board_gui.get_surface(piece_black)
    assert surface_black == mock_black_piece

    # Testa peça branca coroada
    surface_white_king = board_gui.get_surface(piece_white_king)
    assert surface_white_king == mock_white_king

    @patch("board_gui.BOARD", MagicMock(name="BOARD"))
@patch("board_gui.MOVE_MARK", MagicMock(name="MOVE_MARK"))
def test_draw_board(mock_board_surface, mock_move_mark, board_gui, mock_display_surface):
    # Configura as marcas de movimento
    board_gui.set_move_marks([(0, 0), (1, 1)])
    board_gui.draw_board(mock_display_surface)

    # Verifica chamadas do blit
    mock_display_surface.blit.assert_any_call(mock_board_surface, (26, 26))
    assert mock_display_surface.blit.call_count > 1  # Deve incluir BOARD + MOVE_MARKs

    # Adiciona logs para análise
    print(mock_display_surface.blit.call_args_list)

    @patch("board_gui.BLACK_PIECE_SURFACE", MagicMock(name="BLACK_PIECE_SURFACE"))
@patch("board_gui.WHITE_PIECE_SURFACE", MagicMock(name="WHITE_PIECE_SURFACE"))
@patch("board_gui.BLACK_KING_PIECE_SURFACE", MagicMock(name="BLACK_KING_PIECE_SURFACE"))
@patch("board_gui.WHITE_KING_PIECE_SURFACE", MagicMock(name="WHITE_KING_PIECE_SURFACE"))
def test_draw_pieces(mock_black_piece, mock_white_piece, mock_black_king, mock_white_king, board_gui, mock_display_surface):
    board_gui.draw_pieces(mock_display_surface)

    # Verifica se as superfícies corretas foram desenhadas
    mock_display_surface.blit.assert_any_call(mock_black_piece, board_gui.pieces[0]["rect"])
    mock_display_surface.blit.assert_any_call(mock_white_king, board_gui.pieces[1]["rect"])

    # Adiciona logs para debug (se necessário)
    print(mock_display_surface.blit.call_args_list)
'''