from PyQt4 import QtCore, QtGui
import screen, sys, os

app=QtGui.QApplication(sys.argv)
window=QtGui.QWidget()
ui=screen.Ui_Dialog()
ui.setupUi(window)

QtCore.QObject.connect(ui.pushButton,QtCore.SIGNAL("clicked()"),lambda:test(ui))

def test(ui):
	dir=os.getcwd()+"/screenhot"
	path=dir+"/screenhot.jpg"
	if not os.path.exists(dir):
		os.makedirs(dir)
	QtGui.QPixmap.grabWindow(QtGui.QApplication.desktop().winId()).save(path,'jpg')
	pic=ui.label
	pic.setGeometry(10,10,450,300)
	pic.setPixmap(QtGui.QPixmap(path))
	pic.setScaledContents(True)

window.show()
sys.exit(app.exec_())