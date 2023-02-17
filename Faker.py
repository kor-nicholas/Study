# pip install Faker

from faker import Faker
from faker.providers import internet

fake = Faker()
fake.add_provider(internet)

count = int(input('Введите количество объектов для генерации: '))

for i in range(count):
	print(fake.domain_name())
	print(fake.name())
	print(fake.address())
	print(fake.text())
	print(fake.ipv4_private())