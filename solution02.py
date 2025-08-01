# only needed for command line arguments
import sys

# import all the widgets
from PySide6.QtCore import Qt
from PySide6.QtGui import (QCloseEvent, QColor, QImage, QKeySequence,
                           QMouseEvent, QPainter, QPen, QPixmap, QAction)
from PySide6.QtWidgets import (QApplication, QColorDialog, QFileDialog, QLabel,
                               QMainWindow, QMenuBar, QMessageBox,
                               QSlider, QToolBar, QWidget)


class MyPaintArea(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        
        self.setMinimumWidth(640)
        self.setMinimumHeight(480)

        self.image: QImage = QImage(640, 480, QImage.Format.Format_RGB32)
        self.image.fill(QColor(255, 255, 255))

        self.mouse_down: bool = False
        self.last_pos: tuple[int, int] = (0, 0)

        self.pen_size: int = 2
        self.pen_color: QColor = QColor(0, 0, 0)

    def updatePenColor(self, color: QColor):
        self.pen_color = color

    def updatePenSize(self, size: int):
        self.pen_size = size

    def paintEvent(self, event):
        painter: QPainter = QPainter(self)
        painter.drawImage(0, 0, self.image)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_down = True
            x: int = event.position().x()
            y: int = event.position().y()
            self.last_pos = (x, y)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_down = False

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.mouse_down:
            x: int = event.position().x()
            y: int = event.position().y()
            
            painter: QPainter = QPainter(self.image)
            pen: QPen = QPen(self.pen_color, self.pen_size)
            painter.setPen(pen)
            painter.drawLine(self.last_pos[0], self.last_pos[1], x, y)

            self.last_pos = (x, y)
            self.update()


# we define our own window type to build a custom UI
class MyWindow(QMainWindow):
    def quit_app(self):
        self.close()

    def closeEvent(self, ev: QCloseEvent):
        # closing the last (and only) window ends the application
        if QMessageBox.question(
                self, "Please confirm...",
                "Do you really want to close the application?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            ) == QMessageBox.StandardButton.Yes:
            ev.setAccepted(True)
        else:
            ev.setAccepted(False)

    def show_info(self):
        # open a simple dialog window to say hello
        QMessageBox.question(
            self,
            "About Übungsblatt 02 Musterlösung...",
            "Musterlösung von Übungsblatt 02,\n"
            "EIS SoSem 2024\n"
            "Autor: Michael Wand",
            QMessageBox.StandardButton.Ok,
        )

    def open_img(self):
        file_name, selected_filter = QFileDialog.getOpenFileName(
            self, "Open Image", ".", "PNG Files (*.png)"
        )
        if file_name != "":
            self.paintArea.image = QImage(file_name)
            self.update()

    def save_img_as(self):
        file_name, selected_filter = QFileDialog.getSaveFileName(
            self, "Save Image As...", ".", "PNG Files (*.png)"
        )
        if file_name != "":
            self.paintArea.image.save(file_name)

    def show_color_dialog(self):
        color: QColor = QColorDialog.getColor(self.paintArea.pen_color, self)
        if color.isValid():
            self.paintArea.updatePenColor(color)

    def __init__(self, parent):
        # call parent constructor
        super().__init__(parent)

        # set a frame object (empty container) that fills the whole window
        self.paintArea = MyPaintArea(self)

        # a bit of housekeeping...
        self.initMenubar()
        self.initToolbar()

        # make this the content of the main window
        self.setCentralWidget(self.paintArea)

    def initMenubar(self):
        self.file_menu: QMenuBar = self.menuBar().addMenu("&File")

        self.open_action = self.file_menu.addAction("&Open...")
        self.open_action.setShortcut(QKeySequence(Qt.Modifier.CTRL | Qt.Key.Key_O))
        self.open_action.setIcon(QPixmap("imgs/open_32x32.png"))
        self.open_action.triggered.connect(self.open_img)

        self.save_as_action = self.file_menu.addAction("Save &As...")
        self.save_as_action.setShortcut(QKeySequence(Qt.Modifier.CTRL | Qt.Key.Key_S))
        self.save_as_action.setIcon(QPixmap("imgs/saveas_26x26.png"))
        self.save_as_action.triggered.connect(self.save_img_as)

        self.file_menu.addSeparator()

        self.quit_action = self.file_menu.addAction("&Quit...")
        self.quit_action.setShortcut(QKeySequence(Qt.Modifier.CTRL | Qt.Key.Key_Q))
        self.quit_action.setIcon(QPixmap("imgs/quit_26x26.png"))
        self.quit_action.triggered.connect(self.quit_app)

        self.help_menu: QMenuBar = self.menuBar().addMenu("&Help")
        self.info_action = self.help_menu.addAction("&Information...")
        self.info_action.setShortcut(QKeySequence(Qt.Key.Key_F1))
        self.info_action.setIcon(QPixmap("imgs/info_32x32.png"))
        self.info_action.triggered.connect(self.show_info)

    def initToolbar(self):
        self.tools: QToolBar = self.addToolBar("Basic Tools")
        self.tools.addAction(self.open_action)
        self.tools.addAction(self.save_as_action)
        self.tools.addSeparator()
        self.tools.addAction(self.info_action)
        self.tools.addSeparator()
        self.tools.addAction(self.quit_action)
        self.tools.addSeparator()

        # Pen Color
        self.color_btn = QAction(self)
        self.color_btn.setToolTip("Pen Color")
        self.color_btn.setIcon(QPixmap("imgs/colorpicker_32x32.png"))
        self.color_btn.triggered.connect(self.show_color_dialog)
        self.tools.addAction(self.color_btn)
        self.tools.addSeparator()

        # Pen Size
        self.pen_slider: QSlider = QSlider(Qt.Orientation.Horizontal)
        self.pen_slider_label: QLabel = QLabel(f"Pen Size: {self.paintArea.pen_size:>2}")
        self.pen_slider_label.setToolTip("Pen Size")
        self.pen_slider_label.setFixedWidth(65)

        self.pen_slider.setRange(1, 10)
        self.pen_slider.setValue(self.paintArea.pen_size)
        self.pen_slider.setPageStep(1)
        self.pen_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.pen_slider.setTickInterval(1)
        self.pen_slider.setToolTip("Pen Size")
        self.pen_slider.setFixedWidth(200)
        self.pen_slider.valueChanged.connect(self.paintArea.updatePenSize)
        self.pen_slider.valueChanged.connect(
            lambda value: self.pen_slider_label.setText(f"Pen Size: {value:>2}")
        )

        self.tools.addWidget(self.pen_slider_label)
        self.tools.addSeparator()
        self.tools.addWidget(self.pen_slider)
        self.tools.addSeparator()


# our main program starts here, Python-style
if __name__ == "__main__":
    # create an application object (needs cmd-line arguments)
    app: QApplication = QApplication(sys.argv)

    # Create the main window.
    main_window: MyWindow = MyWindow(None)
    main_window.show()

    # Start the event loop.
    # Ends only after closing the main window
    app.exec()
