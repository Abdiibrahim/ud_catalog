from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(id=1 , name="Sydney Adams", email="sydneyadams@email.com", picture='https://conferencecloud-assets.s3.amazonaws.com/default_avatar.png')
session.add(User1)
session.commit()

# Items for Basketball
category1 = Category(user_id=1, name="Basketball")
session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Basketball Top", description="Lightweight tank. Available in a variety of colours.", price="$17.99", type="Shirts", category=category1)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Basketball Short Sleeve Shirt", description="Short-sleeve shirt. Available in a variety of colours.", price="$23.99", type="Shirts", category=category1)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Basketball Shorts", description="Made form lightweight, breathable fabric. Sizes: XS, S, M, L, XL", price="$24.99", type="Pants", category=category1)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="High Top Sneakers", description="Designed for optimal support. Sizes: 5-12", price="$79.99", type="Shoes", category=category1)
session.add(item4)
session.commit()

item5 = Item(user_id=1, name="High Performance Shoes", description="Designed for high performance. Sizes: 5-12", price="$109.99", type="Shoes", category=category1)
session.add(item5)
session.commit()


# Items for Soccer
category2 = Category(user_id=1, name="Soccer")
session.add(category2)
session.commit()

item1 = Item(user_id=1, name="Fitted Shirt", description="Fitted shirt. Adjusted for comfort.", price="$24.99", type="Shirts", category=category2)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Loose Shirt", description="Loose shirt. Highly breathable.", price="$24.99", type="Shirts", category=category2)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Soccer Shorts", description="High performance. Available in a variety of colours", price="$19.99", type="Pants", category=category2)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Outdoor Cleats", description="Designed for use on turf/grass.", price="$99.99", type="Shoes", category=category2)
session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Indoor Cleats", description="Designed for use on indoor courts.", price="$79.99", type="Shoes", category=category2)
session.add(item5)
session.commit()


# Items for Hockey
category3 = Category(user_id=1, name="Hockey")
session.add(category3)
session.commit()

item1 = Item(user_id=1, name="Generic Jersey", description="Available in a variety of colours", price="$29.99", type="Shirts", category=category3)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="High Performance Jersey", description="Made from lightweight material for optimal performance.", price="$39.99", type="Shirts", category=category3)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Hockey Pants", description="Padded pants to provide protection.", price="$39.99", type="Pants", category=category3)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Hockey Skates", description="Deigned for comfort on the ice.", price="$109.99", type="Shoes", category=category3)
session.add(item4)
session.commit()

item5 = Item(user_id=1, name="High Performance Skates", description="Designed for high performance.", price="$129.99", type="Shoes", category=category3)
session.add(item5)
session.commit()


print "Added menu items!"
