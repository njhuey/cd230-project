import calc


def test_add() -> None:
    x, y = 5, 7
    assert calc.add(x, y) == 12
