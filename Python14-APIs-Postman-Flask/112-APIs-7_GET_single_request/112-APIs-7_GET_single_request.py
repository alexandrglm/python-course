from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)

# from app_109
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


# id, title, content
class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

class GuideSchema(ma.Schema):
    class Meta:
        fields = ('title', 'content')


guide_schema = GuideSchema()
guides_schema = GuideSchema(many=True)


# from app_110

## POST endpoint
# Endpoint POST para agregar una nueva guía
@app.route('/guide', methods=["POST"])
def add_guide():
    title = request.json['title']
    content = request.json['content']

    new_guide = Guide(title, content)

    db.session.add(new_guide)
    db.session.commit()

    guide = Guide.query.get(new_guide.id)

    return guide_schema.jsonify(guide)


# from app_111
## GET endpoint
@app.route("/guides", methods=["GET"])
def get_guides():
   
    all_guides = Guide.query.all()
    result = guides_schema.dump(all_guides)
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)