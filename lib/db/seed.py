from faker import Faker
from sqlalchemy.orm import Session
from models import User  # Replace with your actual model

fake = Faker()

def create_fake_data(db: Session):
    for _ in range(10):  # Change the number based on how much data you want
        fake_name = fake.name()
        fake_email = fake.email()
        
        # Create an instance of your model with the fake data
        db_item = User(name=fake_name, email=fake_email)
        
        # Add it to the session and commit
        db.add(db_item)
        db.commit()

# Usage
# Assuming you have your SQLAlchemy session ready (db_session), you can call the function
# create_fake_data(db_session)
