class Binary:
    def __init__(self, num):  # инициализация объекта Binary (num - число в 10 сс)
        self.num = 0
        n = 0
        while num != 0:
            self.num += ((num % 10) * (2 ** n))
            num = num // 10
            n += 1

    def __add__(self, other):  # сложение объекта Binary и other
        return translation(self.num + other.num)

    def __sub__(self, other):  # вычитание other из объекта Binary
        return translation(self.num - other.num)

    def __mul__(self, other):  # умножение объекта Binary на other
        return translation(self.num * other.num)

    def __floordiv__(self, other):  # целочисленное деление объекта Binary на other
        return translation(self.num // other.num)

    def __str__(self):  # конвертирование объекта Binary в строку
        return '{} '.format(self)


def translation(number):
    n = 0
    output = 0
    while number != 0:
        output = (number % 2) * (10 ** n) + output
        number = number // 2
        n += 1
    return output


x = int(input("Введите первое число в двоичной системемe счисления: "))
y = int(input("Введите второе число в двоичной системемe счисления: "))
a = Binary(x)
b = Binary(y)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
