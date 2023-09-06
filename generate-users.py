from faker import Faker

fake = Faker()

for _ in range(100):
    print(fake.email(), "--", fake.name())
