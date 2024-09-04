from src.math_operations import add,sub

def test_add():
    assert add(5,2)==7
    assert add(1,2)==3

def test_sub():
    assert sub(5,2)==3
    assert sub(2,2)==0