from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return f'<User {self.email}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    firstname = db.Column(db.String(250))
    lastname = db.Column(db.String(250))
    email = db.Column(db.String(250))
    password = db.Column(db.String(30), nullable=False)
    subscription_date_mmddaaaa = db.Column (db.String(8))
    favorites = relationship('Favorite')

    def __repr__(self):
        return f'{self.username}'

    def serialize(self):
        return {
            "username" : self.username,
            "firstname" : self.firstname,
            "lastname" : self.lastname,
            "email" : self.email
        }

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), unique = True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), unique = True)
    favorite_planets = relationship('Planets', uselist = False, foreign_keys=[planet_id])
    favorite_character = relationship('Character', uselist = False, foreign_keys=[character_id])

    def serialize(self):
        return {
            "name" : self.name
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(250))
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorite.id'))
    # user = relationship('Favorite')

    def __repr__(self):
        return f'{self.planet_name}'

    def serialize(self):
        return {
            "planet_name" : self.planet_name,
        }
    
class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(250))
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorite.id'))
    # user = relationship('Favorite')

    def __repr__(self):
        return f'{self.character_name}'

    def serialize(self):
        return {
            "character_name" : self.character_name
        }