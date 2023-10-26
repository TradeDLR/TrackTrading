from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
class Window(QMainWindow):
  def __init__(self):
      super().__init__()

      self.setGeometry(300, 600, 600, 300)
      self.setWindowTitle("TradingGUI")
      self.show()

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QLineEdit, QCompleter
#
# app = QApplication(sys.argv)
#
# line_edit = QLineEdit()
# completer = QCompleter(["item1", "item2", "item3"])
# line_edit.setCompleter(completer)
#
# line_edit.show()
# sys.exit(app.exec_())
