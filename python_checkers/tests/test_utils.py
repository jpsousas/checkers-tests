from python_checkers.utils import *

def test_get_position_with_row_col():
    assert get_position_with_row_col(0, 0) == 0 #((0*4)+(0//2)) =0 
    assert get_position_with_row_col(0, 1) == 0  #((0*4)+(1//2)) = 0
    assert get_position_with_row_col(1, 0) == 4  # ((1*4)(0//2)) = 4
    assert get_position_with_row_col(1, 2) == 5  # ((1*4)+(2//2))= 5
    assert get_position_with_row_col(3, 5) == 14  # #((3*4)+(5//2)) = 15
    
def test_get_piece_position():
    #deve retornar um valor de 0-31 para representar um peao na list de peoes do GUI
    #obtendo os valores fornecidos no proprio jogo
    square_dist = 56
    top_left_coords = (34,34)
    assert get_piece_position((100,100),square_dist, top_left_coords) == 4 
    assert get_piece_position((150,100),square_dist,top_left_coords) == 5 
    assert get_piece_position((50,50),square_dist,top_left_coords) == 0
    assert get_piece_position((200,200),square_dist,top_left_coords) == 9 
    assert get_piece_position((300,300),square_dist,top_left_coords) == 18 

def test_get_piece_gui_coords():
    square_dist = 50
    top_left_coords = (34,34)
    assert get_piece_gui_coords((7, 3), square_dist, top_left_coords) == (184, 384)
    assert get_piece_gui_coords((8, 0), square_dist, top_left_coords) == (34, 434)
    assert get_piece_gui_coords((6, 6), square_dist, top_left_coords) == (334, 334) 
    assert get_piece_gui_coords((9, 9), square_dist, top_left_coords) == (484, 484)

def test_get_surface_mouse_offset():
    assert get_surface_mouse_offset((314, 426), (41, 41)) == (-19, -17) # posicao existe
    assert get_surface_mouse_offset((200, 200), (150, 150)) == (50, 50) # posicao nao existe propriamente dito
    assert get_surface_mouse_offset((0, 0), (0, 0)) == (0, 0)