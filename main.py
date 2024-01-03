import sys
from PyQt5.QtWidgets import QApplication
from parent_widget import ParentWidget

def main():
    app = QApplication(sys.argv)
    parent_widget = ParentWidget()
    parent_widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()