from db import db


class BnbModel(db.Model):
    __table__ = "bnblistings"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    summary = db.Column(db.String(240))
    content = db.Column(db.Text())
    thumbnail = db.Column(db.String(80))
    active = db.Column(db.Boolean, default=False)
    archived = db.Column(db.Boolean, default=False)
    deleted = db.Column(db.Boolean, default=False)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)

    def __init__(self, title: str, summary: str, content: str, thumbnail: str, active: bool,
                 archived: bool, deleted: bool, bedrooms: int, bathrooms: int
                 ):
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.deleted = deleted
        self.archived = archived
        self.active = active
        self.thumbnail = thumbnail
        self.content = content
        self.summary = summary
        self.title = title

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "summary": self.summary,
            "content": self.content,
            "thumbnail": self.thumbnail,
            "active": self.active,
            "archived": self.archived,
            "deleted": self.deleted,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()