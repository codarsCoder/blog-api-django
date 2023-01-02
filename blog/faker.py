from .models import Category, Blog
from faker import Faker
from datetime import datetime

def run():
    fake = Faker(['en-US'])
    categories = (
        "Politics",
        "Sports",
        "Millitary",
        "Travel",
        "Showbiz"
    )


def run():
    fake = Faker()
    categories = ("Life", "Science", "Politics", "Sports")

    for categoryy in categories:
        new_category = Category.objects.create(category_name=categoryy)
        for _ in range(20):
            Blog.objects.create(category=new_category,
                                title=fake.name(), content=fake.text(), user_id = fake.pybool())
    print("Finished")
