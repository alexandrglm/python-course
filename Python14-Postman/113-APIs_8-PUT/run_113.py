from app_113 import db, app

with app.app_context():
    db.create_all()