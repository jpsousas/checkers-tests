import pygame
import pytest
from unittest.mock import MagicMock
from python_checkers.held_piece import HeldPiece

def test_held_piece_init():
    # mocka um objeto de Heldpiece pra testar 
    surface = MagicMock()
    surface.get_rect.return_value = pygame.Rect(0, 0, 50, 50)  # Rect mock
    offset = (10, 20)

    piece = HeldPiece(surface, offset)

    assert piece.surface == surface
    assert piece.draw_rect == pygame.Rect(0, 0, 50, 50)
    assert piece.offset == offset

@pytest.fixture(scope='module', autouse=True)
def pygame_init():
    pygame.init()
    yield
    pygame.quit()

def test_draw_piece():
    # mocka o objeto surface
    surface = MagicMock()
    surface.get_rect.return_value = pygame.Rect(146, 34, 44, 44)
    offset = (10, 20)
    display_surface = MagicMock()

    #mocka posicao do mouse
    pygame.mouse.get_pos = MagicMock(return_value=(100, 150))

    piece = HeldPiece(surface, offset)

    piece.draw_piece(display_surface)

    # tentar exibir
    display_surface.blit.assert_called_with(surface, piece.draw_rect)

def test_check_collision():
    surface = pygame.Surface((50, 50))
    offset = (0, 0)
    piece = HeldPiece(surface, offset)

    piece.draw_rect.x = 100
    piece.draw_rect.y = 160

    rect_list = [
        pygame.Rect(100, 160, 60, 60),  # colide com a peça
        pygame.Rect(200, 200, 50, 50),  # nao colide
    ]

    collision = piece.check_collision(rect_list)

    assert collision == rect_list[0], f"Esperado {rect_list[0]}, mas recebeu {collision}."




    