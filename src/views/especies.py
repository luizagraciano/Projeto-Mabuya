from flask import Blueprint, redirect, render_template, request, session, url_for
from src.data.db import get_db

#Cria a blueprint do módulo de avistamentos
bp = Blueprint('especies', __name__, url_prefix='/especies')

@bp.route('/<nome>')
def especie(nome):
    db = get_db()
    especie = db.execute(
        'SELECT * FROM especime WHERE nome_popular = ? COLLATE NOCASE', (nome,)
        ).fetchone()
    
    return render_template('especies.html', especie = especie)

