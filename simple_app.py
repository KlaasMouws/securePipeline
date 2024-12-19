from flask import Flask

app = Flask(__name__)
password = "test123"
@app.route("/")
def home():
    return "Hello, world!"

if __name__ == "__main__":
    app.run()
