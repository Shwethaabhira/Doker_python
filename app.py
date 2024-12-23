from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hi Shwetha</h1>
    <h2>This is your application</h2>
    <h3>Thank you!!</h3>
    """

if __name__ == "__main__":
    app.run(debug=True)
