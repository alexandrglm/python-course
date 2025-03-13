from app_111 import db, app

with app.app_context():
    db.create_all()