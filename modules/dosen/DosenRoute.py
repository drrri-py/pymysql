#routes/DosenRoute.py

from flask import *
from modules.dosen.DosenView import *

app_dosen = Blueprint('app_dosen', __name__, template_folder='templates')

app_dosen.add_url_rule('/', 'index', DosenView().index, methods=['GET'])

app_dosen.add_url_rule('/create', 'create', DosenView().create,methods=['GET'])

app_dosen.add_url_rule('/edit/<int:dosen_id>', 'edit', DosenView().edit,methods=['GET'])

app_dosen.add_url_rule('/store', 'store', DosenView().store, methods=['POST'])

app_dosen.add_url_rule('/update/<int:dosen_id>', 'update', DosenView().update,methods=['POST'])

app_dosen.add_url_rule('/delete/<int:dosen_id>', 'delete', DosenView().delete,methods=['GET'])