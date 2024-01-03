import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QComboBox, QMessageBox, QListWidget, QHBoxLayout, QDialog, QFormLayout, QGridLayout, QListWidgetItem, QDateEdit, QFileDialog,  QTableWidgetItem, QTableWidget
from PyQt5.QtCore import pyqtSignal, Qt, QDate
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal, QObject
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class PeriksaKondisi(QWidget):
    kondisi_checked = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        self.init_ui()
        
    def init_ui(self):
        
        form_layout = QFormLayout()
        
        
        
        self.setGeometry(550, 300, 900, 300)
        self.setWindowTitle('Periksa Kondisi Pasien')
        
        label_nama = QLabel('Nama:')
        label_umur = QLabel('Umur:')
        label_alamat = QLabel('Alamat:')
        label_tekanan_darah = QLabel('Tekanan Darah:')
        label_suhu = QLabel('Suhu:')
        label_gejala = QLabel('Gejala:')
        label_gaya_hidup = QLabel('Gaya Hidup:')
        

        self.input_nama = QLineEdit(self)
        self.input_umur = QLineEdit(self)
        self.input_alamat = QLineEdit(self)
        self.input_tekanan_darah = QLineEdit(self)
        self.input_suhu = QLineEdit(self)
        self.input_gejala = QLineEdit(self)
        self.input_gaya_hidup = QLineEdit(self)
        btn_periksa_kondisi = QPushButton('Simpan Kondisi', self)
        btn_periksa_kondisi.clicked.connect(self.periksa_kondisi)
        

        form_layout = QFormLayout()
        form_layout.addRow(label_nama, self.input_nama)
        form_layout.addRow(label_umur, self.input_umur)
        form_layout.addRow(label_alamat, self.input_alamat)
        form_layout.addRow(label_tekanan_darah, self.input_tekanan_darah)
        form_layout.addRow(label_suhu, self.input_suhu)
        form_layout.addRow(label_gejala, self.input_gejala)
        form_layout.addRow(label_gaya_hidup, self.input_gaya_hidup)

        self.pasien_list_periksa_kondisi = QListWidget()
        
        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(self.pasien_list_periksa_kondisi)
        layout.addWidget(btn_periksa_kondisi)
        self.setLayout(layout)


    def periksa_kondisi(self):
        nama = self.input_nama.text()
        umur = self.input_umur.text()
        alamat = self.input_alamat.text()
        tekanan_darah = self.input_tekanan_darah.text()
        suhu = self.input_suhu.text()
        gejala = self.input_gejala.text()
        gaya_hidup = self.input_gaya_hidup.text()

        data = {
            'nama': nama,
            'umur': umur,
            'alamat': alamat,
            'tekanan_darah': tekanan_darah,
            'suhu': suhu,
            'gejala': gejala,
            'gaya_hidup': gaya_hidup
        }

        self.kondisi_checked.emit({'data': data})
        
    def get_conditions_by_name(self, patient_name):
        # Implement the logic to fetch conditions based on the patient's name
        # This is a placeholder; replace it with your actual implementation
        conditions = []
        # Fetch conditions from your data source or perform any necessary operations
        # ...

        return conditions