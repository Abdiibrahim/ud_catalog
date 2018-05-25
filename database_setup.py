from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# Create User Table
class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	picture = Column(String(250))


# Create Category Table
class Category(Base):
	__tablename__ = 'category'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		return {
			'name'    : self.name,
			'id'      : self.id
		}


# Create Item Table
class Item(Base):
	__tablename__ = 'item'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	description = Column(String(250))
	price = Column(String(8))
	type = Column(String(250))
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		return {
			'name'        : self.name,
			'description' : self.description,
			'id'          : self.id,
			'user_id'     : self.user_id,
			'category-id' : self.categpry_id,
			'price'       : self.price,
			'type'        : self.type
		}


engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.create_all(engine)
