from application import app
from flask import current_app, render_template, request, jsonify

@app.route("/")
def home():
    listVideo = current_app.config['video']
    videoList = listVideo.showAllVideos()
    moreLikes = listVideo.getMoreLikes()
    moreViewsSlider = listVideo.getMoreViewsSlider()
    moreViews = listVideo.getMoreViews()
    return render_template("index.html", video = listVideo, videoList = videoList, moreLikes = moreLikes, moreViewsSlider = moreViewsSlider, moreViews = moreViews)