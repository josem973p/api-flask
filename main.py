#importaciones
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# conexion db e inicio app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:418103812@flask.cvowhhzoj0ol.us-east-2.rds.amazonaws.com/api_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
'''______________________________________________________________________________________'''
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

class alumnochema(ma.Schema):
    class Meta:
        fields = ('nombre', 'apellido', 'edad','carreraId','materiaId')

alumno_schema = alumnochema()
alumno_schema = alumnochema(many=True)

'''______________________________________________________________________________________'''

class materia(db.Model):
   
    idmateria = db.Column(db.Integer, primary_key=True)
    materia = db.Column(db.String(45))
  


    def __init__(self, materia):
        self.materia = materia
     

db.create_all()

class materiaSchema(ma.Schema):
    class Meta:
        fields = ('materia',)

materia_schema = materiaSchema()
materias_schema = materiaSchema(many=True)

'''______________________________________________________________________________________'''

'''______________________________________________________________________________________'''

class carrera(db.Model):
   
    idcarrera = db.Column(db.Integer, primary_key=True)
    carrera = db.Column(db.String(45))
  


    def __init__(self, carrera):
        self.carrera = carrera
     

db.create_all()

class carreraSchema(ma.Schema):
    class Meta:
        fields = ('carrera',)

carrera_schema = carreraSchema()
carreras_schema = carreraSchema(many=True)

'''______________________________________________________________________________________'''


#endpoints

@app.route('/', methods=['GET'])
def index():
    return jsonify({'mensaje': 'endpoint raiz'})

@app.route('/postAlumno', methods=['POST'])
def createAlumnos():
    nombre= request.json['nombre']
    apellido = request.json['apellido']
    edad = request.json['edad']
    carreraId = request.json['carreraId']
    materiaId = request.json['materiaId']

    newAlumno = alumno(nombre,apellido, edad, carreraId,materiaId)
    db.session.add(newAlumno)
    db.session.commit()
    return alumno_schema.jsonify(newAlumno)

@app.route('/postCarrera', methods=['POST'])
def createCarrera():
    car= request.json['carrera']
    newCarrera = carrera(car)
    db.session.add(newCarrera)
    db.session.commit()
    return carrera_schema.jsonify(newCarrera)


@app.route('/table/<tabla>', methods=['GET'])
def get_tasks(tabla):
  data = tabla.query.all()
  result = tasks_schema.dump(data)
  return jsonify(result)


#main
if __name__ == "__main__":
    app.run(debug=True)


