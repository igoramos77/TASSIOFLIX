from application import app
from flask import render_template, redirect, jsonify, request, current_app

@app.route("/video/like", methods=['GET'])
def like():
    try:
        videos_curtidos = current_app.config ['video']
        video_id_like = request.values.get('like')
        video = videos_curtidos.getVideoById(video_id_like)
        video.setLike(video.getLikes() +1)
        return jsonify(qtd_likes = video.getLikes())
    except Exception as e:
        return str(e)

@app.route("/video/unlike", methods=['GET'])
def unlike():
    try:
        videos_curtidos = current_app.config ['video']
        video_id_like = request.values.get('unlike')
        video = videos_curtidos.getVideoById(video_id_like)
        video.setLike(video.getLikes() -1)
        return jsonify(qtd_likes = video.getLikes())
    except Exception as e:
        return str(e)


@app.route("/player/comment", methods=['GET'])
def comment(video_id):
    video = current_app.config['video'].show(video_id)
    comment.setComment(request.values.get('comment'))

    return jsonify(comment = video.setComment())
    

@app.route("/player/search", methods=['GET'])
def search():
    search = request.values.get('search')
    
    video = current_app.config['video'].getVideoByTitle(search)
    
    return jsonify(video)


@app.route("/player/<int:video_id>")
def player(video_id):
    video = current_app.config['video'].show(video_id)
    comments = current_app.config['commentary'].getCommentsByVideo(video_id)
    video.setViews(video.getViews() +1)

    if (video is None):
        return redirect('/')

    return render_template ("player.html", video = video, comments = comments, countComments = len(comments))

