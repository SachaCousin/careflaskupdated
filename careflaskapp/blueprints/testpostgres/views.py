from flask import Blueprint, render_template



testpostgres = Blueprint('testpostgres', __name__, template_folder='templates')


@testpostgres.route('/letest')
def postgres():
    return render_template('testpostgres1/htmlpostgres.html')



