from app import db

class Persona(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))

class Producto(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))
    precio = db.Column(db.String(255))
    nombre = db.Column(db.String(255))

class Images(db.Model):
    __tablename__="imagenes"
    id=db.Column(db.Integer, primary_key=True)
    type=db.Column(db.String(255),nullable=False)
    data=db.Column(db.LargeBinary,nullable=False)
    renderData = db.Column(db.Text)
