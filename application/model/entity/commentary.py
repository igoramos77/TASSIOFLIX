from flask import current_app

class Commentary:
    def __init__ (self, id, videoId, content):
        self._id = id
        self._content = content
        self._video_id = videoId

    def getContent(self):
        return self._content

    def getId(self):
        return self._id

    def get_video_commentary_id (self):
        return self._video_id

    