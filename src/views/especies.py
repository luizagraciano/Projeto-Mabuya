from flask import Blueprint, redirect, render_template, request, session, url_for
from src.data.db import get_db

#Cria a blueprint do módulo de avistamentos
bp = Blueprint('especies', __name__, url_prefix='/especies')

@bp.route('/')
def especies():
    return render_template('especies.html')