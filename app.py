# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Permite peticiones desde el HTML local

@app.route('/sum', methods=['POST'])
def sum_matrices():
    data = request.get_json()
    matrix_a = data.get('matrixA')
    matrix_b = data.get('matrixB')
    
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[i])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
        
    return jsonify({"result": result})

@app.route('/mult', methods=['POST'])
def mult_matrices():
    data = request.get_json()
    matrix_a = data.get('matrixA')
    matrix_b = data.get('matrixB')
    
    r = len(matrix_a)
    c = len(matrix_a[0])
    
    result = []
    for i in range(r):
        row = []
        for j in range(c):
            suma = 0
            for k in range(c):
                suma += matrix_a[i][k] * matrix_b[k][j]
            row.append(suma)
        result.append(row)
        
    return jsonify({"result": result})

if __name__ == '__main__':
    # Corremos Python en el puerto 5000 para no chocar con NodeJS
    app.run(port=5000, debug=True)