from json import dumps
import json
from flask import Response, request, abort, jsonify
from bson import json_util

from . import database
from core import app

@app.route('/', methods=['GET'])
def index():
    return 'Metadata service online'

@app.route('/video', methods=['GET'])
def videos():
    videoId = request.args.get('id', '')
    if videoId:
        video = database.get_video(videoId)
        if not video:
            abort(404)
        return video

    videos = database.select_videos()
    
    return jsonify(videos)

@app.route('/video', methods=['POST'])
def post_video():
    video = request.get_json()
    if not video \
        or not video['name'] \
            or not video['videoPath']:
        abort(400)

    return database.add_video(video)
