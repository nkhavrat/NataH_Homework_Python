def month_to_season(month):
    if 1 <= month <= 2 or month == 12:
        return "Зима"
    if 3 <= month <= 5:
        return "Весна"
    if 6 <= month <= 8:
        return "Лето"
    if 9 <= month <= 11:
        return "Осень"
    else:
        "Неверный номер месяца"


match = int(input("Введите номер месяца (1-12):"))
print(month_to_season(match))
