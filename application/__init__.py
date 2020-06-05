from flask import Flask
import os

from application.model.dao.video_DAO import VideoDAO
from application.model.dao.comentary_DAO import CommentaryDAO

template_folder = os.path.abspath("application/view/templates")
static_folder = os.path.abspath("application/view/static")

app = Flask(__name__, template_folder = template_folder, static_folder = static_folder)

video = VideoDAO()
commentary = CommentaryDAO()

app.config['video'] = video
app.config['commentary'] = commentary


from application.controller import home_controller
from application.controller import player_controller
from application.controller import commentary_controller

#from application.controller import category_controller
#from application.controller import video_controller