import os
import time
import random
import flask_bcrypt
from flask_cors import CORS
from flask import json, jsonify, request, url_for, redirect, session, make_response, send_from_directory
from flask import abort, render_template, render_template_string, Flask, flash
from flask_restful import Resource, Api
import traceback
import configparser
import mysql.connector

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 50
app.config['UPLOAD_PATH'] = 'uploads'
app.config['TEMPLATES_AUTO_RELOAD'] = True

secret = os.urandom(32)
app.config['SECRET_KEY'] = secret
app.secret_key = secret

bcrypt = flask_bcrypt.Bcrypt(app)
CORS(app)
api = Api(app)
PORT_FLASK = 5000

# -- Read INI file
CONFIGFILE = configparser.ConfigParser()
CONFIGFILE.read('config.ini')

#-- DATABASE
USE_SECTION = CONFIGFILE['database']['use_section']
DRIVER =  CONFIGFILE[USE_SECTION]['driver']

HOST = CONFIGFILE[USE_SECTION]['host']
DATABASE = CONFIGFILE[USE_SECTION]['database']
USER = CONFIGFILE[USE_SECTION]['user']
PASSWORD = CONFIGFILE[USE_SECTION]['password']
PORT = int(CONFIGFILE[USE_SECTION]['port'])


class ManageDatabase(object):
    #-- https://www.psycopg.org/docs/usage.html
    #-- https://pynative.com/python-postgresql-select-data-from-table/
    #-- https://zetcode.com/python/psycopg2/
    def __init__(self):
        pass

    @staticmethod
    def open_connection():
        """
        Establece una conexion con la base de datos
        """
        try:
            CONN = mysql.connector.connect(
                host=HOST,
                database=DATABASE,
                user=USER,
                password=PASSWORD,
                port=PORT,)
            #-- Retornar resultado como diccionarios, accesibles por el nombre de la columna
            cursor = CONN.cursor(dictionary=True)
        except:
            return (None, None, False, traceback.format_exc())
        return (CONN, cursor, True, 'OK')
    
    @staticmethod
    def close_connection(*args):
        """
        Cierra todas las conexiones agrupadas en el parametro
        Todo objeto en la conexion debe contener el metodo -close-
        """

        for obj in args:
            try:
                obj.close()
            except Exception as e:
                continue

def obtener_marcas():
    dbconn, cursor, status, error = ManageDatabase.open_connection()
    sql_query = """
    SELECT 
        *
    FROM 
        marcas
    WHERE TRUE;
    """
    cursor.execute(sql_query)
    marcas = cursor.fetchall()
    ManageDatabase.close_connection(dbconn, cursor)
    return marcas

def obtener_semillas():
    dbconn, cursor, status, error = ManageDatabase.open_connection()
    sql_query = """
    SELECT 
        *
    FROM 
        productos
    WHERE id_categoria=4;
    """
    cursor.execute(sql_query)
    semillas = cursor.fetchall()
    ManageDatabase.close_connection(dbconn, cursor)
    return semillas

def obtener_fertilizantes():
    dbconn, cursor, status, error = ManageDatabase.open_connection()
    sql_query = """
    SELECT 
        *
    FROM 
        productos
    WHERE id_categoria=3;
    """
    cursor.execute(sql_query)
    fertilizantes = cursor.fetchall()
    ManageDatabase.close_connection(dbconn, cursor)
    return fertilizantes

def obtener_sustratos():
    dbconn, cursor, status, error = ManageDatabase.open_connection()
    sql_query = """
    SELECT 
        *
    FROM 
        productos
    WHERE id_categoria=1;
    """
    cursor.execute(sql_query)
    sustratos = cursor.fetchall()
    ManageDatabase.close_connection(dbconn, cursor)
    return sustratos

def obtener_parafernalias():
    dbconn, cursor, status, error = ManageDatabase.open_connection()
    sql_query = """
    SELECT 
        *
    FROM 
        productos
    WHERE id_categoria=5;
    """
    cursor.execute(sql_query)
    parafernalias = cursor.fetchall()
    ManageDatabase.close_connection(dbconn, cursor)
    return parafernalias
    
def obtener_iluminarias():
    dbconn, cursor, status, error = ManageDatabase.open_connection()
    sql_query = """
    SELECT 
        *
    FROM 
        productos
    WHERE id_categoria=2;
    """
    cursor.execute(sql_query)
    iluminarias = cursor.fetchall()
    ManageDatabase.close_connection(dbconn, cursor)
    return iluminarias

def obtener_categorias():
    dbconn, cursor, status, error = ManageDatabase.open_connection()
    sql_query = """
    SELECT 
        *
    FROM 
        categorias
    WHERE TRUE;
    """
    cursor.execute(sql_query)
    categorias = cursor.fetchall()
    ManageDatabase.close_connection(dbconn, cursor)
    return categorias

def obtener_productos():
    dbconn, cursor, status, error = ManageDatabase.open_connection()
    sql_query = """
    SELECT 
        *
    FROM 
        productos
    WHERE disponibilidad=%s AND id_categoria=%s;
    """
    cursor.execute(sql_query,(True, 4))
    productos = cursor.fetchall()
    ManageDatabase.close_connection(dbconn, cursor)
    
    return productos

@app.route('/show_menu/<int:marca_id>', methods=['GET'])
def show_menu(marca_id:int):
    dbconn, cursor, status, error = ManageDatabase.open_connection()
    sql_query = """
    SELECT 
        *
    FROM 
        productos
    WHERE disponibilidad=%s AND id_marca=%s;
    """
    cursor.execute(sql_query,(True, marca_id))
    prod_por_marca = cursor.fetchall()
    ManageDatabase.close_connection(dbconn, cursor)
    
    productos = obtener_productos()
    categorias = obtener_categorias()
    semillas = obtener_semillas()
    marcas = obtener_marcas()
    iluminarias = obtener_iluminarias()
    fertilizantes = obtener_fertilizantes()
    sustratos = obtener_sustratos()
    parafernalias = obtener_parafernalias()
    
    return render_template('show_menu.html', prod_por_marca=prod_por_marca,productos=productos, categorias=categorias, semillas=semillas, marcas=marcas, iluminarias=iluminarias, fertilizantes=fertilizantes, sustratos=sustratos, parafernalias=parafernalias)

@app.route('/show/<int:product_id>', methods=['GET'])
def show(product_id:int):
    productos = obtener_productos()
    categorias = obtener_categorias()
    semillas = obtener_semillas()
    marcas = obtener_marcas()
    iluminarias = obtener_iluminarias()
    fertilizantes = obtener_fertilizantes()
    sustratos = obtener_sustratos()
    parafernalias = obtener_parafernalias()
    
    dbconn, cursor, status, error = ManageDatabase.open_connection()
    sql_query = """
    SELECT 
        *
    FROM 
        productos
    WHERE id=%s;
    """
    cursor.execute(sql_query,(product_id,))
    producto = cursor.fetchone()
    ManageDatabase.close_connection(dbconn, cursor)
    
    return render_template('show.html', object=producto, productos=productos, categorias=categorias, semillas=semillas, marcas=marcas, iluminarias=iluminarias, fertilizantes=fertilizantes, sustratos=sustratos, parafernalias=parafernalias, ruta_imagen = producto['image_url'])


@app.route('/', methods = ['GET'])
def main_page():
    """
    Mostrar pagina principal
    """

    productos = obtener_productos()
    categorias = obtener_categorias()
    semillas = obtener_semillas()
    marcas = obtener_marcas()
    iluminarias = obtener_iluminarias()
    fertilizantes = obtener_fertilizantes()
    sustratos = obtener_sustratos()
    
    return render_template('main_page.html', productos=productos, categorias=categorias, semillas=semillas, marcas=marcas, iluminarias=iluminarias, fertilizantes=fertilizantes, sustratos=sustratos)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('500.html', error=str(traceback.format_exc())), 500

if __name__ == '__main__':
    app.run()