from address import Address
from mailing import Mailing

to_address = Address("353440", "Анапа", "Центарльная", "15", "")
from_address = Address("123456", "Москва", "Ленина", "1", "101")

mail = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350,
    track="RU123456789CN"
)


print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, "
      f"{mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, "
      f"{mail.to_address.house} - {mail.to_address.apartment}. Стоимость {mail.cost} рублей.")
