from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1113, 800)
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
#######################################################################################
        self.back_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(10, 10, 75, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
#######################################################################################
        self.frame_input = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_input.setGeometry(QtCore.QRect(190, 70, 761, 531))
        self.frame_input.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_input.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_input.setObjectName("frame_input")
#######################################################################################        
        self.hardware_btn = QtWidgets.QPushButton(parent=self.frame_input)
        self.hardware_btn.setGeometry(QtCore.QRect(180, 470, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.hardware_btn.setFont(font)
        self.hardware_btn.setObjectName("hardware_btn")
        
        self.network_btn = QtWidgets.QPushButton(parent=self.frame_input)
        self.network_btn.setGeometry(QtCore.QRect(370, 470, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.network_btn.setFont(font)
        self.network_btn.setObjectName("network_btn")
        
        self.password_label = QtWidgets.QLabel(parent=self.frame_input)
        self.password_label.setGeometry(QtCore.QRect(110, 370, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        
        self.password_input = QtWidgets.QLineEdit(parent=self.frame_input)
        self.password_input.setGeometry(QtCore.QRect(360, 370, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.password_input.setFont(font)
        self.password_input.setObjectName("password_input")
        
        self.username_input = QtWidgets.QLineEdit(parent=self.frame_input)
        self.username_input.setGeometry(QtCore.QRect(360, 290, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.username_input.setFont(font)
        self.username_input.setObjectName("username_input")
        
        self.username_label = QtWidgets.QLabel(parent=self.frame_input)
        self.username_label.setGeometry(QtCore.QRect(100, 290, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        
        self.ip_label = QtWidgets.QLabel(parent=self.frame_input)
        self.ip_label.setGeometry(QtCore.QRect(90, 200, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        
        self.ip_address_input = QtWidgets.QLineEdit(parent=self.frame_input)
        self.ip_address_input.setGeometry(QtCore.QRect(360, 200, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ip_address_input.setFont(font)
        self.ip_address_input.setObjectName("ip_address_input")
        
        self.heading = QtWidgets.QLabel(parent=self.frame_input)
        self.heading.setGeometry(QtCore.QRect(150, 10, 521, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(43)
        self.heading.setFont(font)
        self.heading.setObjectName("heading")
###############################################################################################        
        self.frame_harware = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_harware.setGeometry(QtCore.QRect(30, 60, 1071, 721))
        self.frame_harware.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_harware.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_harware.setObjectName("frame_harware")
###############################################################################################        
        self.heading_hardware = QtWidgets.QLabel(parent=self.frame_harware)
        self.heading_hardware.setGeometry(QtCore.QRect(160, 10, 771, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(43)
        self.heading_hardware.setFont(font)
        self.heading_hardware.setObjectName("heading_hardware")
        
        self.table_hardware = QtWidgets.QTableWidget(parent=self.frame_harware)
        self.table_hardware.setGeometry(QtCore.QRect(20, 80, 1041, 621))
        self.table_hardware.setObjectName("table_hardware")
        self.table_hardware.setColumnCount(0)
        self.table_hardware.setRowCount(0)
###############################################################################################        
        self.frame_network = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_network.setGeometry(QtCore.QRect(30, 60, 1071, 721))
        self.frame_network.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_network.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_network.setObjectName("frame_network")
###############################################################################################       
        self.heading_network = QtWidgets.QLabel(parent=self.frame_network)
        self.heading_network.setGeometry(QtCore.QRect(160, 10, 771, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(43)
        self.heading_network.setFont(font)
        self.heading_network.setObjectName("heading_network")
###############################################################################################        
        self.frame_network_main = QtWidgets.QFrame(parent=self.frame_network)
        self.frame_network_main.setGeometry(QtCore.QRect(120, 160, 821, 491))
        self.frame_network_main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_network_main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_network_main.setObjectName("frame_network_main")
###############################################################################################       
        self.wifi_label = QtWidgets.QLabel(parent=self.frame_network_main)
        self.wifi_label.setGeometry(QtCore.QRect(220, 20, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.wifi_label.setFont(font)
        self.wifi_label.setObjectName("wifi_label")
        
        self.wifi_table = QtWidgets.QTableWidget(parent=self.frame_network_main)
        self.wifi_table.setGeometry(QtCore.QRect(30, 90, 771, 300))
        self.wifi_table.setRowCount(3)
        self.wifi_table.setColumnCount(2)
        self.wifi_table.setObjectName("wifi_table")
        self.wifi_table.horizontalHeader().setDefaultSectionSize(375)
        
        self.ac_btn = QtWidgets.QPushButton(parent=self.frame_network_main)
        self.ac_btn.setGeometry(QtCore.QRect(110, 420, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ac_btn.setFont(font)
        self.ac_btn.setObjectName("ac_btn")
        
        self.connected_btn = QtWidgets.QPushButton(parent=self.frame_network_main)
        self.connected_btn.setGeometry(QtCore.QRect(320, 420, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.connected_btn.setFont(font)
        self.connected_btn.setObjectName("connected_btn")
        
        self.ping_btn = QtWidgets.QPushButton(parent=self.frame_network_main)
        self.ping_btn.setGeometry(QtCore.QRect(590, 420, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ping_btn.setFont(font)
        self.ping_btn.setObjectName("ping_btn")

        self.graph_btn = QtWidgets.QPushButton(parent=self.frame_network_main)
        self.graph_btn.setGeometry(QtCore.QRect(320, 460, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.graph_btn.setFont(font)
        self.graph_btn.setObjectName("graph_btn")
##############################################################################################
        self.frame_ac = QtWidgets.QFrame(parent=self.frame_network)
        self.frame_ac.setGeometry(QtCore.QRect(90, 90, 861, 591))
        self.frame_ac.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_ac.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_ac.setObjectName("frame_ac")
##############################################################################################
        self.ac_table = QtWidgets.QTableWidget(parent=self.frame_ac)
        self.ac_table.setGeometry(QtCore.QRect(30, 20, 800, 561))
        self.ac_table.setObjectName("ac_table")
        self.ac_table.setColumnCount(0)
        self.ac_table.setRowCount(0)
##############################################################################################
        self.frame_connected = QtWidgets.QFrame(parent=self.frame_network)
        self.frame_connected.setGeometry(QtCore.QRect(90, 90, 861, 591))
        self.frame_connected.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_connected.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_connected.setObjectName("frame_connected")

        self.connected_table = QtWidgets.QTableWidget(parent=self.frame_connected)
        self.connected_table.setGeometry(QtCore.QRect(30, 20, 800, 561))
        self.connected_table.setObjectName("connected_table")
        self.connected_table.setColumnCount(0)
        self.connected_table.setRowCount(0)
##############################################################################################
        self.frame_ping = QtWidgets.QFrame(parent=self.frame_network)
        self.frame_ping.setGeometry(QtCore.QRect(90, 90, 861, 591))
        self.frame_ping.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_ping.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_ping.setObjectName("frame_ping")

        self.text_edit = QtWidgets.QTextEdit(self.frame_ping)
        self.text_edit.setGeometry(QtCore.QRect(30, 20, 800, 561))
        self.text_edit.setObjectName("text_edit")
#############################################################################################
        self.frame_graph = QtWidgets.QFrame(parent=self.frame_network)
        self.frame_graph.setGeometry(QtCore.QRect(90, 90, 861, 591))
        self.frame_graph.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_graph.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_graph.setObjectName("frame_graph")

        self.image_label = QtWidgets.QLabel(parent=self.frame_graph)
        self.image_label.setGeometry(QtCore.QRect(120, 70, 800, 561))
        self.image_label.setObjectName("image_label")

#############################################################################################
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Remote Information"))
        self.heading.setText(_translate("MainWindow", "Remote Information"))
        self.ip_address_input.setText(_translate("MainWindow", "192.168.0.176"))
        self.ip_label.setText(_translate("MainWindow", "Ip Address :"))
        self.username_input.setText(_translate("MainWindow", "Other"))
        self.username_label.setText(_translate("MainWindow", "Username :"))
        self.password_input.setText(_translate("MainWindow", "qwerty"))
        self.password_label.setText(_translate("MainWindow", "Password :"))
        self.hardware_btn.setText(_translate("MainWindow", "Hardware Info"))
        self.back_btn.setText(_translate("MainWindow", "Back"))
        self.network_btn.setText(_translate("MainWindow", "Network Info"))
        self.heading_hardware.setText(_translate("MainWindow", "Remote Hardware Information"))
        self.heading_network.setText(_translate("MainWindow", "Remote Network Information"))
        self.wifi_label.setText(_translate("MainWindow", "Wireless LAN adapter Wi-Fi"))
        self.ac_btn.setText(_translate("MainWindow", "Active Connections"))
        self.connected_btn.setText(_translate("MainWindow", "List Connected Devices"))
        self.graph_btn.setText(_translate("MainWindow", "Show Network"))
        self.ping_btn.setText(_translate("MainWindow", "Ping Check"))