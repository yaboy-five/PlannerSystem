from flask import Flask, render_template, request, redirect, url_for

from database import get_connection
from models import add_user

app = Flask(__name__)

# DB connection
# Connecting with databse.py

# routing

# homepage 
@app.route("/")
def index():
    return render_template("index.html")

# adding a user
@app.route("/add-user", methods=["GET", "POST"])
def add_user_page():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]

        add_user(name, email)

        return redirect(url_for("users"))

    return render_template("add_user.html")

# view activities
@app.route("/activities")
def activities():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            A.ActivityName, 
            A.ActivityDate, 
            A.ActivityType,
            A.Status,
            U.FullName
        FROM Activities A
        INNER JOIN Users U ON A.UserID = U.UserID
        ORDER BY A.ActivityDate
    """)

    activities = cursor.fetchall()

    connection.close()

    return render_template("view_activities.html", activities=activities)

if __name__ == "__main__":
    app.run(debug=True)