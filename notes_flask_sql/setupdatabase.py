from basic import db, Puppy

# Creates all th tables Model -> DB Table
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

