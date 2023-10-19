from flask import Blueprint,request,render_template

from models import Images
from app import db
import base64

appImagen = Blueprint("appImagen",__name__,template_folder="vistas")

def renderImage(data):
    imagenRenderizada = base64.b16decode(data).decode('ascci')
    return imagenRenderizada

@appImagen.route('/leerImagen/<int:id>')
def leerImagen():
    imagen = Images.query.filter_by(id=1).first().renderData
    return render_template('mostrarImagen.html', imagen=imagen)

@appImagen.route('/leerImagen',methods=["POST","GET"])
def indexImagen():
    if request.method == 'POST':
        file = request.files['img']
        data = file.read()
        render = renderImage(data)
        nuevaImagen = Images()
        nuevaImagen.type='Perfil'
        nuevaImagen.renderData = render
        nuevaImagen.data = data
        db.session.add(nuevaImagen)
        db.session.commit()
    return render_template('imagenes.html')

