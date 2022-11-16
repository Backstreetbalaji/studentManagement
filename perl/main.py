from flask import Flask, render_template, request

from database import Database

app = Flask(__name__)
obj = Database()


@app.route("/")
def homepage():
    return render_template("hello.html")


@app.route('/add')
def add():
    return render_template("add.html")


@app.route("/data", methods=['POST', 'GET'])
def register():
    n = request.form.get('name')
    a = request.form.get('age')
    nu = request.form.get('number')
    obj.insert_into_database('n, a, nu')
    return render_template("data.html", name=n, age=a, number=nu)


if __name__ == '__main__':
    app.run()
