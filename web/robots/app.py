import dotenv

dotenv.load_dotenv(".env")

from robots.robots import app

if __name__ == "__main__":
    app.run(port=5000)
