import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        # Менше 15 років
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        # Від 15 до 23 років
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        # 24 роки (рівно 2)
        (24, 24, [2, 2]),
        # Крок для котів (+1 за кожні 4 роки після 24)
        (27, 24, [2, 2]),
        (28, 24, [3, 2]),
        # Крок для собак (+1 за кожні 5 років після 24)
        (24, 28, [2, 2]),
        (24, 29, [2, 3]),
        # Великі значення
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
