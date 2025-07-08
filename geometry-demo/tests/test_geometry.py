import pytest
from geometry import Square, Circle, Shape, area_stats

def test_square_area_zero_and_positive():
    zero = Square(0)
    two  = Square(2)
    assert zero.area() == pytest.approx(0)
    assert two.area() == pytest.approx(4)

def test_circle_area_zero_and_positive():
    c0 = Circle(0)
    c1 = Circle(1)
    assert c0.area() == pytest.approx(0)
    assert c1.area() == pytest.approx(3.141592653589793)

def test_stats_keys_and_values():
    shapes = [Square(1), Circle(1)]
    stats = area_stats(*shapes)

    expected_keys = {"n", "total", "mean", "min", "max"}
    assert set(stats.keys()) == expected_keys
    assert all(isinstance(v, (int, float)) for v in stats.values())

def test_stats_raises_without_shapes():
    with pytest.raises(ValueError):
        area_stats()
