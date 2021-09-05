from faker import Faker

fake = Faker('Ru-ru')


class UserData:
    def __init__(self, name=None, email=None, city=None):
        self.name = name
        self.email = email
        self.city = city

    @staticmethod
    def random():
        name = fake.name()
        email = fake.email()
        city = fake.city()
        return UserData(name, email, city)