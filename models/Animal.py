class Animal:

    counter = 0

    def __init__(self, name, birthday, weight, type_animal):
        self.name = name
        self.birthday = birthday
        self.weight = weight
        self.type_animal = type_animal
        self.command_animal = []

        Animal.counter += 1
        self.id = Animal.counter

    def get_name(self):
        return self.name

    def get_birthday(self):
        return self.birthday

    def get_weight(self):
        return self.weight

    def get_type(self):
        return self.type_animal

    def set_name(self, name):
        self.name = name

    def set_weight(self, weight):
        self.weight = weight

    def get_id(self):
        return self.id

    def __str__(self):
        return f"Кличка животного: {self.name}\nВозраст животного: {self.birthday}\nВес животного: {self.weight:.2f} кг\nТип животного: {self.type_animal}"

    def get_commands(self):
        return self.command_animal

    def add_command(self, command):
        self.command_animal.append(command)
