from app import create_app, db
from dotenv import load_dotenv
from sqlalchemy import inspect
import os

load_dotenv()  # Load environment variables from .flaskenv or .env file into the environment

app = create_app()  # Create the Flask app instance


if __name__ == "__main__":
    app.run()
