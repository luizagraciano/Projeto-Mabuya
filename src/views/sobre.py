from flask import Blueprint, redirect, render_template, request, session, url_for

bp = Blueprint('about', __name__, url_prefix='/about')

@bp.route('/')
def sobre():
    return render_template('sobre.html')