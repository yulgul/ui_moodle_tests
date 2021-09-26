import os
import random

from faker import Faker

from common.constans import PersonalDataConstants

fake = Faker('Ru-ru')

current_dir = os.path.dirname(__file__)
path = os.path.join(current_dir, "images")
filename = random.choice(os.listdir(path))


class UserData:
    def __init__(self, first_name=None, last_name=None, email=None, email_display_mode=None, moodlenet=None, city=None,
                 time_zone=None, middle_name=None, interest=None, id_number=None, institution=None, department=None, phone=None, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.email_display_mode = email_display_mode
        self.moodlenet = moodlenet
        self.city = city
        self.time_zone = time_zone
        self.middle_name = middle_name
        self.interest = interest
        self.id_number= id_number
        self.institution= institution
        self.department= department
        self.phone = phone
        self.address = address

    @staticmethod
    def random():
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        email_display_mode = random.choice(
            list(PersonalDataConstants.EMAIL_DISPLAY_MODES.values())
        )
        moodlenet = fake.url()
        city = fake.city()
        time_zone = random.choice(list(PersonalDataConstants.TIMEZONE_VALUES))
        middle_name = fake.middle_name()
        interest = fake.word()
        id_number = fake.businesses_inn()
        institution = fake.company()
        department = fake.bs()
        phone = fake.phone_number()
        address = fake.address()
        return UserData(first_name, last_name, email, email_display_mode, moodlenet, city, time_zone, middle_name, interest, id_number, institution, department, phone, address)


class UserImage:
    def __init__(self, image, description=None):
        self.image = image
        self.description = description
    @staticmethod
    def random():
        image = os.path.join(path, filename)
        description = fake.text()
        return UserImage(image, description)
