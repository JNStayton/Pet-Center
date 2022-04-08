"""Seed file to make data for pets table in petcenter db"""

from models import Pet, db 
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets

bowie = Pet(name="David Bowie", species="Cat", photo_url="https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1143&q=80", age=6, notes="She's so swishy in her satin and tat; In her frock coat and bipperty-bopperty hat - Oh God, I could do better than that!! Oh, yeah!", available=True)

booger = Pet(name="Booger", species="Dog", photo_url="https://images.unsplash.com/photo-1587300003388-59208cc962cb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80", age=3, notes="Oh, I'm just a precious dog, a wonderful pupper boii.", available=True)

el = Pet(name="El-Ahrairah", species="Rabbit", photo_url="https://images.unsplash.com/photo-1609151354448-c4a53450c6e9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=435&q=80", age=3, notes="All the world will be your enemy, Prince with a Thousand Enemies, and whenever they catch you, they will kill you. But first they must catch you, digger, listener, runner, prince with the swift warning. Be cunning and full of tricks and your people shall never be destroyed.", available=False)

# Add to database

db.session.add_all([bowie, booger, el])
db.session.commit()