import pytest
from unittest.mock import MagicMock, patch
from game_control import GameControl

@pytest.fixture
def mock_board():
    """Mocka o objeto Board."""
    board = MagicMock()
    board.get_pieces.return_value = []
    board.get_winner.return_value = None
    return board

@pytest.fixture
def mock_board_gui():
    """Mocka o objeto BoardGUI."""
    board_gui = MagicMock()
    board_gui.get_piece_on_mouse.return_value = None
    board_gui.get_move_marks.return_value = []
    board_gui.get_position_by_rect.return_value = None
    return board_gui

@pytest.fixture
def mock_held_piece():
    """Mocka o objeto HeldPiece."""
    return MagicMock()

@pytest.fixture
def mock_ai():
    """Mocka o objeto AI."""
    ai = MagicMock()
    ai.get_move.return_value = {"position_from": "12", "position_to": "21"}
    return ai

@patch("game_control.Board", autospec=True)
@patch("game_control.BoardGUI", autospec=True)
@patch("game_control.HeldPiece", autospec=True)
@patch("game_control.AI", autospec=True)
def test_initialization(mock_ai_class, mock_held_piece_class, mock_board_gui_class, mock_board_class, mock_board, mock_board_gui, mock_ai):
    """Testa a inicialização da classe GameControl."""
    mock_board_class.return_value = mock_board
    mock_board_gui_class.return_value = mock_board_gui
    mock_ai_class.return_value = mock_ai

    game_control = GameControl("W", is_computer_opponent=True)
    
    assert game_control.turn == "W"
    assert game_control.winner is None
    assert game_control.ai_control is not None
    mock_board_class.assert_called_once()
    mock_board_gui_class.assert_called_once()

def test_hold_piece(mock_board_gui, mock_board):
    """Testa a lógica ao pegar uma peça com o mouse."""
    mock_piece_data = {"piece": {"color": "W"}, "index": 0}
    mock_board_gui.get_piece_on_mouse.return_value = mock_piece_data
    mock_board.get_pieces.return_value = [MagicMock(get_moves=lambda board: [{"position": "12", "eats_piece": False}])]
    mock_board.get_row_number.return_value = 1
    mock_board.get_col_number.return_value = 1

    game_control = GameControl("W", is_computer_opponent=False)
    game_control.board = mock_board
    game_control.board_draw = mock_board_gui

    game_control.hold_piece((100, 100))

    mock_board_gui.set_move_marks.assert_called_once_with([(1, 1)])
    mock_board_gui.hide_piece.assert_called_once_with(0)

def test_release_piece(mock_board_gui, mock_board):
    """Testa a lógica ao soltar uma peça."""
    mock_board_gui.get_move_marks.return_value = [(1, 1)]
    mock_board_gui.get_position_by_rect.return_value = 12
    mock_board_gui.show_piece.return_value = 0
    mock_board.get_piece_by_index.return_value = MagicMock(get_moves=lambda board: [])
    mock_board.get_winner.return_value = None

    game_control = GameControl("W", is_computer_opponent=False)
    game_control.board = mock_board
    game_control.board_draw = mock_board_gui
    game_control.held_piece = MagicMock()

    game_control.release_piece()

    mock_board.move_piece.assert_called_once_with(0, 12)
    mock_board_gui.set_pieces.assert_called_once()
    assert game_control.turn == "B"

def test_move_ai(mock_board, mock_board_gui, mock_ai):
    """Testa a lógica do movimento da IA."""
    mock_board.get_pieces.return_value = [
        MagicMock(get_position=lambda: "12"),
        MagicMock(get_position=lambda: "15")
    ]
    mock_board_gui.get_piece_properties.return_value = []
    mock_board.get_winner.return_value = None

    game_control = GameControl("B", is_computer_opponent=True)
    game_control.board = mock_board
    game_control.board_draw = mock_board_gui
    game_control.ai_control = mock_ai

    game_control.move_ai()

    mock_ai.get_move.assert_called_once_with(mock_board)
    mock_board.move_piece.assert_called_once_with(0, 21)
    mock_board_gui.set_pieces.assert_called_once()
    assert game_control.turn == "W"

def test_get_turn_and_winner():
    """Testa os métodos get_turn e get_winner."""
    game_control = GameControl("W", is_computer_opponent=False)
    game_control.turn = "B"
    game_control.winner = "W"

    assert game_control.get_turn() == "B"
    assert game_control.get_winner() == "W"
