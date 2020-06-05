from application import app
from flask import jsonify, request, current_app
import logging

logging.basicConfig(level=logging.DEBUG)

@app.route("/video/<int:video_id>/commentary", methods=['POST'])
def store(video_id):    
    content = request.values.get('content')

    commentary_id = current_app.config['commentary'].add_commentary(
      video_id,
      content
    )

    return jsonify({
      "id": commentary_id,
      "content": content
    })

@app.route("/video/<int:video_id>/commentary/<int:comment_id>", methods=['DELETE'])
def destroy(video_id, comment_id):    
    current_app.config['commentary'].removeComment(video_id, comment_id)

    return jsonify({})