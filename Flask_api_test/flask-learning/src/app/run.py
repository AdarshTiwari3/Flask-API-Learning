from app import create_app, db
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .flaskenv or .env file into the environment

app = create_app()  # Create the Flask app instance

# Create all the tables in the database
with app.app_context():
    # db.drop_all()  # Drop all tables
    db.create_all() 

if __name__ == "__main__":
    app.run()
