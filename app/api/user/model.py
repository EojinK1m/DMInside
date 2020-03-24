from app import db, ma


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(16), unique=True, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), unique=True)
    profile_image = db.Column(db.Integer, unique=True, nullable=True)
    explain = db.Column(db.Text, nullable=True)

    posts = db.relationship('PostModel', backref='uploader')
    galleries = db.relationship('GalleryModel', backref='master')


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel()

    username = ma.auto_field()
    explain = ma.auto_field()
    profile_image = ma.auto_field()


user_schema = UserSchema()
users_schema = UserSchema(many=True, only=['username', 'profile_image'])