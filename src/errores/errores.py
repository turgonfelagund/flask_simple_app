from flask import render_template
import os

src_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)));
template_dir = os.path.join(src_dir, 'templates');

#En este caso el directorio debe ser relativo para que se encuentre el recurso css
#Con ruta absoluta no funciona
static_dir = os.path.relpath("static")
css_dir = os.path.join(static_dir, "css")


def page_not_found(error): #Argumento obligatorio
    #No es necesario pasar el código de error
    return render_template("404.html", css_url = css_dir.replace("\\", "/") + '/404.css');


def server_internal_error(error):

    #No es necesario pasar el código de error
    return "Hay un error interno de servidor";