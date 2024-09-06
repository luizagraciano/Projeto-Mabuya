from flask import Blueprint, redirect, render_template, request, session, url_for

bp = Blueprint('sobre', __name__, url_prefix='/about')

@bp.route('/')
def sobre():
    return render_template('sobre.html')