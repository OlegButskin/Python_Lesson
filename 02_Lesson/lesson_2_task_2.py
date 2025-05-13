def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = 2000
result = is_year_leap(year)
print(f"год {year}: {result}")

year = 1900
print(f"год {year}: {is_year_leap(year)}")