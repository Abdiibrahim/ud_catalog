#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

engine = create_engine('postgresql://catalog:password@localhost/catalog',
                       connect_args={'check_same_thread': False})

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(id=1 , name="Sydney Adams", email="sydneyadams@example.com",
    picture='https://conferencecloud-assets.s3.amazonaws.com/default_avatar.png')

session.add(User1)
session.commit()

# Items for Basketball
category1 = Category(user=user1, name="Basketball")

session.add(category1)
session.commit()

item1 = Item(category=category1, user=user1, name="Basketball Top", description="Lightweight tank. \
    Available in a variety of colours.", price="$17.99", type="Shirts")

session.add(item1)
session.commit()

print("Added menu items!")
