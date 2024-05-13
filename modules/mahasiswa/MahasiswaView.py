from flask import *
from modules.mahasiswa.MahasiswaModel import *

class MahasiswaView:
    
    @staticmethod
    def index():
        data = MahasiwaModel().all()
        return render_template('dosen_index.html', data=data)
    @staticmethod
    def create():
        return render_template('dosen_create.html')

    @staticmethod
    def store():
        mahasiswa_obj = MahasiwaModel()
        post = request.form
        mahasiswa_obj.nidn = post['nim']
        mahasiswa_obj.nama = post['nama']
        MahasiwaModel().store(mahasiswa_obj)
        return redirect('/mahasiswa')
    
    @staticmethod
    def edit(mahasiswa_id):
        obj = MahasiwaModel().find(mahasiswa_id)
        return render_template('mahasiswa_edit.html', obj=obj)
    
    @staticmethod
    def update(mahasiswa_id):
        data = MahasiwaModel().find(mahasiswa_id)
        if data:
            post = request.form
            mahasiswa_obj = MahasiwaModel()
            mahasiswa_obj.nim = post['nim']
            mahasiswa_obj.nama = post['nama']
            MahasiwaModel().update(mahasiswa_id, mahasiswa_obj)
            return redirect('/mahasiswa')
        else:
            return redirect(request.referrer)
        
    @staticmethod
    def delete(mahasiswa_id):
      data = MahasiwaModel().find(mahasiswa_id)
      if data:
          MahasiwaModel().delete(mahasiswa_id)
          return redirect('/mahasiswa')
      else:
          return redirect(request.referrer)