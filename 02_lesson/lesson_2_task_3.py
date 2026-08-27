import math


def square(side):
    return math.ceil(side ** 2)


side_square = float(input("Введите сторону квадрата:"))
result = square(side_square)
print(f"Площадь квадрата:{result}")
