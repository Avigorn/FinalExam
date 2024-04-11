from models.Animal import Animal


class Home_Animal(Animal):
    def __init__(self, name, birthday, weight, type_animal):
        super().__init__(name, birthday, weight, type_animal)
