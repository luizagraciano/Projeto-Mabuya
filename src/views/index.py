from flask import Blueprint, redirect, render_template, request, session, url_for

bp = Blueprint('index', __name__, url_prefix='/index')

@bp.route('/')
def index():
    return render_template('index.html')