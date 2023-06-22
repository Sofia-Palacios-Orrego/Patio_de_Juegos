from flask import Flask, render_template

patio = Flask(__name__)

@patio.route("/play", methods=['GET'])
def one():
    return render_template("index.html", x=3)

@patio.route("/play/<int:x>", methods=['GET'])
def two(x):
    return render_template("index.html", x=x)

@patio.route("/play/<int:x>/<color>", methods=['GET'])
def three(x, color):
    return render_template("index.html", x=x, color=color)


if __name__ == "__main__":
    patio.run( debug = True, port = 5001 )
