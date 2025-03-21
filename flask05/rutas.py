from flask import Flask, render_template
from flask import request
from flask import response
from flask import redirect, url_for
from modelos import Producto
import sqlite3

app = Flask(__name__)

@app.route('/')
def inicio():
    productos = {Producto("Computadoras",200), Producto("Impresoras",50)}
    return render_template('index.html', productos=productos)

@app.route('/editar/<producto>/<precio>')
def editar(id):
    conexion = conexion()
    p = conexion.execute('SELECT * FROM productos WHERE id = ?', (id,)).fetchone()
    #print(producto)
    conexion.close()
    return render_template('editar.html', producto=producto, precio=precio)

@app.route('/guardar', methods=['POST'])
def guardar():
    n= request.form.get['nombre']
    p= request.form.get['precio']
    id= request.form.get['id']
    print(f"{n}, {p}, {id}")
    #i = 0
    #for e in productos:
    #    if e.nombre == n:
    #        Producto[i] = Producto(n,p)
    #        print(f"{e.nombre} {e.precio}")
    #    i+=1
    conexion = conexion()
    conexion.execute('UPDATE productos SET nombre = ?, precio = ? WHERE id = ?', (n,p,id))
    conexion.commit()
    conexion.close()
    return response("Guardado", headers={'Location':'/'}, status=302)

@app.route('/eliminar/<id>')
def eliminar(id):
    #print(producto)
    #i = 0
    #for e in productos:
    #    if e.nombre == producto:
    #        productos.pop(i)
    #        print(f"{e.nombre} {e.precio}")
    #    i+=1
    conexion = conexion()
    conexion.execute('DELETE FROM productos WHERE id = ?', (id,))
    conexion.commit()
    conexion.close()
    return response("Eliminado", headers={'Location':'/'}, status=302)

@app.route('/crear', methods=['POST'])
def crear():
    n= request.form.get['nombre']
    p= request.form.get['precio']
    #print(n, p)
    #productos.append(Producto(n,p))
    conexion = conexion()
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO productos (nombre, precio) VALUES (?,?)', (n,p))
    conexion.commit()
    conexion.close()
    return response("Agregado", headers={'Location':'/'}, status=302)

def conexion():
    conexion = sqlite3.connect('productos.db')
    #cursor = conexion.cursor()
    #cursor.execute('CREATE TABLE IF NOT EXISTS productos (nombre TEXT, precio REAL)')
    #conexion.commit()
    #conexion.close()
    conexion.row_factory = sqlite3.Row
    return conexion

def iniciar_db():
    conexion = conexion()
    cursor = conexion.cursor()
    cursor.execute(''
    'CREATE TABLE IF NOT EXISTS productos '
    '(id INTEGRED PRIMARY KEY, nombre TEXT NOT NULL, precio REAL NOT NULL)')
    conexion.commit()
    conexion.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)