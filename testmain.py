class Address(Field):
    # Static list of allowed cities
    allowed_cities = ["Київ", "Львів", "Одеса", "Харків", "Дніпро"]

    def __init__(self, city, street):
        self.city = city
        self.street = self.normalize_street(street)
        # Store full address as the value
        super().__init__(f"{self.city}, {self.street}")
        self.validate()

    # Format the street: trim whitespace and add "вул." if missing
    def normalize_street(self, street):
        street = street.strip()
        if not street.lower().startswith("вул."):
            street = "вул. " + street
        return street

    # Validate city and street formatting
    def validate(self):
        if self.city not in self.allowed_cities:
            raise ValueError(f"City '{self.city}' is not allowed. Choose from: {', '.join(self.allowed_cities)}")

        if not isinstance(self.street, str):
            raise ValueError("Street name must be a string.")

        if len(self.street.strip()) < 5:
            raise ValueError("Street name is too short.")

        if not any(char.isdigit() for char in self.street):
            raise ValueError("Street must contain a house number.")

    # Return formatted address string
    def __str__(self):
        return f"{self.city}, {self.street}"

    # Show the list of allowed cities to the user
    @staticmethod
    def print_allowed_cities():
        print("Choose a city from the list:")
        for idx, city in enumerate(Address.allowed_cities, 1):
            print(f"{idx}. {city}")
