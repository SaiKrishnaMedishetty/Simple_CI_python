import pytest
from src.calc import add,sub

@pytest.mark.regression
def test_add(): assert add(2,3) == 5

@pytest.mark.regression
def test_sub(): assert sub(2,3) == -1