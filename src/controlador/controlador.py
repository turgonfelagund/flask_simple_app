from modelo.modelo_mysql_connector import getAll, getUserByNameModel, insertUserModel, deleteUserModel, updateUserModel
from flask import jsonify, make_response;

def pruebaUser():
    return "Prueba exitosa";

def obtenerRegistros():
    print(getAll);
    return getAll();

def getUserByName(nombre):
    return getUserByNameModel([nombre]);

def insertUserController(nombre, edad):

    success = insertUserModel([nombre, edad]);

    if(success):
        response_obj = make_response(jsonify({"Resultado" : "El usuario fué insertado con éxito"}));
        response_obj.status = 200;
    else:
        response_obj = make_response(jsonify({"Resultado" : "No se pudo insertar con éxito al usuario"}));
        response_obj.status = 500;

    response_obj.headers['consulta'] = 'inserción de usuario';

    return  response_obj;

def deleteUserController(user_id):

    success = deleteUserModel([user_id]);

    mensajeSuccess = '''Se eliminó con éxito al usuario {}'''.format(user_id);
    mensajeFail = '''No se pudo eliminar al usuario {}'''.format(user_id);

    return prepararRespuesta("borrado", success, mensajeSuccess, mensajeFail);

def updateUserController(datos):

    success = updateUserModel(datos);

    mensajeSuccess = '''Se actualizó con éxito al usuario {}'''.format(datos[0]);
    mensajeFail = '''No se pudo actualizar al usuario {}'''.format(datos[0]);

    return prepararRespuesta('actualizar', success, mensajeSuccess, mensajeFail);





def prepararRespuesta(header, success, exito, error):

    if(success):
        response_obj = make_response(jsonify({"Resultado" : exito}));
        response_obj.status = 200;
    else:
        response_obj = make_response(jsonify({"Resultado" : error}));
        response_obj.status = 500;

    response_obj.headers['consulta'] = header;

    return  response_obj;