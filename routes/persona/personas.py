from flask import Blueprint,request,redirect,render_template,url_for
from models import Persona
from forms import PersonaForm
from app import db

apppersona = Blueprint('apppersona',__name__,template_folder="templates")

@apppersona.route('/')
@apppersona.route('/index')

def inicio():
    personas = Persona.query.all()
    return render_template('index.html', personas=personas)

@apppersona.route('/agregar',methods=["GET","POST"])
def agregar():
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('apppersona.inicio'))
    return render_template('agregar.html',forma=personaForm)

@apppersona.route("/editar/<int:id>",methods=["GET", "POST"])
def editar(id):
    persona = Persona.query.get_or_404(id)
    personaForm = PersonaForm(obj=persona)
    if(request.method == "POST"):
        if( personaForm.validate_on_submit() ):
            personaForm.populate_obj(persona)
            db.session.commit()
            return redirect(url_for('apppersona.inicio'))
    return render_template('editar.html',forma = personaForm)

@apppersona.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('apppersona.inicio'))

