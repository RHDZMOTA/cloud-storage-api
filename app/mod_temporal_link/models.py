from app import db


class BaseModel(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer,primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modify = db.Column(db.DateTime,
                            default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp())


class User(BaseModel):
    __tablename__ = 'user'

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)
    # Authorization
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User; name={name}; email={email}>'.format(name=self.name, email=self.email)

