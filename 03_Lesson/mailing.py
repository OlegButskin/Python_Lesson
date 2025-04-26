from address import Address

class Mailing:
    def __init__(self, to_address: Address, from_address: Address, cost: int, track: str):
        self.to_address = to_address    # Адрес получателя
        self.from_address = from_address # Адрес отправителя
        self.cost = cost                # Стоимость (число)
        self.track = track               # Трек-номер (строка)