from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDateEdit, QComboBox, QMessageBox
from PyQt5.QtCore import pyqtSignal, QDate

class HasilPemeriksaanWidget(QDialog):
    kondisi_changed = pyqtSignal()
    hasil_pemeriksaan_saved = pyqtSignal(dict)

    def __init__(self, kondisi_data, kartu_rumah_sakit=None):
        super(HasilPemeriksaanWidget, self).__init__()

        self.kondisi_data = kondisi_data
        self.kartu_rumah_sakit = kartu_rumah_sakit  # Mengakses instance KartuRumahSakit dari parent()

        self.setWindowTitle('Hasil Pemeriksaan')
        self.setGeometry(600, 300, 400, 300)
        self.init_ui()


    def init_ui(self):
        label_nama = QLabel('Nama Pasien: ')
        self.input_nama = QLineEdit(self)

        label_hasil_pemeriksaan = QLabel('Hasil Pemeriksaan:')
        self.input_hasil_pemeriksaan = QLineEdit(self)

        label_obat = QLabel('Obat yang akan diminum:')
        self.input_obat = QLineEdit(self)

        label_tanggal = QLabel('Tanggal Pemeriksaan:')
        self.label_tanggal = QDateEdit(self)
        self.label_tanggal.setDate(QDate.currentDate())

        label_keluhan = QLabel('Keluhan:')
        self.input_keluhan = QLineEdit(self)

        nama_dokter = QLabel('Dokter:')
        self.nama_dokter = QComboBox(self)
        self.nama_dokter.addItems(['Dr. Yasuo, Sp. Jantung', 'Dr. Ahri, Sp. Mata', 'Dr. Riven, Sp. Tulang'])

        btn_simpan_hasil = QPushButton('Simpan Hasil Pemeriksaan', self)
        btn_simpan_hasil.clicked.connect(self.simpan_pemeriksaan)

        layout = QVBoxLayout()
        layout.addWidget(label_nama)
        layout.addWidget(self.input_nama)
        layout.addWidget(label_hasil_pemeriksaan)
        layout.addWidget(self.input_hasil_pemeriksaan)
        layout.addWidget(label_obat)
        layout.addWidget(self.input_obat)
        layout.addWidget(label_tanggal)
        layout.addWidget(self.label_tanggal)
        layout.addWidget(label_keluhan)
        layout.addWidget(self.input_keluhan)
        layout.addWidget(nama_dokter)
        layout.addWidget(self.nama_dokter)
        layout.addWidget(btn_simpan_hasil)

        self.setLayout(layout)

    def simpan_pemeriksaan(self):
        nama_pasien = self.input_nama.text()
        hasil_pemeriksaan = self.input_hasil_pemeriksaan.text()
        obat = self.input_obat.text()
        tanggal = self.label_tanggal.text()
        keluhan = self.input_keluhan.text()
        dokter = self.nama_dokter.currentText()
        

        if not nama_pasien or not hasil_pemeriksaan or not obat or not tanggal or not keluhan or not dokter:
            self.show_dialog("Error", "Harap lengkapi semua kolom.")
            return
        

         # Simpan hasil_pemeriksaan dan obat ke dalam variabel kelas
        self.hasil_pemeriksaan_data = {
            "nama": nama_pasien,
            "hasil_pemeriksaan": hasil_pemeriksaan,
            "obat": obat,
            "tanggal": tanggal,
            "keluhan": keluhan,
            "dokter": dokter
        }
        

        # Simpan hasil_pemeriksaan dan obat ke database
        self.kartu_rumah_sakit.simpan_hasil_pemeriksaan_to_db(nama_pasien, hasil_pemeriksaan, obat, tanggal, keluhan, dokter)

    # Emit sinyal bahwa kondisi telah berubah
        self.kondisi_changed.emit()
        self.hasil_pemeriksaan_saved.emit(self.hasil_pemeriksaan_data)

        # Tutup dialog
        self.accept()
        
        
    def show_dialog(self, title, message):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()