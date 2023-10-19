from flask import Blueprint,jsonify,request
from models import Producto
from app import db

appproducto = Blueprint("appproducto",__name__)
@appproducto.route('/producto/agregar',methods=["POST"])
def agregarProducto():
    try:
        json = request.get_json()
        producto = Producto()
        producto.nombre = json['nombre']
        producto.descripcion = json['descripcion']
        producto.precio = json['precio']
        db.session.add(producto)
        db.session.commit()
        return jsonify({"status":400,"mensaje":"Producto"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})
    

appproducto = Blueprint("appproducto",__name__)
@appproducto.route('/producto/editar',methods=["POST"])
def editarProducto():
    try:
        json = request.get_json()
        producto = Producto().query.get_or_404(json["id"])
        producto.nombre = json['nombre']
        producto.descripcion = json['descripcion']
        producto.precio = json['precio']
        db.session.add(producto)
        db.session.commit()
        return jsonify({"status":400,"mensaje":"Producto modificado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

appproducto = Blueprint("appproducto",__name__)
@appproducto.route('/producto/eliminar',methods=["POST"])
def eliminarProducto():
    try:
        json = request.get_json()
        producto = Producto().query.get_or_404(json["id"])

        db.session.delete(producto)
        db.session.commit()
        return jsonify({"status":400,"mensaje":"Producto eliminado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appproducto.route('/producto/obtener')
def obtenerProducto():
    producto = Producto.query.all()
    listaProducto=[]
    for p in listaProducto:
        producto={}
        producto["nombre"] = p.nombre
        producto["descripcion"] = p.descripcion
        producto["precio"] = p.precio
        listaProducto.append(producto)
    return 

