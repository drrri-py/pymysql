#app.py
from flask import Flask
from modules.dosen.DosenRoute import app_dosen
from modules.mahasiswa.MahasiswaRoute import app_mahasiswa

app = Flask(__name__)

app.register_blueprint(app_dosen, url_prefix='/dosen')
app.register_blueprint(app_mahasiswa, url_prefix='/mahasiswa')

if __name__=='__main__':
    app.run(debug=True)