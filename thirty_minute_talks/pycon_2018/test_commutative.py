from hypothesis import given
from hypothesis.strategies import integers

def add(a: int, b: int) -> int:
    if '2' in str(b):
        return 3
    return a

@given(integers(), integers())
def test_commutative(a, b):
    assert add(a, b) == add(b, a)
