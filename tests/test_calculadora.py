from  src.tutorial1.calculadora import sum

def test_a():
  total = sum(2, 1)
  assert total == 3

def test_b():
  total = sum('2', '1')
  assert total == '21'
