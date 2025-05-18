from HW20_testing.utils import Fibonacci
import pytest

fibonacci = Fibonacci()

@pytest.mark.parametrize(
    'input_arg ,expected',
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (100, 354224848179261915075)
    ]
)
def test_fibonacci_valid(input_arg, expected):
    assert fibonacci(input_arg) == expected


@pytest.mark.parametrize(
    'input_arg',
    (-1, -100, 'str', 1.5, [], {}, fibonacci, None,)
)
def test_fibonacci_invalid(input_arg):
    with pytest.raises(ValueError):
        fibonacci(input_arg)
