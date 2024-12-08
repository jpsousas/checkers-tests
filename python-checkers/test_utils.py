import pytest
from utils import get_position_with_row_col, get_piece_position, get_piece_gui_coords, get_surface_mouse_offset

def test_get_position_with_row_col():
    assert get_position_with_row_col(0, 0) == 0  # Top-left corner
    assert get_position_with_row_col(1, 0) == 4  # Second row, first column
    assert get_position_with_row_col(2, 2) == 10  # Third row, third column
    assert get_position_with_row_col(7, 7) == 31  # Bottom-right corner

def test_get_piece_position():
    square_dist = 50
    top_left_coords = (100, 100)
    
    coords = (150, 150)  # Center of the first square (row 1, col 1)
    assert get_piece_position(coords, square_dist, top_left_coords) == 5
    
    coords = (200, 200)  # Center of the square (row 2, col 2)
    assert get_piece_position(coords, square_dist, top_left_coords) == 10

def test_get_piece_gui_coords():
    square_dist = 50
    top_left_coords = (100, 100)
    
    coords = (1, 1)  # Row 1, Column 1
    expected_coords = (200, 150)  # Expected GUI coordinates
    assert get_piece_gui_coords(coords, square_dist, top_left_coords) == expected_coords

    coords = (2, 2)  # Row 2, Column 2
    expected_coords = (200, 200)  # Expected GUI coordinates
    assert get_piece_gui_coords(coords, square_dist, top_left_coords) == expected_coords

def test_get_surface_mouse_offset():
    surface_pos = (300, 400)
    mouse_pos = (250, 350)
    assert get_surface_mouse_offset(surface_pos, mouse_pos) == (50, 50)

    surface_pos = (500, 600)
    mouse_pos = (550, 650)
    assert get_surface_mouse_offset(surface_pos, mouse_pos) == (-50, -50)

