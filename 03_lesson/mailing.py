# Класс Mailing описывает почтовое отправление:
# адрес получателя, отправителя, стоимость и трек-номер


class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address      # Адрес получателя
        self.from_address = from_address  # Адрес отправителя
        self.cost = cost                  # Стоимость (в рублях)
        self.track = track                # Трек-номер (например: AB123...)
