# pip install SQLAlchemy
# https://docs.sqlalchemy.org/en/20/orm/quickstart.htmls
# https://metanit.com/python/database/3.1.php

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, relationship


# "sqlite:///относительный_путь/database"
# "sqlite:////абсолютный_путь/database"
# parameter echo=True - log all activities in db
engine = create_engine('sqlite:///test_db.sql')

class Base(DeclarativeBase): pass

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)

# create tables
Base.metadata.create_all(bind=engine)

# parameter autoflush=True - autocommit after changes
with Session(bind=engine) as db:
    # Create
    tom = Person(name='Tom', age=45)
    db.add(tom)
    # db.refresh(tom) # to get new object from db
    db.commit()
    print(f'tom.id: {tom.id}')

    # Read
    people = db.query(Person).all()
    for person in people:
        print(f'{person.id}. {person.name} {person.age} years old')

    person_with_1_id = db.get(Person, 1)
    print(f'person with id 1: {person_with_1_id}')

    people_whose_more_30_years_old = db.query(Person).filter(Person.age > 30).all()
    for person in people_whose_more_30_years_old:
        print(f'{person.id}. {person.name} {person.age} years old (filter: >30 years)')

    person_with_name_tom = db.query(Person).filter(Person.name == 'Tom').first()
    print(f'person with name Tom: {person_with_name_tom}')

    # Update
    tom = db.query(Person).filter(Person.id == 10).first()
    if tom != None:
        tom.age = 21
        db.commit()
        db.refresh(tom)
        print(f'check update, tom age 21: {tom}')

    # Delete
    tom = db.query(Person).filter(Person.age == 21).first()
    if tom != None:
        db.delete(tom)
        db.commit()

# one-to-many
# 1 user can work in 1 company
# in 1 company can work many users

class User(Base):
    __tablename__ = 'users'
    __mapper_args__ = {
        'confirm_deleted_rows': False # no to show warning
    }
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship('Company', back_populates='users')
    # 'Company' - other relationship model
    # back_populates - other attribute in this model

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    users = relationship('User', back_populates='company', cascade='all, delete-orphan')
    # cascade - delete all other users

Base.metadata.create_all(bind=engine)

with Session(bind=engine) as db:
    # Create
    microsoft = Company(name='Microsoft')
    google = Company(name='Google')

    tom = User(name='Tom')
    bob = User(name='Bob')

    microsoft.users = [tom]
    google.users = [bob]

    # add users and companies in db
    db.add_all([microsoft, google])
    db.commit()

    # add user in company
    alice = User(name='Alice')
    google.users.extend([alice]) # (last time no work in me)

    # set company for user
    sam = User(name='Sam')
    sam.company = microsoft
    db.add(sam)
    db.commit()

    # Read
    for company in db.query(Company).all():
        print(f'company {company.id}. {company.name}')
        for user in company.users:
            print(f'user {user.id}. {user.name}')
        print('--------------------\n')

    # Update
    tom = db.query(User).filter(User.name=='Tom').first()
    google = db.query(Company).filter(Company.name=='Google').first()

    if tom != None and google != None:
        tom.company = google
        db.commit()
        print('update: now Tom work in Google')

    # Delete
    tom = db.query(User).filter(User.name == 'Tom').first()
    google = db.query(Company).filter(Company.name == 'Google').first()

    if tom != None and google != None:
        google.users.remove(tom)
        db.commit()
        print('delete: now Tom no work in Google, delete in google.users')

    db.delete(tom)
    db.commit()
    print('delete: now Tom died :)')






