class Field:
    def __init__(self, value=None):
        self.value = value


class CityList:
    def __init__(self, cities):
        self.cities = cities

    def is_valid(self, city):
        return city in self.cities

    def print_choices(self):
        print("Оберіть місто зі списку:")
        for idx, city in enumerate(self.cities, 1):
            print(f"{idx}. {city}")

    def get_by_index(self, index):
        if 1 <= index <= len(self.cities):
            return self.cities[index - 1]
        raise ValueError("Невірний номер міста.")


class Address(Field):
    def __init__(self, city, street, city_list: CityList):
        self.city = city
        self.street = street
        self.city_list = city_list
        super().__init__(f"{city}, {street}")
        self.validate()

    def validate(self):
        if not self.city_list.is_valid(self.city):
            raise ValueError(f"Місто '{self.city}' не дозволене.")

        if not isinstance(self.street, str):
            raise ValueError("Назва вулиці має бути рядком.")

        if len(self.street.strip()) < 5:
            raise ValueError("Назва вулиці занадто коротка.")

        if not any(char.isdigit() for char in self.street):
            raise ValueError("Адреса має містити номер будинку.")

    def __str__(self):
        return f"{self.city}, {self.street}"


def main():
    allowed = CityList(["Київ", "Львів", "Одеса", "Харків", "Дніпро"])

    allowed.print_choices()

    try:
        choice = int(input("Введіть номер міста зі списку: ").strip())
        city = allowed.get_by_index(choice)
    except Exception as e:
        print("Помилка:", e)
        return

    street = input("Введіть вулицю та номер (наприклад, 'вул. Шевченка 10'): ").strip()

    try:
        address = Address(city, street, allowed)
        print("Збережено адресу:", address)
    except ValueError as e:
        print("Помилка:", e)


if __name__ == "__main__":
    main()
