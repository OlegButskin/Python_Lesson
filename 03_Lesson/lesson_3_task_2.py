from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79123456789"),
    Smartphone("Samsung", "Galaxy S23", "+79241235566"),
    Smartphone("Sony", "Xperia Z4", "+79345678901"),
    Smartphone("Google", "Pixel 7 Pro", "+79456789012"),
    Smartphone("OnePlus", "11 Pro", "+79567890123")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")