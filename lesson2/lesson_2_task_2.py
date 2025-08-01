def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


year = int(input("Введите год: "))
isVisokosny = is_year_leap(year)
print(f"Год: {year} : {isVisokosny}")
