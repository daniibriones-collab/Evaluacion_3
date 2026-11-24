from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():

    nota1 = ''
    nota2 = ''
    nota3 = ''
    asistencia = ''
    promedio = None
    estado = ''

    if request.method == 'POST':

        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado = 'Aprobado'
        else:
            estado = 'Reprobado'

    return render_template('ejercicio1.html',
                           nota1=nota1,
                           nota2=nota2,
                           nota3=nota3,
                           asistencia=asistencia,
                           promedio=promedio,
                           estado=estado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():

    nombre1 = ''
    nombre2 = ''
    nombre3 = ''
    nombre_mayor = ''
    cantidad = 0

    if request.method == 'POST':

        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombre_mayor = nombre1

        if len(nombre2) > len(nombre_mayor):
            nombre_mayor = nombre2

        if len(nombre3) > len(nombre_mayor):
            nombre_mayor = nombre3

        cantidad = len(nombre_mayor)

    return render_template('ejercicio2.html',
                           nombre1=nombre1,
                           nombre2=nombre2,
                           nombre3=nombre3,
                           nombre_mayor=nombre_mayor,
                           cantidad=cantidad)


if __name__ == '__main__':
    app.run(debug=True)