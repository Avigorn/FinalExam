from models.Home_Animal import Home_Animal


class Dog(Home_Animal):
    def __init__(self, name, birthday, weight, type_animal):
        super().__init__(name, birthday, weight, type_animal)
