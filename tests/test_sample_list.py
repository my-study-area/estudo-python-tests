import pytest
from src.tutorial4parametrize.sample_list import add


def test_sample_list():
  result = add([1,2], [3])
  assert result == [1, 2, 3]


@pytest.mark.parametrize("a,b,c", [(1, 2, 3), ("a", "b", "ab"), ([1, 2], [3], [1, 2, 3])],
                         ids=["num", "str", "list"])
def test_sample_list_parametrize_ids(a, b, c):
  result = add(a, b)
  print(result)
  assert result == c


@pytest.mark.parametrize("a,b,c", [(1, 2, 3), ("a", "b", "ab"), ([1, 2], [3], [1, 2, 3])])
def test_sample_list_parametrize(a, b, c):
  result = add(a, b)
  print(result)
  assert result == c
