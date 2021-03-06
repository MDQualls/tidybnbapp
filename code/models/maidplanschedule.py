from db import db


class MaidPlanSchedule(db.Model):
    __tablename__ = "maidplanschedule"

    id = db.Column(db.Integer, primary_key=True)
    schedule_name = db.Column(db.String(80), nullable=False)
    schedule_date = db.Column(db.DateTime, nullable=False)
    start_time = db.Column(db.Time, nullable=False, default=0)
    end_time = db.Column(db.Time, nullable=False, default=0)
    post_clean_buffer = db.Column(db.Integer, nullable=False, default=0)

    plans = db.relationship('MaidPlanModel', secondary="maidplanscheduleplan", backref='maidplanschedule',
                           lazy='dynamic')

    def __init__(self, schedule_name, schedule_date, start_time, end_time, post_clean_buffer):
        self.schedule_name = schedule_name
        self.schedule_date = schedule_date
        self.start_time = start_time
        self.end_time = end_time
        self.post_clean_buffer = post_clean_buffer,

    def json(self):
        return {
            "id": self.id,
            "schedule_name": self.schedule_name,
            "schedule_date": self.schedule_date,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "post_clean_buffer": self.post_clean_buffer,
            "plan": [plan.json() for plan in self.plan.first()],
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
