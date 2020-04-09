from app import db, ma


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(16), unique=True, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id', ondelete='CASCADE'), unique=True)
    explain = db.Column(db.Text, nullable=True)

    posts = db.relationship('PostModel', backref='uploader')
    profile_image = db.relationship('ImageModel', uselist=False)

    def delete_user(self):
        db.session.delete(self)


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel()


    username = ma.auto_field()
    explain = ma.auto_field()
    profile_image = ma.Nested('ImageSchema', only=["url"])


user_schema = UserSchema()
users_schema = UserSchema(many=True, only=['username', 'profile_image'])