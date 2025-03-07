from flask import Flask, render_template
from modelos import Producto

app = Flask(__name__)

@app.route('/')
def inicio():
    productos = {Producto("Manzanas",19), Producto("Peras",20)}
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)