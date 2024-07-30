from app import create_app
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .flaskenv file into the environment and this file should be in parent only
# print("FLASK_ENV:", os.getenv('FLASK_ENV'))
app = create_app()

if __name__ == "__main__":
    app.run()
