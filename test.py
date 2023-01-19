import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):#метод -инициация приложения калькулятор
        self.calc = Calculator
    def test_adding_success(self):#1й метод тест(сложение)
        assert self.calc.adding(self, 4, 4) == 8 #вызываем из калькулятора метод adding
    def test_division_success(self):#1й метод тест(деление)
        assert self.calc.division(self, 4, 4) == 1 #вызываем из калькулятора метод division
    def test_multiply_success(self):
        assert self.calc.multiply(self, 4, 4) == 16  # вызываем из калькулятора метод multiply
    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 4, 4) == 0  # вызываем из калькулятора метод subtraction
    def test_adding_unsuccess(self):#2й метод неуспешный тест(сложение)
        assert self.calc.adding(self, 1, 1) == 3
    def test_zero_division(self):  #тест деления на ноль
        with pytest.raises(ZeroDivisionError):#стандартное исключение
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')
# def test_sum():#тест без класса
#     assert 2+2==4

# def sum (x,y):#тест без класса
#     return x+y
# def test_sum():#тест без класса
#     assert sum(1,2)==3