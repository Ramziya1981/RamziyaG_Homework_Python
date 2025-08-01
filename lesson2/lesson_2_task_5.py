def month_to_seasonar(month):
    if month < 1 or month > 12:
        return "Неверный номер месяца"
    elif month in [12, 1, 2]:
        return "зима"
    elif month in [3, 4, 5]:
        return "весна"
    elif month in [6, 7, 8]:
        return "лето"
    elif month in [9, 10, 11]:
        return "осень"


try:
    month = int(input("Введите номер месяца (1-12): "))
    print(month_to_seasonar(month))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")
