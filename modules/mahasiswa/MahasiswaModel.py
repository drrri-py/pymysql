# models/DosenModel.py
from core.coremodel import CoreModel

class MahasiwaModel(CoreModel):
    def __init__(self):
        self.table_name = "Mahasiswa"
        self.table_id = "id"