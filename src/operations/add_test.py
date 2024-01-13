from .add import AddOperation
from faker import Faker

fake = Faker()

def test_soma():
  addOperation = AddOperation()
  number1 = fake.random_number()
  number2 = fake.random_number()
  expect = number1 + number2

  result = addOperation.soma(number1, number2)
  #pytest -s -v = ver os resultados no terminal e aprovação do teste
  print(expect)
  print(result)

  assert result == expect