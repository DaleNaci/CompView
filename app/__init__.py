from flask import Flask, render_template


app = Flask(__name__)

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
