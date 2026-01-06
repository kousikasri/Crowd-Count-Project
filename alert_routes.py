from flask import Blueprint, request, jsonify
from alerts.alert_store import update_threshold, acknowledge, reset_ack, get_config
from alerts.alert_store import get_active_alerts, acknowledge

alert_bp = Blueprint("alert", __name__)

@alert_bp.route("/alerts/config", methods=["GET"])
def config():
    return jsonify(get_config())

@alert_bp.route("/alerts/update", methods=["POST"])
def update():
    data = request.json
    update_threshold(data["zone"], data["threshold"], data["enabled"])
    reset_ack(data["zone"])
    return {"msg": "Threshold updated"}

@alert_bp.route("/alerts/ack/<zone>", methods=["POST"])
def ack(zone):
    acknowledge(zone)
    return {"msg": "Alert acknowledged"}

@alert_bp.route("/alerts/active", methods=["GET"])
def active():
    return jsonify(get_active_alerts())

@alert_bp.route("/alerts/ack/<zone>", methods=["POST"])
def acknowledge_alert(zone):
    acknowledge(zone)
    return {"msg": "Acknowledged"}
