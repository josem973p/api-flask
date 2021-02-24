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

class alumnoSchema(ma.Schema):
    class Meta:
        fields = ('nombre', 'apellido', 'edad','carreraId','materiaId')

alumno_schema = alumnoSchema()
alumnos_schema = alumnoSchema(many=True)

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

@app.route('/postMateria', methods=['POST'])
def createMateria():
    mat= request.json['materia']
    newMateria = materia(mat)
    db.session.add(newMateria)
    db.session.commit()
    return materia_schema.jsonify(newMateria)


@app.route('/tableAlumno', methods=['GET'])
def get_tableAlumnos():
  data = alumno.query.all()
  result = alumnos_schema.dump(data)
  return jsonify(result)

@app.route('/tableCarrera', methods=['GET'])
def get_tableCarera():
  data = carrera.query.all()
  result = carreras_schema.dump(data)
  return jsonify(result)

@app.route('/tableMateria', methods=['GET'])
def get_tableMateria():
  data = materia.query.all()
  result = materias_schema.dump(data)
  return jsonify(result)

 
@app.route('/updateAlumno/<id>', methods=['PUT'])
def updateAlumno(id):
  data = alumno.query.get(id)

  nombre= request.json['nombre']
  apellido = request.json['apellido']
  edad = request.json['edad']
  carreraId = request.json['carreraId']
  materiaId = request.json['materiaId']

  data.nombre=nombre
  data.apellido=apellido
  data.edad=edad
  data.carreraId=carreraId
  data.materiaId=materiaId

  db.session.commit()
  
 
  return jsonify({
      "mensaje":"modificado correctamente"
  })

@app.route('/updateCarrera/<id>', methods=['PUT'])
def updateCarrera(id):
  data = carrera.query.get(id)
  carr= request.json['carrera']
  data.carrera=carr
  db.session.commit()
  return jsonify({
      "mensaje":"modificado correctamente"
  })

@app.route('/updateMateria/<id>', methods=['PUT'])
def updateMateria(id):
  data = materia.query.get(id)
  mat= request.json['materia']
  data.materia=mat
  db.session.commit()
  return jsonify({
      "mensaje":"modificado correctamente"
  })

'''___ manejor de errores ___ '''
@app.errorhandler(404)
def not_found(error):
    return jsonify({'mensaje': 'lo siento no se encuentra lo que buscas'})

@app.errorhandler(500)
def server_error(error):
    return jsonify({'mensaje': 'error interno :('})

#main
if __name__ == "__main__":
    app.run(debug=True)


