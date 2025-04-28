from app import app
from flask import render_template

@app.route('/hello')
def hello():
    return "Hello, world"

@app.route('/info')
def info():
    return "This is an informational page."

@app.route('/calc/<int:first_int>/<int:second_int>')
def find_sum(first_int, second_int):
    sum_int = first_int + second_int
    return f"The sum of {first_int} and {second_int} is {sum_int}."

@app.route('/reverse/<rev_str>')
def reverse(rev_str):
    if len(rev_str) > 0:
        rev_word = rev_str[::-1]
        return rev_word
    return "String must be longer than 0 characters"

@app.route('/user/<name>/<int:age>')
def greet_age(name, age):
    if age > 0:
        return f"Hello, {name}. You are {age} years old."
    return "Age cannot be negative!"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")