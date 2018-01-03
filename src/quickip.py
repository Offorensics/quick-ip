import time
import sys
import subprocess
from PyQt4.QtGui import *

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('IPv4 Quick Change')
w.setGeometry(800, 400, 250, 200)
w.setFixedSize(250, 200)
w.setStyleSheet("background-color: #d1d3d6")
w.setWindowIcon(QIcon('<path_to_your_logo>'))

btn1 = QPushButton('192.168.1.2', w)
btn1.move(0, 0)
btn1.resize(125, 100)
btn1.setStyleSheet('QPushButton {background-color: #02044f; color: white;}')

btn2 = QPushButton('192.168.4.2', w)
btn2.move(0, 100)
btn2.resize(125, 100)
btn2.setStyleSheet('QPushButton {background-color: #000491; color: white;}')

btn3 = QPushButton('192.168.9.2', w)
btn3.move(125, 100)
btn3.resize(125, 100)
btn3.setStyleSheet('QPushButton {background-color: #0409cc; color: white;}')

btn4 = QPushButton('192.168.3.2', w)
btn4.move(125, 0)
btn4.resize(125, 100)
btn4.setStyleSheet("background-color: #2d33ff")
btn4.setStyleSheet('QPushButton {background-color: #2d33ff; color: white;}')
 
def on_click(interface, addr):
	net_set_f = "/etc/network/interfaces"
	
	new_settings = ("# interfaces(5) file used by ifup(8) and ifdown(8)\n"
			"auto lo\n"
			"iface lo inet loopback\n\n"
			"auto " + interface + "\n"
			"iface " + interface + " inet static\n\n"
			"address " + addr + "\n"
			"netmask 255.255.255.0\n")
      
	with open(net_set_f, "w") as f:
		f.write(new_settings)

	cmd = "sudo ifdown " + interface + " && sudo ifup " + interface + " 1>/dev/null &2>1"
	subprocess.Popen([cmd], shell=True)
	w.close()

with open("quickip.cfg") as quick:
	interface = quick.read().strip()
 
btn1.clicked.connect(lambda: on_click(interface, "192.168.1.2"))
btn2.clicked.connect(lambda: on_click(interface, "192.168.4.2"))
btn3.clicked.connect(lambda: on_click(interface, "192.168.9.2"))
btn4.clicked.connect(lambda: on_click(interface, "192.168.3.2")) 

w.show()
app.exec_()
