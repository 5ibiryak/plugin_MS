import metashape
from PyQt5 import QtCore, QtGui, QtWidgets
from project import Ui_MainWindow
import sys
from glob import glob
from PyQt5 import sip

# Checking compatibility
# compatible_major_version = "1.7"
# found_major_version = ".".join(Metashape.app.version.split('.')[:2])
# if found_major_version != compatible_major_version:
#     raise Exception("Incompatible Metashape version: {} != {}".format(found_major_version, compatible_major_version))

#кнопка split_by_cameras

#кнопка add_photos
def btn_click():
    name_dir_photo = ui.textEdit.toPlainText()
    files_lst = glob(name_dir_photo+"\**.jpg") 
    chunk = metashape.app.document.addChunck()
    chunk.addPhotos([files_lst])

#выбор папки
def getDirectory():
    dirlist = QtWidgets.QFileDialog.getExistingDirectory()
    ui.textEdit.setPlainText(format(dirlist))




app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


ui.pushButton.clicked.connect(getDirectory)
ui.pushButton_3.clicked.connect(btn_click)
sys.exit(app.exec_())