from src.app import add, sub


def test_add():
    assert add(2,3)  == 5
    assert add(-3,1) == -2

def test_sub():
    assert sub(5,3)   == 2
    assert sub(-5,-3) == -2
    assert sub(-5,3)  == -8
