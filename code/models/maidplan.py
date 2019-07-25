from db import db
from datetime import datetime


class MaidPlanModel(db.Model):
    __tablename__ = "maidplans"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    summary = db.Column(db.String(240))
    description = db.column(db.Text())
    plan_creation_date = db.Column(db.DateTime, default=datetime.now())
    plan_update_date = db.Column(db.DateTime, default=None)
    deleted = db.Column(db.Boolean)

    def __init__(self, title, summary, description, deleted):
        self.title = title
        self.summary = summary
        self.description = description
        self.deleted = deleted

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "summary": self.summary,
            "description": self.description,
            "deleted": self.deleted,
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
