#importaciones
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# conexion db e inicio app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:418103812@localhost/api-flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class alumno(db.Model):
   
    idalumnos = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    apellido = db.Column(db.String(45))
    edad =db.Column(db.Integer)
    carreraId = db.Column(db.Integer)
    materiaId = db.Column(db.Integer)


    def __init__(self, nombre, apellido,edad,carreraId, materiaId):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.carreraId = carreraId
        self.materiaId = materiaId

db.create_all()

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('nombre', 'apellido', 'edad','carreraId','materiaId')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

#endpoints

@app.route('/', methods=['GET'])
def index():
    return jsonify({'mensaje': 'endpint raiz'})

@app.route('/post', methods=['POST'])
def createAlumnos():
    nombre= request.json['nombre']
    apellido = request.json['apellido']
    edad = request.json['edad']
    carreraId = request.json['carreraId']
    materiaId = request.json['materiaId']

    newAlumno = alumno(nombre,apellido, edad, carreraId,materiaId)
    db.session.add(newAlumno)
    db.session.commit()
    return task_schema.jsonify(newAlumno)


#main
if __name__ == "__main__":
    app.run(debug=True)


