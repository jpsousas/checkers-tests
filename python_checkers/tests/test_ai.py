import pytest
import pygame
from python_checkers.ai import AI
from python_checkers.board import Board
from unittest.mock import MagicMock, patch


def test_AI_init():
    black='B'
    white='W'

    first_ai_instance = AI(black)
    second_ai_instance = AI(white)
    assert first_ai_instance.color == black
    assert second_ai_instance.color == white

@pytest.fixture
def mock_board():
    """Mocka o objeto Board."""
    board = MagicMock()
    board.get_winner.return_value = None
    board.get_pieces.return_value = []
    board.get_color_up.return_value = "W"
    return board

@pytest.fixture
def mock_piece():
    """Mocka o objeto Piece."""
    piece = MagicMock()
    piece.get_moves.return_value = [{"position": "21", "eats_piece": False}]
    piece.get_color.return_value = "W"
    piece.get_position.return_value = "12"
    return piece

def test_get_value_win(mock_board):
    """Testa o método get_value quando o AI vence."""
    ai = AI("W")
    mock_board.get_winner.return_value = "W"
    mock_board.get_pieces.return_value = [MagicMock(get_color=lambda: "W")]

    assert ai.get_value(mock_board) == 2

def test_get_value_loss(mock_board):
    """Testa o método get_value quando o AI perde."""
    ai = AI("W")
    mock_board.get_winner.return_value = "B"
    mock_board.get_pieces.return_value = [MagicMock(get_color=lambda: "B")]

    assert ai.get_value(mock_board) == -2

def test_get_value_draw(mock_board):
    """Testa o método get_value quando há empate."""
    ai = AI("W")
    mock_board.get_winner.return_value = None
    mock_board.get_pieces.return_value = [
        MagicMock(get_color=lambda: "W"),
        MagicMock(get_color=lambda: "B")
    ]

    assert ai.get_value(mock_board) == 0

def test_get_value_advantage(mock_board):
    """Testa o método get_value quando o AI tem mais peças."""
    ai = AI("W")
    mock_board.get_winner.return_value = None
    mock_board.get_pieces.return_value = [
        MagicMock(get_color=lambda: "W"),
        MagicMock(get_color=lambda: "W"),
        MagicMock(get_color=lambda: "B")
    ]

    assert ai.get_value(mock_board) == 1

def test_get_value_disadvantage(mock_board):
    """Testa o método get_value quando o adversário tem mais peças."""
    ai = AI("W")
    mock_board.get_winner.return_value = None
    mock_board.get_pieces.return_value = [
        MagicMock(get_color=lambda: "W"),
        MagicMock(get_color=lambda: "B"),
        MagicMock(get_color=lambda: "B")
    ]

    assert ai.get_value(mock_board) == -1
