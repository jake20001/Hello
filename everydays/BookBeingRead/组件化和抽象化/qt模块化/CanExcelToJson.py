# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : CanExcelToJson
# Author : zhangjk
# CreateTime : 2020/12/16 17:08
# FileName : CanExcelToJson
# Description : 
# --------------------------------
import os
import sys
import traceback

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMessageBox


if getattr(sys, 'frozen', False):
    # we are running in a |PyInstaller| bundle
    scriptspath = sys._MEIPASS
    print("1111 pyinstaller ",scriptspath)
    scriptspath = os.path.dirname(os.path.realpath(sys.executable))
    print("1111---> pyinstaller ",scriptspath)
else:
    # we are running in a normal Python environment
    scriptspath = os.path.dirname(__file__)
    print("1111 Python environment ",scriptspath)

scriptsicon = os.path.join(scriptspath,'icon')
iconpath = os.path.join(scriptsicon,'bean_logo.ico')
resources = os.path.join(scriptspath,'resources')
config = os.path.join(scriptspath,'config')

VERSION = '版本:V1.0.0'
ToolName = 'CAN ExcelToJson'


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 200)
        Form.setWindowIcon(QtGui.QIcon(iconpath))

        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 60, 471, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        # 垂直布局
        self.big_verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        # left，top，right，bottom
        self.big_verticalLayout.setContentsMargins(20, 10, 20, 10)
        self.big_verticalLayout.setObjectName("big_verticalLayout")

        # 水平布局1
        self.horizontalLayout_can_config = QtWidgets.QHBoxLayout()
        self.horizontalLayout_can_config.setObjectName("horizontalLayout_can_config")
        self.label_can_config = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_can_config.setObjectName("CAN配置文件")
        self.label_can_config.setFixedWidth(150)
        self.setFontColor(self.label_can_config)

        # items下拉框
        self.comboBox_can_items = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_can_items.setGeometry(QtCore.QRect(10, 320, 600, 30))
        self.comboBox_can_items.setObjectName("comboBox_can_items")
        self.comboBox_can_items.setFixedWidth(300)
        self.comboBox_can_items.setToolTip("选择要转换CAN配置文件")
        self.comboBox_can_items.setEditable(True)
        self.comboBox_can_items.addItems([])
        self.comboBox_can_items.activated[str].connect(self.choose_can_items)

        # 一个刷新按键
        self.pushButton_refresh_config = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_refresh_config.setGeometry(QtCore.QRect(650, 250, 100, 30))
        self.pushButton_refresh_config.setObjectName("刷新CAN配置文件")
        self.pushButton_refresh_config.setFixedWidth(150)
        self.setFontColor(self.pushButton_refresh_config)
        # 注册
        self.pushButton_refresh_config.clicked.connect(self.refresh_can_config)

        self.horizontalLayout_can_config.addWidget(self.label_can_config)
        self.horizontalLayout_can_config.addWidget(self.comboBox_can_items)
        self.horizontalLayout_can_config.addWidget(self.pushButton_refresh_config)

        # 水平布局2
        self.horizontalLayout_xml_to_excel = QtWidgets.QHBoxLayout()
        self.horizontalLayout_xml_to_excel.setObjectName("horizontalLayout_xml_to_excel")
        self.label_xml_to_excel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_xml_to_excel.setObjectName("CASE统计")
        self.label_xml_to_excel.setFixedWidth(150)
        self.setFontColor(self.label_xml_to_excel)

        # items下拉框
        self.comboBox_items = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_items.setGeometry(QtCore.QRect(10, 320, 600, 30))
        self.comboBox_items.setObjectName("comboBox_items")
        self.comboBox_items.setFixedWidth(300)
        self.comboBox_items.setToolTip("选择要转换Excel")
        self.comboBox_items.setEditable(True)
        self.comboBox_items.addItems([])
        self.comboBox_items.activated[str].connect(self.choose_excel_items)

        # 一个刷新按键
        self.pushButton_refresh_excel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_refresh_excel.setGeometry(QtCore.QRect(650, 250, 100, 30))
        self.pushButton_refresh_excel.setObjectName("刷新")
        self.pushButton_refresh_excel.setFixedWidth(100)
        self.setFontColor(self.pushButton_refresh_excel)
        # 注册
        self.pushButton_refresh_excel.clicked.connect(self.refresh_excel)

        self.pushButton_xml_to_excel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_xml_to_excel.setGeometry(QtCore.QRect(650, 250, 100, 30))
        self.pushButton_xml_to_excel.setObjectName("转换")
        self.setFontColor(self.pushButton_xml_to_excel)
        self.pushButton_xml_to_excel.setFixedWidth(100)
        # 注册
        self.pushButton_xml_to_excel.clicked.connect(self.excel_to_json)

        self.horizontalLayout_xml_to_excel.addWidget(self.label_xml_to_excel)
        self.horizontalLayout_xml_to_excel.addWidget(self.comboBox_items)
        self.horizontalLayout_xml_to_excel.addWidget(self.pushButton_refresh_excel)
        self.horizontalLayout_xml_to_excel.addWidget(self.pushButton_xml_to_excel)

        # End BIG
        self.big_verticalLayout.addLayout(self.horizontalLayout_can_config)
        self.big_verticalLayout.addLayout(self.horizontalLayout_xml_to_excel)

        # 自动填充区域
        Form.setCentralWidget(self.horizontalLayoutWidget)
        # 菜单
        self.myMenu()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 选择list
        self.isSelectedCan = False
        self.mItemSelect = ItemSelect(self.comboBox_can_items,self.isSelectedCan)
        self.isSelectedExcel = False
        self.xItemSelect = ItemSelect(self.comboBox_items,self.isSelectedExcel)

    def myMenu(self):
        # File
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        mHelp = QAction(QIcon('help.png'), '&Help', self)
        mHelp.setShortcut('Ctrl+H')
        mHelp.setStatusTip('Help')
        mHelp.triggered.connect(self.help)
        # Tool

        # statusbar = self.statusBar()
        self.statusbar = QtWidgets.QStatusBar(self)
        # tip
        self.statusbar.showMessage(ToolName + ' Tool developed by JK.Z')
        self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(125,255,125,255);color:black;font-weight:bold;text:xxx;}")
        # statusbar.setObjectName('Flash Tool developed by JK.Z')
        self.setStatusBar(self.statusbar)

        #创建一个菜单栏
        menubar = self.menuBar()
        menubar.setStyleSheet("QMenuBar{padding-left:8px;background:rgba(100,100,100,255);color:black;font-weight:bold;}")
        #添加菜单
        fileMenu = menubar.addMenu('&HELP')
        # toolMenu = menubar.addMenu('&Tool')
        #添加事件
        fileMenu.addAction(exitAction)
        fileMenu.addAction(mHelp)
        self.setMenuBar(menubar)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", ToolName + "工具 " + VERSION))
        self.label_can_config.setText(_translate("Form", "CAN配置文件:"))
        self.label_xml_to_excel.setText(_translate("Form", "Excel to Json:"))
        self.pushButton_refresh_config.setText(_translate("Form", "刷新CAN配置文件"))
        self.pushButton_xml_to_excel.setText(_translate("Form", "转换"))
        self.pushButton_refresh_excel.setText(_translate("Form", "刷新Excels"))


    def setFontColor(self,mObj):
        mObj.setFont(QFont("Microsoft YaHei",10,QFont.Bold))
        if isinstance(mObj,(QtWidgets.QLabel,QMessageBox)):
            mObj.setStyleSheet("color:blue")
        else:
            mObj.setStyleSheet("color:red")

    def excel_to_json(self):
        print('excel_to_json')
        selectedCanItem = self.select_can_item()
        print(selectedCanItem)
        selectedExcelItem = self.select_excel_item()
        print(selectedExcelItem)
        self.pushButton_xml_to_excel.setText("转换中...")
        # self.mExcelToJson = ExcelToJson(scriptspath,selectedCanItem,selectedExcelItem)
        # self.mExcelToJson.finishSignal.connect(self.show_tip)
        # self.mExcelToJson.start()


    # 主要函数入口
    def refresh_can_config(self):
        print('refresh_can_config')
        self.refresh_resource(config,self.comboBox_can_items)

    def refresh_excel(self):
        print("refresh_excel")
        self.refresh_resource(resources,self.comboBox_items)

    def refresh_resource(self,files,comboBox):
        print("refresh_resource")
        # self.tExcels = Excels(files,comboBox)
        # self.tExcels.finishSignal[list].connect(self.refresh)
        # self.tExcels.start()

    def refresh(self,ax):
        self.tExcels.comboBox.clear()
        self.tExcels.comboBox.addItems(ax)

    # new structure
    def choose_can_items(self,text):
        self.mItemSelect.set_text(text)

    def choose_excel_items(self,text):
        self.xItemSelect.set_text(text)

    def select_can_item(self):
        return self.mItemSelect.get_text()

    def select_excel_item(self):
        return self.xItemSelect.get_text()


    # Menu触发
    def help(self):
        try:
            qmsg = QMessageBox(self)
            qmsg.setWindowTitle(VERSION)
            qmsg.setText(ToolName + "工具.\n"
                                    "有任何疑问直接找JK.Z"
                         )
            qmsg.show()
            self.statusbar.showMessage(ToolName + ' Tool developed by JK.Z')
        except Exception as e:
            traceback.print_exc()

    # 通用提示框
    def show_tip(self,text):
        self.pushButton_xml_to_excel.setText('转换')
        self.setFontColor(self.pushButton_xml_to_excel)
        message = QMessageBox(self)
        message.setWindowTitle("Hi~~~")
        message.setText(text)
        self.setFontColor(message)
        message.show()


class MyApp(Ui_Form,QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.setupUi(self)

    # 创建文件夹
    def create_folder(self,new_folder):
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        return new_folder

# 数据结构定义，这里可以把组件模块化：例如加入button
class ItemSelect(object):

    def __init__(self,comboBox,has_selected):
        self.comboBox = comboBox
        self.has_selected = has_selected
        # 扩展button等组件

    def set_text(self,text):
        self.comboBox.text = text
        self.has_selected = True

    def get_text(self):
        if self.has_selected:
            item = self.comboBox.text
        else:
            item = self.comboBox.currentText()
        return item

def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

