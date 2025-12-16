from task_a.task_a import square_area, fib


def test_square_area():
    assert square_area(5) == 25
    assert square_area(0) == 0


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(5) == 5
    assert fib(10) == 55

