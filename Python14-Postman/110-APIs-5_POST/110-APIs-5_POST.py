# 03-140: POST

## app.py
from flask import Flask, request, jsonify

# POST endpoint

@app.route('/guide', methods=['POST'])
def add_guide():
    
    title = request.json['title']
    content = request.json['content']

    new_guide = Guide(title, content)

    db.session.add(new_guide)
    db.session.commit()

    guide = Guide.query

    return guide_schema.jsonify(guide)