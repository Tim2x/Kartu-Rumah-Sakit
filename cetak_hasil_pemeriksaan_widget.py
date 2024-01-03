from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDate
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class CetakHasilPemeriksaanWidget(QDialog):
    def __init__(self, hasil_pemeriksaan_data, parent=None):
        super(CetakHasilPemeriksaanWidget, self).__init__(parent)

        self.setWindowTitle('Cetak Hasil Pemeriksaan')
        self.setGeometry(600, 300, 400, 300)

        self.hasil_pemeriksaan_data = hasil_pemeriksaan_data
        self.init_ui()

    def init_ui(self):
        label_nama = QLabel(f'Nama Pasien: {self.hasil_pemeriksaan_data["nama"]}')
        label_hasil_pemeriksaan = QLabel(f'Hasil Pemeriksaan: {self.hasil_pemeriksaan_data["hasil_pemeriksaan"]}')
        label_obat = QLabel(f'Obat yang akan diminum: {self.hasil_pemeriksaan_data["obat"]}')
  
        

        btn_cetak = QPushButton('Cetak', self)
        btn_cetak.clicked.connect(self.cetak_hasil_pemeriksaan)

        layout = QVBoxLayout()
        layout.addWidget(label_nama)
        layout.addWidget(label_hasil_pemeriksaan)
        layout.addWidget(label_obat)
       
        layout.addWidget(btn_cetak)

        self.setLayout(layout)

    def cetak_hasil_pemeriksaan(self):
        # Logika untuk mencetak hasil pemeriksaan ke PDF
        pdf_filename = f"hasil_pemeriksaan_{self.hasil_pemeriksaan_data['nama']}.pdf"
        self.generate_pdf(pdf_filename)
        print("Melakukan pencetakan ke PDF...")
        self.accept()
        
    def show_message(self, title, message):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    def generate_pdf(self, filename):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            folder_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf);;All Files (*)", options=options)

            if folder_path:
                full_path = f"{folder_path}.pdf"  # Ensure the extension is added

                c = canvas.Canvas(full_path, pagesize=letter)
                c.setFont("Helvetica", 12)

                c.drawString(100, 750, f'Nama Pasien: {self.hasil_pemeriksaan_data["nama"]}')
                c.drawString(100, 730, f'Hasil Pemeriksaan: {self.hasil_pemeriksaan_data["hasil_pemeriksaan"]}')
                c.drawString(100, 710, f'Obat yang akan diminum: {self.hasil_pemeriksaan_data["obat"]}')

                c.save()
                self.show_message("Pencetakan Berhasil", f"Hasil pemeriksaan telah dicetak ke dalam file PDF: {full_path}")
            else:
                self.show_message("Batal", "Pencetakan dibatalkan.")
        except Exception as e:
            print(f"Error: {e}")
            self.show_message("Error", f"Error saat mencetak ke PDF: {e}")
