from flask import Blueprint, Response
from detection.video_stream import generate_frames

camera_bp = Blueprint("camera", __name__)

@camera_bp.route("/video/<int:cam_id>")
def video_feed(cam_id):
    return Response(
        generate_frames(cam_id),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )
