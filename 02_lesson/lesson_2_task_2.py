def is_year_leap(number):
    return True if number % 4 == 0 and number % 100 != 0 or number % 400 == 0\
        else False


num = int(input("Ввeдите год :"))
result = is_year_leap(num)
print(f"Высокосный год {num}?: {result}")
