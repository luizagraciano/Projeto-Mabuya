from flask import Blueprint, redirect, render_template, request, session, url_for
from src.data.db import get_db

#Cria a blueprint do módulo de avistamentos
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

        #Redireciona para página com todos os avistamentos
        return redirect(url_for('avistamento.ler'))

    #Renderiza a página de cadastrar um avistamento
    return render_template('avistamento/criar.html')


@bp.route('/todos')
#LER
def ler():
        
    #Chama o banco de dados e coleta valores de todos os avistamentos cadastrados
    db = get_db()
    avistamentos = db.execute(
        'SELECT * FROM avistamento ORDER BY data_avistamento DESC'
    ).fetchall()
    
    #Renderiza a página com todos os avistamentos
    return render_template('avistamento/leitura.html', avistamentos=avistamentos)


#COLETAR AVISTAMENTO POR ID
def get_avistamento(id):

    #Chama o banco de dados e coleta valores de um avistamento específico
    db = get_db()
    avistamento = db.execute(
        'SELECT * FROM avistamento WHERE id = ?', (id,)
    ).fetchone()

    return avistamento
 

@bp.route('/<int:id>/editar', methods=('GET', 'POST'))
#EDITAR
def editar(id):

    #Identifica e seleciona o avistamento
    avistamento = get_avistamento(id)

    if request.method == 'POST':
        #Lê formulário
        especie = request.form ['especie']
        local = request.form ['local']
        comentario = request.form ['comentario']

        #Chama o banco de dados e edita valores
        db = get_db()
        db.execute(
            'UPDATE avistamento SET nome_especie = ?, local_avistamento = ?, comentario = ? WHERE id = ?',
            (especie, local, comentario, id)
        )
        db.commit()

        #Redireciona para página com todos os avistamentos
        return redirect(url_for('avistamento.ler'))
    
    #Renderiza página de editar um avistamento
    return render_template('avistamento/editar.html', avistamento=avistamento)


@bp.route('/<int:id>/deletar')
#DELETAR
def deletar(id):

    #Identifica e seleciona o avistamento
    get_avistamento(id)

    #Chama o banco de dados e edita valores
    db = get_db()
    db.execute(
        'DELETE FROM avistamento WHERE id = ?', (id,)
        )
    db.commit()

    return redirect(url_for('avistamento.ler'))