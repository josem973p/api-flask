#importaciones
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


# conexion db e inicio app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:418103812@localhost/api-flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class alunmno(db.Model):
   
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

#endpoints

@app.route('/', methods=['GET'])
def index():
    return jsonify({'mensaje': 'endpint raiz'})


#main
if __name__ == "__main__":
    app.run(debug=True)


