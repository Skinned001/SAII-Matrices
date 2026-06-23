// server.js
const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors()); // Permite peticiones desde el navegador (HTML local)
app.use(express.json());

app.post('/sum', (req, res) => {
    const { matrixA, matrixB } = req.body;
    
    let result = [];
    for (let i = 0; i < matrixA.length; i++) {
        let row = [];
        for (let j = 0; j < matrixA[i].length; j++) {
            row.push(matrixA[i][j] + matrixB[i][j]);
        }
        result.push(row);
    }
    
    res.json({ result });
});

app.post('/mult', (req, res) => {
    const { matrixA, matrixB } = req.body;
    const r = matrixA.length;
    const c = matrixA[0].length;
    
    let result = [];
    for (let i = 0; i < r; i++) {
        let row = [];
        for (let j = 0; j < c; j++) {
            let sum = 0;
            for (let k = 0; k < c; k++) {
                sum += matrixA[i][k] * matrixB[k][j];
            }
            row.push(sum);
        }
        result.push(row);
    }
    
    res.json({ result });
});

app.listen(3000, () => {
    console.log('Servidor NodeJS corriendo en http://localhost:3000');
});