from flask import Blueprint, jsonify, Response
from analytics.analytics_store import get_zone_counts, get_history
import csv
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/analytics/zone-wise", methods=["GET"])
def zone_wise():
    return jsonify(zone_counts)

@analytics_bp.route("/analytics/hourly", methods=["GET"])
def hourly():
    return jsonify(zone_history)

@analytics_bp.route("/export/csv")
def export_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Timestamp", "Camera ID", "Zone ID", "People Count"])

    for row in get_history():
        writer.writerow([
            row["timestamp"],
            row["camera_id"],
            row["zone_id"],
            row["count"]
        ])

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=crowd_data.csv"}
    )

@analytics_bp.route("/export/pdf")
def export_pdf():
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    text = pdf.beginText(40, 800)

    text.textLine("CrowdCount – Analytics Report")
    text.textLine("")

    for row in get_history():
        line = f"{row['timestamp']} | Cam {row['camera_id']} | {row['zone_id']} | {row['count']}"
        text.textLine(line)

    pdf.drawText(text)
    pdf.save()
    buffer.seek(0)

    return Response(
        buffer,
        mimetype="application/pdf",
        headers={"Content-Disposition": "attachment; filename=crowd_data.pdf"}
    )