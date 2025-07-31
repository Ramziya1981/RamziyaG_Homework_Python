def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


# Пример №1
year_to_check = 2024
result = is_year_leap(year_to_check)

print(f"год{year_to_check}:{result}")

# Пример №2
year_to_check = 2023
result = is_year_leap(year_to_check)

print(f"год{year_to_check}:{result}")
