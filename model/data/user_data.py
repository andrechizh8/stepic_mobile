from dataclasses import dataclass
from faker import Faker
import os
from dotenv import load_dotenv

load_dotenv()
faker = Faker()


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    password: str
    bio_info: str
    random_email: str
    random_password: str


current_user = User(first_name=faker.first_name(), last_name=faker.last_name(),
                    bio_info=faker.job(), email=os.getenv("EMAIL"), password=os.getenv("PASSWORD"),
                    random_email=faker.email(),
                    random_password=faker.password())
