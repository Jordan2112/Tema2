# from flask import Flask,render_template,request,url_for
# from werkzeug.exceptions import abort
# from werkzeug.utils import redirect
# import logging

# app = Flask(__name__)
# logging.basicConfig(filename='error.log',level=logging.DEBUG)

# @app.route('/')
# def index():
#     return f"Index app"

# @app.route('/login',methods=["GET","POST"])
# def login():
#     if(request.method == 'POST'):
#         redirect('/')
#     else:
#         return render_template('login.html')
    
# @app.route('/juego',methods=["POST"])
# def agregarJuego():
#     try:
#         token = request.headers.get('token')
#         app.logger.debug(f"token:{token}")
#         info = request.headers.get_json()
#         nombre = info['nombre']
#         precio = info['precio']
#         return f"Nombre {nombre} , precio {precio}, Token {token}"
#     except:
#         return abort(404)
    
# @app.errorhandler(404)
# def pageNotFound(error):
#     return render_template("error.html", error=error),404

from flask import Flask
from database import db
from config import BasicConfig
from flask_migrate import Migrate
import logging

from routes.persona.personas import apppersona
from routes.producto.producto import appproducto
from routes.imagen.imagen import appImagen

app= Flask(__name__)
app.register_blueprint(apppersona)
app.register_blueprint(appproducto)
app.register_blueprint(appImagen)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename="logs.log")










