from app_109 import app, db


with app.app_context():
    db.create_all()

