from flask import Blueprint, request, jsonify
from zone.zone_store import add_zone, get_zones, update_zone, delete_zone

zone_bp = Blueprint("zone", __name__)

@zone_bp.route("/zone/add", methods=["POST"])
def add():
    add_zone(request.json)
    return {"msg": "Zone saved"}

@zone_bp.route("/zone/update", methods=["PUT"])
def update():
    update_zone(request.json)
    return {"msg": "Zone updated"}

@zone_bp.route("/zone/delete/<int:zone_id>", methods=["DELETE"])
def delete(zone_id):
    delete_zone(zone_id)
    return {"msg": "Zone deleted"}

@zone_bp.route("/zone/all", methods=["GET"])
def all_zones():
    return jsonify(get_zones())
