from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask_db_l8ys_user:3S02PJf9cSaburqEyYIFj8dTicQ4F85w@dpg-cvnsuk15pdvs73fs853g-a.oregon-postgres.render.com/flask_db_l8ys'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Create the tables if they do not exist
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Hello, CI/CD with Docker & GitHub Actions!"

@app.route("/add-user")
def add_user():
    new_user = User(name="Talha")
    db.session.add(new_user)
    db.session.commit()
    return f"Added user {new_user.name} with ID {new_user.id}"

@app.route("/users")
def get_users():
    users = User.query.all()
    return "<br>".join([f"{user.id}: {user.name}" for user in users])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
