from app import app
from flask import render_template, request, redirect, url_for
import re
from datetime import datetime

@app.route("/")
def home():
    current_time = datetime.now()
    return render_template("index.html", current_time=current_time)

@app.route("/contact", methods=["GET"])
def contact():
    contact_info = {
        'name': 'Customer Care Department',
        'address': {
            'street': '123 Main St',
            'city': 'Wonderland',
            'zip': '12345'
        }
    }
    success = request.args.get("success")
    return render_template("contact.html", success=success, contact_info=contact_info)

@app.route("/about")
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template("about.html", team_members=team_members)

@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        name_pattern = r"^[A-Za-zА-Яа-яЁё\s]+$"
        email_pattern = r"[^@]+@[^@]+\.[^@]+"

        if not name.strip() or not re.match(name_pattern, name):
            error = "Please enter a valid name (only letters and spaces)."
            return render_template("contact.html", error=error, name=name, email=email, message=message)
        
        if not re.match(email_pattern, email):
            error = "Please enter a valid email address."
            return render_template("contact.html", error=error, name=name, email=email, message=message)
        
        if not message.strip():  
            error = "Please enter a message."
            return render_template("contact.html", error=error, name=name, email=email, message=message)
        return redirect(url_for("contact", success="1"))