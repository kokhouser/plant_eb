from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    plants = db.relationship('Plant', backref='addedBy', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Plant(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	commonName = db.Column(db.String(255))
	latinName = db.Column(db.String(255))
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Plant %r>' % (self.commonName)