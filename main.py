from PySide6.QtWidgets import QApplication, QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle("Fourier Series App")
window.resize(400, 300)
window.show()

app.exec()
