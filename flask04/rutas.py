from flask import Flask, render_template
from flask import request
from flask import response
from flask import redirect, url_for
from modelos import Producto

app = Flask(__name__)

@app.route('/')
def inicio():
    productos = {Producto("Computadoras",200), Producto("Impresoras",50)}
    return render_template('index.html', productos=productos)

@app.route('/editar/<producto>/<precio>')
def editar(producto, precio):
    print(producto)
    return render_template('editar.html', producto=producto, precio=precio)

@app.route('/guardar', methods=['POST'])
def guardar():
    n= request.form.get['nombre']
    p= request.form.get['precio']
    print(n, p)
    i = 0
    for e in productos:
        if e.nombre == n:
            Producto[i] = Producto(n,p)
            print(f"{e.nombre} {e.precio}")
        i+=1
    return response("Guardado", headers={'Location':'/'}, status=302)

@app.route('/eliminar/<producto>')
def eliminar(producto):
    print(producto)
    i = 0
    for e in productos:
        if e.nombre == producto:
            productos.pop(i)
            print(f"{e.nombre} {e.precio}")
        i+=1
    return response("Eliminado", headers={'Location':'/'}, status=302)

@app.route('/agregar', methods=['POST'])
def agregar():
    n= request.form.get['nombre']
    p= request.form.get['precio']
    print(n, p)
    productos.append(Producto(n,p))
    return response("Agregado", headers={'Location':'/'}, status=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)