import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QMessageBox, QLineEdit, QAbstractItemView
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from window import Ui_MainWindow
from info import get_hardware_info_via_ssh, get_network_info_via_ssh
from network import create_and_save_network_map

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.current_frame = self.ui.frame_input

        self.ui.frame_harware.setVisible(False)
        self.ui.frame_network.setVisible(False)
        self.ui.frame_input.setVisible(True)
        self.ui.frame_network_main.setVisible(False)
        self.ui.frame_ac.setVisible(False)
        self.ui.frame_connected.setVisible(False)
        self.ui.frame_ping.setVisible(False)
        self.ui.frame_graph.setVisible(False)
        
        self.ui.back_btn.setVisible(False)

        self.ui.hardware_btn.clicked.connect(self.hardware_clicked)
        self.ui.network_btn.clicked.connect(self.network_clicked)
        self.ui.back_btn.clicked.connect(self.back_clicked)
        
        self.ui.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    def back_clicked(self):
        if self.current_frame != None:
            if self.current_frame == self.ui.frame_harware:
                self.ui.frame_harware.setVisible(False)
                self.ui.frame_input.setVisible(True)
                self.ui.back_btn.setVisible(False)
            elif self.current_frame == self.ui.frame_network:
                self.ui.frame_network.setVisible(False)
                self.ui.frame_input.setVisible(True)
                self.ui.back_btn.setVisible(False)
            elif self.current_frame == self.ui.frame_input:
                self.ui.back_btn.setVisible(False)
            else:
                self.current_frame.setVisible(False)
                self.current_frame = self.ui.frame_network
                self.ui.frame_network.setVisible(True)
                self.ui.frame_network_main.setVisible(True)
        
    def hardware_add_table(self, info):
        self.current_frame = self.ui.frame_harware
        self.ui.table_hardware.setRowCount(len(info))
        self.ui.table_hardware.setColumnCount(2)
        self.ui.table_hardware.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) 
        
        self.ui.table_hardware.setHorizontalHeaderLabels(["Specification", "Value"])
        
        for row, (key, value) in enumerate(info.items()):
            self.ui.table_hardware.setItem(row, 0, QTableWidgetItem(key))
            self.ui.table_hardware.setItem(row, 1, QTableWidgetItem(str(value)))
        
        header = self.ui.table_hardware.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(0, 250)
        header.resizeSection(1, 750)
        
        self.ui.frame_harware.setVisible(True)

    def hardware_clicked(self):
        self.ui.back_btn.setVisible(True)
        self.current_frame = self.ui.frame_harware
        ip_address = self.ui.ip_address_input.text()
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()

        if ip_address and username and password:
            # print(f"IP Address: {ip_address}, Username: {username}, Password: {password}") 
            try:
                self.ui.frame_input.setVisible(False)
                
                information = get_hardware_info_via_ssh(ip_address, username, password)
                
                self.hardware_add_table(information)
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                QMessageBox.critical(self, "Error", error_message)
        else:
            type_values = f"Please Fill in the Required Fields"
            QMessageBox.critical(self, "Error", type_values)

    def ac_btn_clicked(self,netstat_info):
        self.ui.back_btn.setVisible(True)
        self.current_frame = self.ui.frame_ac
        self.ui.frame_network_main.setVisible(False)
        self.ui.frame_ac.setVisible(True)
        
        self.ui.ac_table.setRowCount(len(netstat_info))
        self.ui.ac_table.setColumnCount(4)
        self.ui.ac_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) 
        
        self.ui.ac_table.setHorizontalHeaderLabels(["Protocol", "Local Address", "Foreign Address", "State"])
        
        for row, val in enumerate(netstat_info):
            self.ui.ac_table.setItem(row, 0, QTableWidgetItem(val[0]))
            self.ui.ac_table.setItem(row, 1, QTableWidgetItem(val[1]))
            self.ui.ac_table.setItem(row, 2, QTableWidgetItem(val[2]))
            if len(val) == 4:
                self.ui.ac_table.setItem(row, 3, QTableWidgetItem(val[3]))
        
        header = self.ui.ac_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(0, 200)
        header.resizeSection(1, 200)
        header.resizeSection(2, 200)
        header.resizeSection(3, 200)

    def connected_btn_clicked(self, arp_info):
        self.ui.back_btn.setVisible(True)
        self.current_frame = self.ui.frame_connected
        self.ui.frame_network_main.setVisible(False)
        self.ui.frame_connected.setVisible(True)

        self.ui.connected_table.setRowCount(len(arp_info))
        self.ui.connected_table.setColumnCount(3)
        self.ui.connected_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) 
        
        self.ui.connected_table.setHorizontalHeaderLabels(["Internet Address", "Physical Address", "Type"])
        
        for row, val in enumerate(arp_info):
            self.ui.connected_table.setItem(row, 0, QTableWidgetItem(val[0]))
            self.ui.connected_table.setItem(row, 1, QTableWidgetItem(val[1]))
            self.ui.connected_table.setItem(row, 2, QTableWidgetItem(val[2]))
        
        header = self.ui.connected_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(0, 200)
        header.resizeSection(1, 200)
        header.resizeSection(2, 200)

    def ping_btn_clicked(self, ping_info):
        self.ui.back_btn.setVisible(True)
        self.current_frame = self.ui.frame_ping
        self.ui.frame_network_main.setVisible(False)
        self.ui.frame_ping.setVisible(True)

        self.ui.text_edit.clear()
        self.ui.text_edit.append(ping_info)

    def graph_btn_clicked(self, ip):
        self.ui.back_btn.setVisible(True)
        self.current_frame = self.ui.frame_graph
        self.ui.frame_network_main.setVisible(False)
        self.ui.frame_graph.setVisible(True)

        self.ui.image_label.setText("Obtaining Graph....")
        self.repaint()
        image_path = create_and_save_network_map(ip)
        if image_path:
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaledToWidth(800)
            self.ui.image_label.setPixmap(pixmap)
        else:
            self.ui.image_label.setText("Failed to generate network graph.")

    def network_add_table(self, wifi_info, netstat_info, arp_info, ping_info,ip):
        self.ui.frame_network.setVisible(True)
        self.ui.frame_network_main.setVisible(True)

        self.ui.wifi_table.setRowCount(len(wifi_info))
        self.ui.wifi_table.setColumnCount(2)
        self.ui.wifi_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) 
        
        self.ui.wifi_table.setHorizontalHeaderLabels(["Specification", "Value"])
        
        for row, (key, value) in enumerate(wifi_info.items()):
            self.ui.wifi_table.setItem(row, 0, QTableWidgetItem(key))
            self.ui.wifi_table.setItem(row, 1, QTableWidgetItem(str(value)))
        
        
        header = self.ui.wifi_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(0, 350)
        header.resizeSection(1, 350)
        
        self.ui.ac_btn.clicked.connect(lambda: self.ac_btn_clicked(netstat_info))
        self.ui.connected_btn.clicked.connect(lambda: self.connected_btn_clicked(arp_info))
        self.ui.ping_btn.clicked.connect(lambda: self.ping_btn_clicked(ping_info))
        self.ui.graph_btn.clicked.connect(lambda: self.graph_btn_clicked(ip))

    def network_clicked(self):
        self.ui.back_btn.setVisible(True)
        self.current_frame = self.ui.frame_network
        ip_address = self.ui.ip_address_input.text()
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()

        if ip_address and username and password:
            # print(f"IP Address: {ip_address}, Username: {username}, Password: {password}") 
            try:
                self.ui.frame_input.setVisible(False)
                
                wifi_info, netstat_info, arp_info, ping_info = get_network_info_via_ssh(ip_address, username, password)
                
                self.network_add_table(wifi_info, netstat_info, arp_info, ping_info,ip_address)
                
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                print(e)
                QMessageBox.critical(self, "Error", error_message)
        else:
            type_values = f"Please Fill in the Required Fields"
            QMessageBox.critical(self, "Error", type_values)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


