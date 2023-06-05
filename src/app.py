from flask import Flask, url_for, redirect, render_template, jsonify, make_response;
import os, sys;
from errores.errores import server_internal_error, page_not_found

#Impotante que se declare antes de importar userRoutes debido a localizacion de archivo "configdb_mysql_connector.py"
#Porque existen modulos que requieren la rutaRaiz para ser encontrados
rutaRaiz = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
sys.path.append(rutaRaiz);

from rutas.userRoutes import userRoutes;


app = Flask(__name__);

#Declaración de directorio de plantillas
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)));
template_dir = os.path.join(template_dir, "src", "templates");

#Configuración de directorio de estilos
css_dir = os.path.join(app.static_url_path, "css")


#Se declara el módulo o script actual
#Se indica el directorio de plantillas a renderizar
app = Flask(__name__, template_folder= template_dir);


@app.route('/')
def index():
    #render_template() permite renderizar componenetes
    return render_template("index.html"), 200;
    #return "Hola mundo";

#Ejemplo de redirección
@app.route('/redirect')
def redireccion():
    return redirect("saludo");

#Ejemplo de respuesta
@app.route('/test', methods=['GET'])
def crearRespuesta():
    #return redirect("saludo");
    response_obj = jsonify([{"persona" : "Juan", "accion" : "saludo"},
                    {"persona" : "Marina", "accion" : "responde"}]);
    
    response = make_response(response_obj);
    response.headers['header1'] = "test header"
    response.status=200
    return response;

#Obtiene la url que mapea un determinado método
@app.route("/testurl")
def obtenerUrl():
    #devuelve la variable del método saludar()
    return url_for('saludo');

@app.route('/saludarurl', methods=['GET'])
def saludo():
    return "Hola mundooo", 200;

#BLUEPRINTS
#Permite enrutar a un subconjunto de url's
app.register_blueprint(userRoutes, url_prefix = "/users") #url_prefix es el fragemento de url que mapea la blueprint



#ERRORES
app.register_error_handler(404, page_not_found);
app.register_error_handler(500, server_internal_error);

#Ejecucion
if __name__ == "__main__":
    app.run(debug=True, port=5500); #Deshabilitar debug para producción
