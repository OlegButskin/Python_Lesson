def month_to_season(month):
    if month in (12, *range(1, 3)):  
        return "Зима"
    elif month in range(3, 6):       
        return "Весна"
    elif month in range(6, 9):      
        return "Лето"
    elif month in range(9, 12):      
        return "Осень"
    
print(month_to_season(2))
