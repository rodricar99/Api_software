from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/factorial', methods=["GET"])
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

app.run()