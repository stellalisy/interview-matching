from flask import Blueprint, render_template
from flask import current_app as app



# Blueprint Configuration
auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/', methods=['GET'])
def home():
	"""Homepage"""
	return render_template('home.html',
									 title='Flask Blueprint Demo',
									 subtitle='Demonstration of Flask blueprints in action.',
									 template='home-template')