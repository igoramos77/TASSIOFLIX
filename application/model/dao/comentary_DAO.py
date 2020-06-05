from flask import current_app

from application.model.entity.commentary import Commentary
 
class CommentaryDAO:
    def __init__ (self):
        self._generate_id = 2
        self._comments = [
            Commentary(1, 1, 'Muito ruim!!!')
        ]

    def add_commentary (self, video_id, content):
        generatedId = self._generate_id
        self._comments.append(Commentary(generatedId, video_id, content))
        self._generate_id = self._generate_id + 1
        
        return generatedId

    def getCommentsByVideo(self, video_id):
        comments = []
        for i, comment in enumerate (self._comments):
            if comment.get_video_commentary_id() == video_id:
                comments.append(comment)
        return comments


    def removeComment(self, video_id, comment_id):
        for i, comment in enumerate(self._comments):
            if comment.getId() == comment_id:
                self._comments.pop(i)
                return comment
        return None