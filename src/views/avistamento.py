from flask import Blueprint, redirect, render_template, request, session, url_for
from src.data.db import get_db

bp = Blueprint('avistamento', __name__, url_prefix='/avistamento')


@bp.route('/novo', methods=('GET', 'POST'))

#CREATE
def criar():
    if request.method == 'POST':

        #Lê formulário
        especie = request.form ['especie']

        local = request.form ['local']
        comentario = request.form ['comentario']

        #Chama o banco de dados e insere valores
        db = get_db()

        db.execute(
            'INSERT INTO avistamento (nome_especie, local_avistamento, comentario) VALUES (?, ?, ?)',
            (especie, local, comentario)
        )
        db.commit()

        return redirect(url_for('avistamento.ler'))

    return render_template('avistamento/criar.html')


@bp.route('/todos')

#LER
def ler():
        
    #Chama o banco de dados e insere valores
    db = get_db()

    avistamentos = db.execute(
        'SELECT * FROM avistamento ORDER BY data_avistamento DESC'
    ).fetchall()
    
    return render_template('avistamento/leitura.html', avistamentos=avistamentos)