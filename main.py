from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy
from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide Fourier Series SVG Viewer")
        self.resize(800, 600)

        # --- Top bar with button and label ---
        self.label = QLabel("Press the test button.")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("Test Button")

        top_layout = QHBoxLayout()           # horizontal layout for top bar
        top_layout.addWidget(self.button)
        top_layout.addWidget(self.label)

        top_widget = QWidget()               # container for top bar
        top_widget.setLayout(top_layout)

        # --- Canvas area ---
        self.canvas_area = CanvasWindow()
        # Make the canvas expand to take remaining space
        self.canvas_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # --- Main layout ---
        main_layout = QVBoxLayout()
        main_layout.addWidget(top_widget)    # top bar stays at the top
        main_layout.addWidget(self.canvas_area)  # canvas fills the rest
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)

        self.setLayout(main_layout)

        # --- Signals ---
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        self.label.setText("Button pressed!")
        # Note: trigger a canvas redraw
        self.canvas_area.update()

class CanvasWindow(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.GlobalColor.white, 1)
        painter.setPen(pen)

        width = self.width()
        height = self.height()
        horizontal_center = int(width / 2)
        vertical_center = int(height / 2)
        padding = 25

        # Draw a line that scales with widget size
        painter.drawLine(horizontal_center, padding, horizontal_center, height - padding)
        painter.drawLine(padding, vertical_center, width - padding, vertical_center)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
