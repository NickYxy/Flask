from . import ModelMixin
from . import db
from . import timestamp


class Topic(db.Model, ModelMixin):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)
    created_time = db.Column(db.Integer)

    user_id = db.Column(db.Integer)

    # chats = db.relationship('Chat', backref='channel', lazy='dynamic')

    def __init__(self, form):
        self.title = form.get('title', '')
        self.text = form.get('text', '')
        self.user_id = form.get('user_id', '')
        self.created_time = timestamp()

    def update(self, form):
        self.title = form.get('title', '')
        self.text = form.get('text', '')
