from app_110 import db, app

with app.app_context():
    db.create_all()