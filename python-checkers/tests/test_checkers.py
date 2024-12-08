import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
import pygame as pg
from checkers import main
import sys

@pytest.fixture
def mock_pygame():
    """Inicializa e encerra o pygame para os testes."""
    pg.init()
    yield
    pg.quit()

def test_quit_event(mock_pygame):
    """Verifica se o jogo encerra quando o evento QUIT é recebido."""
    quit_event = pg.event.Event(pg.QUIT)  # Cria um evento QUIT válido
    
    with patch("pygame.event.get", return_value=[quit_event]):  # Use o evento criado
        with patch("pygame.quit") as mock_quit:
            main("pvp")
            mock_quit.assert_called_once()

def test_mouse_click_events(mock_pygame):
    """Testa cliques de mouse para pegar e soltar peças."""
    mouse_down_event = pg.event.Event(pg.MOUSEBUTTONDOWN, {"pos": (100, 100)})
    mouse_up_event = pg.event.Event(pg.MOUSEBUTTONUP)

    mock_game_control = MagicMock()

    with patch("pygame.event.get", side_effect=[
        [mouse_down_event], [mouse_up_event], [pg.event.Event(pg.QUIT)]
    ]):
        with patch("checkers.GameControl", return_value=mock_game_control):
            main("pvp")
    
    # Verifica se os métodos corretos foram chamados
    mock_game_control.hold_piece.assert_called_once_with((100, 100))
    mock_game_control.release_piece.assert_called_once()

    
def test_ai_moves_on_userevent(mock_pygame):
    """Verifica se a IA se move quando o evento USEREVENT ocorre."""
    user_event = pg.event.Event(pg.USEREVENT)

    # Mock do GameControl
    mock_game_control = MagicMock()
    mock_game_control.get_winner.return_value = None  # Sem vencedor
    mock_game_control.get_turn.return_value = "B"  # Turno da IA

    with patch("pygame.event.get", side_effect=[
        [user_event], [pg.event.Event(pg.QUIT)]
    ]):
        with patch("checkers.GameControl", return_value=mock_game_control):
            main("cpu")
    
    # Verifica se a IA foi chamada para realizar o movimento
    mock_game_control.move_ai.assert_called_once()













'''def test_turn_text_display(mock_pygame):
    """Verifica se o texto do turno é renderizado corretamente."""
    mock_game_control = MagicMock()
    mock_game_control.get_turn.side_effect = ["W", "B"]  # Simula alternância de turnos

    # Mock de pygame
    with patch("pygame.event.get", side_effect=[
        [pg.event.Event(pg.MOUSEBUTTONDOWN, {"pos": (100, 100)})],
        [pg.event.Event(pg.QUIT)]
    ]):
        with patch("checkers.GameControl", return_value=mock_game_control):
            with patch("pygame.font.SysFont") as mock_font:
                # Mock do render para retornar um MagicMock que imita um Surface
                mock_surface = MagicMock(spec=pg.Surface)
                mock_font.return_value.render = MagicMock(return_value=mock_surface)

                # Mock do método set_mode para criar uma "Surface" falsa
                mock_display = MagicMock(spec=pg.Surface)
                with patch("pygame.display.set_mode", return_value=mock_display):
                    # Chama main para que o Pygame inicialize corretamente
                    main("pvp")

                # Verifica se o texto de turno foi renderizado corretamente
                mock_font.return_value.render.assert_any_call("White's turn", True, (255, 255, 255))
                mock_font.return_value.render.assert_any_call("Black's turn", True, (255, 255, 255))
                
                # Verifica se o texto foi blitted para a tela corretamente
                mock_display.blit.assert_any_call(mock_surface, (509, 26))
'''



'''def test_winner_display(mock_pygame):
    """Verifica se o texto do vencedor é exibido corretamente."""
    mock_game_control = MagicMock()
    mock_game_control.get_winner.return_value = "W"

    with patch("pygame.event.get", return_value=[pg.event.Event(pg.QUIT)]):
        with patch("checkers.GameControl", return_value=mock_game_control):
            with patch("pygame.font.SysFont") as mock_font:
                mock_font.return_value.render = MagicMock()

                main("pvp")

                # Verifica se o texto de vitória foi renderizado
                mock_font.return_value.render.assert_any_call("White wins!", True, (255, 255, 255))
'''


