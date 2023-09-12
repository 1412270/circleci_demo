from main import *


def test_add():
    assert add(2, 3) == 5
    assert multi(5, 5) == 11
    print("Add function works correctly")


if __name__ == '__main__':
    test_add()
