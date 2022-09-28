# -*- coding: utf-8 -*-
"""Cópia de ExemploSQLAlquemy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LWT7waSQ_6fjR04NdVLFERAz_Wx8_sbo
"""

# !pip install sqlalchemy

from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///db.sqlite', echo=True)


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    age = Column(Integer)


def __repr__(self):
    return "<User(name={}, fullname={}, age={})>".format(self.name, self.fullname, self.age)


Base.metadata.create_all(engine)

user = User(name="Josue", fullname="Josue Filipe", age=42)

Session = sessionmaker(bind=engine)
session = Session()
# Comando para inserir um objeto no banco
session.add(user)
session.commit()

andre = User(name="Andre", fullname="Andre Anderson Almeida", age=22)
session.add(andre)
session.commit()

# Comando para inserir varios objetos no banco
session.add_all([
    User(name="Fulano", fullname="Fulano de Tal", age=22),
    User(name="Ciclano", fullname="Ciclano de Tal", age=22)
])
session.commit()

# Consultando registros no banco

fulano = session.query(User).filter_by(fullname="Fulano de Tal").first()
ciclano = session.query(User).filter_by(fullname="Ciclano de Tal").first()

for usuario in session.query(User).order_by(User.fullname):
    print('Nome:{} \t idade:{}'.format(usuario.fullname, usuario.age))