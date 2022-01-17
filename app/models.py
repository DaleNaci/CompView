from . import db


class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    date = db.Column(db.String(256), nullable=False)
    teams = db.relationship("CompParticipants", backref="competition", lazy=True)

    def __repr__(self):
        return f"Competition({self.id}, '{self.name}', '{self.date}')"


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f"Team({self.id}, '{self.name}')"


class CompParticipants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comp_id = db.Column(db.Integer, db.ForeignKey("competition.id"), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("team.id"), nullable=False)

    def __repr__(self):
        return f"CompParticipants({self.comp_id}, '{self.team_id}')"
