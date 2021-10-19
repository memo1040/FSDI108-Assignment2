from flask import Flask


app = Flask(__name__)


me = {
    "name": "Guillermo",
    "last": "Monge",
    "age": 32,
    "hobbies": [],
    "email": "gmt1040@gmail.com",
    "address": {
        "street": "Delta",
        "city": "San Diego"
    }
}


@app.route("/")
@app.route("/home")
def home():
    return "Hello from a Flask Server"

@app.route("/test")
def simple_test():
    return "Hello there!"


@app.route("/about")
def about():
    return me["name"] + " " + me["last"]

@app.route("/about/email")
def email():
    return me["email"]

@app.route("/about/address")
def address():
    return me["address"]["street"] + ", " + me["address"]["city"]





# start the server
# debug true will restart the server automatically
app.run(debug=True)




# /about