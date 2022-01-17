from flask import render_template, url_for
from . import create_app
from app.models import Competition, Team, CompParticipants


competitions = [
    {
        "name": "Southern California VEXU League",
        "state": "California",
        "teams": ["MTSAC1", "MTSAC2", "USC"],
        "date": "01/15/2022 - 03/12/2022"
    },
    {
        "name": "VEX-U on the Plains",
        "state": "Alabama",
        "teams": ["AUBIE1", "BCUZ", "BCUZ2", "NUKE", "PNTHR", "UCF"],
        "date": "01/22/2022"
    }
]

app = create_app()

@app.route("/")
def home():
    return render_template("home.html", competitions=competitions)
