from app import db

class TipoUsuario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(50))
	descripcion = db.Column(db.String(400))
	imagen = db.Column(db.String(400))
	
	def __repr__(self):
		return '<Tipo Usuario %r>' % (self.nombre)



class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	mail = db.Column(db.String(140),index=True, unique=True)
	genero = db.Column(db.String(10),index=True)
	password = db.Column(db.String(60))
	nombre = db.Column(db.String(60))
	descripcion = db.Column(db.String(240))
	imagen_perfil = db.Column(db.String(400))
	imagen_banner = db.Column(db.String(400))
	posts = db.relationship('Post', backref='author', lazy='dynamic')
	comentarios = db.relationship('Comentario',backref='comment', lazy='dynamic')
	id_tipo_usuario = db.Column(db.Integer,db.ForeignKey('tipo_usuario.id'))
	
	def __repr__(self):
		return '<User %r>' % (self.nombre)


class Post(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	titulo = db.Column(db.String(140))
	contenido = db.Column(db.String(65535))
	fecha = db.Column(db.DateTime)
	comentarios = db.relationship('Comentario', backref='comment', lazy='dynamic')
	id_usuario = db.Column(db.Integer,db.ForeignKey('usuario.id')) 
	
	def __repr__(self):
		return '<Post %r>' % (self.titulo)

class Comentario(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	contenido = db.Column(db.String(65535))
	fecha = db.Column(db.DateTime)
	id_post = db.Column(db.Integer, db.ForeignKey('post.id'))
	id_usuario = db.Column(db.Integer,db.ForeignKey('usuario.id'))
	
	def __repr__(self):
		return '<Respuesta %r>' % (self.contenido)
		
