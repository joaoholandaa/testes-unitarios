from faker import Faker
from .calculadora import Calculadora
from .operations.test.add import AddOperationSpy
from .operations.test.sub import SubOperationSpy

fake = Faker()

def test_add():
  addOperation = AddOperationSpy()
  calculadora = Calculadora(addOperation, SubOperationSpy())

  number1 = fake.random_number()
  number2 = fake.random_number()

  result = calculadora.add(number1, number2, True)

  # Teste de entrada
  assert addOperation.soma_attributer['number1'] == number1
  assert addOperation.soma_attributer['number2'] == number2

  # Teste de saída
  assert result is not None

def test_add_none():
  addOperation = AddOperationSpy()
  calculadora = Calculadora(addOperation, SubOperationSpy())

  number1 = fake.random_number()
  number2 = fake.random_number()

  result = calculadora.add(number1, number2, False)

  # Teste de entrada
  assert addOperation.soma_attributer == {}

  # Teste de saída
  assert result is None