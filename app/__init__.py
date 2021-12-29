from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/site.db"
db = SQLAlchemy(app)


class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    date = db.Column(db.String(256), nullable=False)
    teams = db.relationship("TeamCompLink", backref="competition", lazy=True)

    def __repr__(self):
        return f"Competition({self.id}, '{self.name}', '{self.date}')"


class TeamCompLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comp_id = db.Column(db.Integer, db.ForeignKey("competition.id"), nullable=False)
    name = db.Column(db.String(6), nullable=False)

    def __repr__(self):
        return f"TeamCompLink({self.comp_id}, '{self.name}')"



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


@app.route("/")
def home():
    return render_template("home.html", competitions=competitions)


if __name__ == "__main__":
    app.run(debug=True)
