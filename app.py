from flask import Flask, jsonify, render_template, redirect
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from detection.video_processor import init_videos, process_frames
from analytics.analytics_store import get_zone_counts

from auth import auth_bp
from user.user_routes import user_bp
from camera.camera_routes import camera_bp
from analytics.analytics_routes import analytics_bp
from zone.zone_routes import zone_bp

from threading import Thread
import time

from flask import Response
from detection.video_stream import generate_frames
from auth.jwt_utils import token_required
from alerts.alert_routes import alert_bp


import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp"

import cv2
cv2.setNumThreads(1)
cv2.ocl.setUseOpenCL(False)

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = "super-secret-key"
JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(camera_bp)
app.register_blueprint(analytics_bp)
app.register_blueprint(zone_bp)
app.register_blueprint(alert_bp)

VIDEO_SOURCES = {
    1: "videos/cam1.mp4",
    2: "videos/cam2.mp4",
    3: "videos/cam3.mp4",
    4: "videos/cam4.mp4",
}


init_videos(VIDEO_SOURCES)


@app.route("/")
def home():
    return redirect("/login")

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/video_feed")
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/analytics")
def analytics_page():
    return render_template("analytics/analytics.html")

@app.route("/api/analytics")
def analytics_data():
    return {
        "zones": {
            "Zone 1": get_zone_counts("zone1"),
            "Zone 2": get_zone_counts("zone2"),
            "Zone 3": get_zone_counts("zone3"),
            "Zone 4": get_zone_counts("zone4"),
        }
    }

def start_video_processing():
    t = Thread(target=process_frames, daemon=True)
    t.start()




if __name__ == "__main__":
    start_video_processing()
    app.run(debug=False, threaded=True)
