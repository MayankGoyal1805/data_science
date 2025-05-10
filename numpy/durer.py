import numpy as np

square = np.array([
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
])

def test_row():
    for i in range(4):
        assert(square[i, :].sum()) == 34

def test_col():
    for i in range(4):
        assert(square[:, i].sum()) == 34

def test_top_left():
    assert(square[:2,:2].sum()) == 34

def test_bottom_left():
    assert(square[2:,:2].sum()) == 34

def test_top_right():
    assert(square[:2,2:].sum()) == 34

def test_bottom_right():
    assert(square[2:,2:].sum()) == 34   

def test_corners():
    assert(square[0,0]+square[3,0]+square[3,3]+square[0,3]) == 34

def test_center_four():
    assert(square[1,1]+square[1,2]+square[2,2]+square[2,1]) == 34  