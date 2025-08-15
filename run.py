from app import create_app
from dotenv import load_dotenv

from aws_setup import create_aws_instances

load_dotenv()
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)