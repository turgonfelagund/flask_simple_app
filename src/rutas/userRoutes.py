import os, sys
from flask import Blueprint

#Lineas para desarrollo
#modelo = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
#modelo = os.path.join(modelo, "modelo")
#sys.path.append(modelo)

#from src.modelo.modelo_mysql_connector import *

#import src.controlador.controlador

from controlador.controlador import pruebaUser, obtenerRegistros, getUserByName, insertUserController, deleteUserController, updateUserController

#Preparación de blueprint
userRoutes = Blueprint('bluetest', __name__);

#Rutas de blueprint
@userRoutes.route("/test1")
def prueba():
    return pruebaUser();

@userRoutes.route('/getall')
def getAll():
    return obtenerRegistros();

@userRoutes.route('/getuser/<nombre>')
def getUser(nombre):
    return getUserByName(nombre)

@userRoutes.route('/insert/<nombre>/<int:edad>', methods=['GET', 'POST'])
def insertUser(nombre, edad):
    return insertUserController(nombre, edad);

@userRoutes.route('delete/<int:user_id>')
def deleteUser(user_id):
    return deleteUserController(user_id);

@userRoutes.route('update/<int:id>/<nombre>/<int:edad>')
def updateUser(id, nombre, edad):
    datos = [nombre, edad, id]
    return updateUserController(datos);