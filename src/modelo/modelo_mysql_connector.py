from configdb_mysql_connector import db
import os, sys;

rutardo = os.path.dirname(os.path.abspath("./src/rutas"));
sys.path.append(rutardo);

consultas = {
    "getAll": "SELECT * FROM usuario",
    "getUserByName" : "SELECT * FROM usuario WHERE nombre = %s",
    "insertUser" : "INSERT INTO usuario (nombre, edad) VALUES (%s, %s)",
    "deleteUser" : "DELETE FROM usuario WHERE id = %s",
    "updateUser" : "UPDATE usuario SET nombre = %s, edad= %s WHERE id = %s"
}

def consultaSelect(request):
    def ejecutarSelect(datos = None):
        cursor = db.cursor();

        cursor.execute(request) if datos == None else cursor.execute(request, datos) ;

        field_names = [desc[0] for desc in cursor.description]

        filas = cursor.fetchall();
        resultado = [];

        for row in filas:
            row_dict = dict(zip(field_names, row));
            resultado.append(row_dict);

        cursor.close();
        #db.close();

        return resultado;

    return ejecutarSelect;

def consultaModificacion(request):
    def ejecutarConsulta(datos = None):

        cursor = db.cursor();
        cursor.execute(request, datos);

        if cursor.rowcount > 0:
            db.commit()
            return True;
        else:
            db.rollback()
            return False;

        cursor.close();

    return ejecutarConsulta;


#Consultas de selección
getAll = consultaSelect(consultas['getAll']);
getUserByNameModel = consultaSelect(consultas['getUserByName'])

#Consultas de inserción
insertUserModel = consultaModificacion(consultas['insertUser']);

#Consultas de borrado
deleteUserModel = consultaModificacion(consultas['deleteUser'])

#Consultas de modición
updateUserModel = consultaModificacion(consultas['updateUser'])