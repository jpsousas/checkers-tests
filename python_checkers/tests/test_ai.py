import pytest
import pygame
from python_checkers.ai import AI
from python_checkers.board import Board

def test_AI_init():
    black='B'
    white='W'

    first_ai_instance = AI(black)
    second_ai_instance = AI(white)
    assert first_ai_instance.color == black
    assert second_ai_instance.color == white
