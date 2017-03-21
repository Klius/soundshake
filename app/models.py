from app import db

class user(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), nullable=False, index=True, unique=True)
	password = db.Column(db.String(64), nullable=False) #TODO: aixo s'haura de tocar!! Cripto etc
	profile_image = db.Column(db.String(400)) #TODO: aixo s'haura de tocar segur xD
	banner_image = db.Column(db.String(400))
	date_creation = db.Column(db.DateTime)

	def __repr__(self):
		return '<User %r>' % (self.nickname)

class person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
	name = db.Column(db.String(50), nullable=False, index=True)
	last_name = db.Column(db.String(100), index=True)
	musical_style = db.Column(db.String(200)) #see if we can use something dinamyc (with links like facebook tags, idk)
	description = db.Column(db.String(800))
	localization = db.Column(db.String(200))
	birth_date = db.Column(db.DateTime)
	fix_phone = db.Column(db.Integer)
	mobile_phone = db.Column(db.Integer)
	email = db.Column(db.String(254),index=True) #254 is the maximum length of a valid email address (StackOverflow)
	link1 = db.Column(db.String(250)) 
	link2 = db.Column(db.String(250))
	#TODO: need to add social networks

	def __repr__(self):
		return '<Person %r %r>' % (self.name, self.last_name)

class profession(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	description = db.Column(db.String(800))
	can_be_person = db.Column(db.Boolean, nullable=False)
	
	def __repr__(self):
		return '<Profession %r>' % (self.name)

class entity(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False, index=True)
	profession_id = db.Column(db.Integer, db.ForeignKey('profession.id', onupdate="CASCADE", ondelete="RESTRICT"), nullable=False, index=True)
	other_profession = db.Column(db.String(100))
	descripcion = db.Column(db.String(800))
	experience_time = db.Column(db.DateTime)
	localization = db.Column(db.String(200))
	phone_number1 = db.Column(db.Integer)
	phone_number2 = db.Column(db.Integer)
	email = db.Column(db.String(254),index=True) #254 is the maximum length of a valid email address (StackOverflow)
	link1 = db.Column(db.String(250)) 
	link2 = db.Column(db.String(250))
	#TODO: need to add social networks	

class band(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False, index=True, unique=True)	
	musical_style = db.Column(db.String(200)) #see if we can use something dinamyc (with links like facebook tags, idk)
	description = db.Column(db.String(800))
	localization = db.Column(db.String(200))
	creation_date = db.Column(db.DateTime)
	phone1 = db.Column(db.Integer)
	phone2 = db.Column(db.Integer)
	email = db.Column(db.String(254),index=True) #254 is the maximum length of a valid email address (StackOverflow)
	link1 = db.Column(db.String(250)) 
	link2 = db.Column(db.String(250))
	#TODO: need to add social networks

	def __repr__(self):
		return '<Band %r>' % (self.name)

class instrument(db.Model):
	__tablename__ = 'instrument'
	id = db.Column(db.Integer, primary_key=True)
	person_id = db.Column(db.Integer, db.ForeignKey('person.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False, index=True)
	instrument = db.Column(db.String(100), nullable=False)
	experience_time = db.Column(db.DateTime) #potser millor string o un integer...
	description = db.Column(db.String(800))
	__table_args__ = (
		UniqueConstraint('person_id', 'instrument')
	)

	def __repr__(self):
		return '<Instrument %r>' % (self.instrument)

class band_member(db.Model):
	__tablename__ = 'band_member'
	id = db.Column(db.Integer, primary_key=True)
	person_id = db.Column(db.Integer, nullable=False, index=True)
	band_id = db.Column(db.Integer, nullable=False, index=True)
	instrument_id = db.Column(db.Integer, nullable=False, index=True)
	__table_args__ = (
		UniqueConstraint('person_id', 'band_id', 'instrument_id', name='_band_member_instrument'),
		ForeignKeyConstraint(
			['person_id', 'band_id', 'instrument_id'],
			['person.id', 'band.id', 'instrument.id'],
			onupdate="CASCADE", ondelete="CASCADE"
		)
	)