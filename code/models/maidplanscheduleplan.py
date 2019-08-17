from db import db


class MaidPlanSchedulePlan(db.Model):
    __tablename__ = "maidplanscheduleplan"

    plan_id = db.Column(db.Integer, db.ForeignKey("maidplans.id"), primary_key=True)
    schedule_id = db.Column(db.Integer, db.ForeignKey("maidplanschedule.id"), primary_key=True)

    plan = db.relationship('MaidPlanModel', backref='maidplanscheduleplan')
    schedule = db.relationship('MaidPlanSchedule', backref='maidplanscheduleplan')
