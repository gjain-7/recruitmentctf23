import dotenv
from reqhead.reqhead import app
dotenv.load_dotenv(".env")

if __name__ == "__main__":
    print("Starting app...")
    app.run(port=5000)
