# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_neos(object):
    def setupUi(self, neos):
        neos.setObjectName("neos")
        neos.resize(807, 600)
        font = QtGui.QFont()
        font.setPointSize(10)
        neos.setFont(font)
        neos.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        neos.setMouseTracking(False)
        neos.setStyleSheet("QMainWindow {\n"
"    background-color: #C9DFF1;\n"
"}\n"
"QCalendar {\n"
"    background-color: ;\n"
"}\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #C1BBA8;\n"
"    background-color: #F0F4F3;\n"
"    color: black;\n"
"}\n"
"QPlainTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #C1BBA8;\n"
"    background-color: #F0F4F3;\n"
"    color: black;\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-color: #EFE7CC;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black ;\n"
"    padding: 2px;\n"
"    background-color: #C9DFF1;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-color: #EFE7CC;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    padding: 2px;\n"
"    background-color: #C9DFF1;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-color: #EFE7CC;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    padding: 2px;\n"
"    background-color: #C1BBA8;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-color: #EFE7CC;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    padding: 2px;\n"
"    background-color: #C1BBA8;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #C1BBA8;\n"
"    background-color: #F0F4F3;\n"
"    color: black;\n"
"}\n"
"QLabel {\n"
"    color: black;\n"
"}\n"
"QLCDNumber {\n"
"    color: #C1BBA8;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"    border-color: transparent;\n"
"    border-style: solid;\n"
"    background-color: #C1BBA8;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #EFE7CC;\n"
"    border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: #C9DFF1;\n"
"}\n"
"QMenuBar::item {\n"
"    color: bl;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"    background-color: #C9DFF1;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background-color: #EFBFA8;\n"
"    color: black;\n"
"}\n"
"QMenu {\n"
"    background-color: #C9DFF1;\n"
"}\n"
"QMenu::item:selected {\n"
"    background-color: #EFE7CC;\n"
"    color: black;\n"
"}\n"
"QMenu::item {\n"
"    color: black;\n"
"    background-color: #C9DFF1;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:  #C1BBA8;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: #EFE7CC;\n"
"        background-color: #EFBFA8;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"}\n"
"QTabBar::tab:first {\n"
"    border-style: solid;\n"
"    border-left-width:1px;\n"
"    border-right-width:0px;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:0px;\n"
"    border-top-color: #EFE7CC;\n"
"    border-left-color: #EFE7CC;\n"
"    border-bottom-color: #EFE7CC;\n"
"    border-top-left-radius: 4px;\n"
"    color: black;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color : #C9DFF1;\n"
"}\n"
"QTabBar::tab:last {\n"
"    border-style: solid;\n"
"    border-top-width:1px;\n"
"    border-left-width:1px;\n"
"    border-right-width:1px;\n"
"    border-bottom-width:0px;\n"
"    border-color: #EFE7CC;\n"
"    border-top-right-radius: 4px;\n"
"    color: black;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: #C9DFF1;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:0px;\n"
"    border-left-width:1px;\n"
"    border-top-color: #EFE7CC;\n"
"    border-left-color: #EFE7CC;\n"
"    border-bottom-color: #EFE7CC;\n"
"    color: black;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: #C9DFF1;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-left-width:1px;\n"
"    border-bottom-width:0px;\n"
"    border-right-color: transparent;\n"
"    border-top-color: #EFE7CC;\n"
"    border-left-color: #EFE7CC;\n"
"    border-bottom-color: #EFE7CC;\n"
"    color:black;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: #F0F4F3;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-left-width:1px;\n"
"      border-bottom-width:0px;\n"
"      border-top-width:1px;\n"
"    border-right-color: transparent;\n"
"    border-top-color: #EFE7CC;\n"
"    border-left-color: #EFE7CC;\n"
"    border-bottom-color: #EFE7CC;\n"
"    color: black;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: #F0F4F3;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: black;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #EFBFA8;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #C1BBA8;\n"
"    color: #EFE7CC;\n"
"    background-color: qradialgradient(cx:0.4, cy:0.4, radius: 1.5,fx:0, fy:0, stop:0 #EFE7CC, stop:0.3 #EFE7CC, stop:0.4 #C1BBA8, stop:0.5 #EFE7CC, stop:1 #EFE7CC);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #C1BBA8;\n"
"    color: #EFE7CC;\n"
"}\n"
"QRadioButton {\n"
"    color: black;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"    color: black;\n"
"    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.4,fx:0.5, fy:0.5, stop:0 #C1BBA8, stop:1 #EFE7CC);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #C1BBA8;\n"
"    color : #EFBFA8;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color: #C1BBA8;\n"
"}\n"
"QSpinBox {\n"
"    color: black;\n"
"    background-color: #F0F4F3;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #C1BBA8;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color: black;\n"
"    background-color: #F0F4F3;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #C1BBA8;\n"
"}\n"
"QTimeEdit {\n"
"    color: black;\n"
"    background-color: #F0F4F3;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #C1BBA8;\n"
"}\n"
"QDateTimeEdit {\n"
"    color: black;\n"
"    background-color: #F0F4F3;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #C1BBA8;\n"
"}\n"
"QDateEdit {\n"
"    color: black;\n"
"    background-color: #F0F4F3;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #C1BBA8;\n"
"}\n"
"QFontComboBox {\n"
"    color: black;\n"
"    background-color: #F0F4F3;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #C1BBA8;\n"
"}\n"
"QComboBox {\n"
"    color: black;\n"
"    background-color: #F0F4F3;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #C1BBA8;\n"
"}\n"
"\n"
"QDial {\n"
"    background: #C1BBA8;\n"
"}\n"
"\n"
"QToolBox {\n"
"    color: black;\n"
"    background-color: #F0F4F3;\n"
"}\n"
"QToolBox::tab {\n"
"    color: black;\n"
"    background-color: #F0F4F3;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #F0F4F3;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color: #F0F4F3;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background-color: #EFE7CC;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background-color: #EFE7CC;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #EFBFA8;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: #EFBFA8;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: #EFBFA8;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: #EFBFA8;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #EFE7CC;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: #EFE7CC;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 10px;\n"
"    border: 1px transparent #C1BBA8;\n"
"    margin: 0px 20px 0px 20px;\n"
"    background: transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
"    max-width: 10px;\n"
"    border: 1px transparent #C1BBA8;\n"
"    margin: 20px 0px 20px 0px;\n"
"    background: transparent;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #EFBFA8;\n"
"    border-style: transparent;\n"
"    border-radius: 4px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #F0F4F3;\n"
"    border-style: transparent;\n"
"    border-radius: 4px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #EFBFA8;\n"
"    border-style: transparent;\n"
"    border-radius: 4px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #F0F4F3;\n"
"    border-style: transparent;\n"
"    border-radius: 4px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: #15433a;\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: #15433a;\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-bottom-left-radius: 4px;\n"
"   background: #15433a;\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-bottom-left-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-top-right-radius: 4px;\n"
"   background: #15433a;\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-top-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"   background: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(neos)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 789, 542))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.formLayoutWidget = QtWidgets.QWidget(self.page)
        self.formLayoutWidget.setGeometry(QtCore.QRect(200, 150, 281, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(6, 6, 6, 6)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.kullanici_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kullanici_edit.setFont(font)
        self.kullanici_edit.setObjectName("kullanici_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.kullanici_edit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.sifre_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sifre_edit.setFont(font)
        self.sifre_edit.setObjectName("sifre_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sifre_edit)
        self.giris_buton = QtWidgets.QPushButton(self.page)
        self.giris_buton.setGeometry(QtCore.QRect(310, 310, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.giris_buton.setFont(font)
        self.giris_buton.setObjectName("giris_buton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 401, 241))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(6, 6, 6, 6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2021, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.not_adress_kayit = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.not_adress_kayit.setFont(font)
        self.not_adress_kayit.setObjectName("not_adress_kayit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.not_adress_kayit)
        self.kayit_et = QtWidgets.QPushButton(self.page_2)
        self.kayit_et.setGeometry(QtCore.QRect(130, 310, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.kayit_et.setFont(font)
        self.kayit_et.setObjectName("kayit_et")
        self.comboBox_5 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_5.setGeometry(QtCore.QRect(480, 110, 151, 21))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.listWidget_3 = QtWidgets.QListWidget(self.page_2)
        self.listWidget_3.setGeometry(QtCore.QRect(440, 180, 256, 192))
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.cikar = QtWidgets.QPushButton(self.page_2)
        self.cikar.setGeometry(QtCore.QRect(710, 200, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.cikar.setFont(font)
        self.cikar.setObjectName("cikar")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.page_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(50, 20, 381, 201))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.adi_soyadi = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.adi_soyadi.setObjectName("adi_soyadi")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.adi_soyadi)
        self.kayit_tarihi = QtWidgets.QDateEdit(self.formLayoutWidget_3)
        self.kayit_tarihi.setCalendarPopup(True)
        self.kayit_tarihi.setDate(QtCore.QDate(2021, 1, 1))
        self.kayit_tarihi.setObjectName("kayit_tarihi")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kayit_tarihi)
        self.telefon = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.telefon.setObjectName("telefon")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.telefon)
        self.mail_adrsi = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.mail_adrsi.setObjectName("mail_adrsi")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.mail_adrsi)
        self.not_arasi = QtWidgets.QTextEdit(self.formLayoutWidget_3)
        self.not_arasi.setObjectName("not_arasi")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.not_arasi)
        self.tableWidget = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget.setGeometry(QtCore.QRect(20, 260, 731, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(520, 60, 81, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.guncelle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.guncelle.setFont(font)
        self.guncelle.setObjectName("guncelle")
        self.verticalLayout.addWidget(self.guncelle)
        self.silme = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.silme.setFont(font)
        self.silme.setObjectName("silme")
        self.verticalLayout.addWidget(self.silme)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.comboBox = QtWidgets.QComboBox(self.page_4)
        self.comboBox.setGeometry(QtCore.QRect(250, 40, 181, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_13 = QtWidgets.QLabel(self.page_4)
        self.label_13.setGeometry(QtCore.QRect(340, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.page_4)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(390, 90, 301, 81))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.ogrenci_adi = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ogrenci_adi.setFont(font)
        self.ogrenci_adi.setObjectName("ogrenci_adi")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ogrenci_adi)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_18)
        self.label_19 = QtWidgets.QLabel(self.page_4)
        self.label_19.setGeometry(QtCore.QRect(460, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.page_4)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(390, 180, 301, 41))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.ucret = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ucret.setFont(font)
        self.ucret.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ucret.setInputMethodHints(QtCore.Qt.ImhNoTextHandles|QtCore.Qt.ImhPreferLowercase|QtCore.Qt.ImhPreferNumbers)
        self.ucret.setObjectName("ucret")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ucret)
        self.kayit_et_sinif = QtWidgets.QPushButton(self.page_4)
        self.kayit_et_sinif.setGeometry(QtCore.QRect(440, 470, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kayit_et_sinif.setFont(font)
        self.kayit_et_sinif.setObjectName("kayit_et_sinif")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_4)
        self.comboBox_2.setGeometry(QtCore.QRect(330, 240, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_4)
        self.stackedWidget_2.setGeometry(QtCore.QRect(440, 240, 311, 81))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_28 = QtWidgets.QLabel(self.page_10)
        self.label_28.setGeometry(QtCore.QRect(50, 30, 131, 16))
        self.label_28.setObjectName("label_28")
        self.stackedWidget_2.addWidget(self.page_10)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.formLayoutWidget_7 = QtWidgets.QWidget(self.page_12)
        self.formLayoutWidget_7.setGeometry(QtCore.QRect(20, 10, 160, 80))
        self.formLayoutWidget_7.setObjectName("formLayoutWidget_7")
        self.formLayout_7 = QtWidgets.QFormLayout(self.formLayoutWidget_7)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_23 = QtWidgets.QLabel(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.pesin = QtWidgets.QLineEdit(self.formLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pesin.setFont(font)
        self.pesin.setObjectName("pesin")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pesin)
        self.stackedWidget_2.addWidget(self.page_12)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.formLayoutWidget_8 = QtWidgets.QWidget(self.page_11)
        self.formLayoutWidget_8.setGeometry(QtCore.QRect(10, 0, 271, 80))
        self.formLayoutWidget_8.setObjectName("formLayoutWidget_8")
        self.formLayout_8 = QtWidgets.QFormLayout(self.formLayoutWidget_8)
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.onodeme = QtWidgets.QLineEdit(self.formLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.onodeme.setFont(font)
        self.onodeme.setObjectName("onodeme")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.onodeme)
        self.stackedWidget_2.addWidget(self.page_11)
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.page_4)
        self.stackedWidget_3.setGeometry(QtCore.QRect(30, 330, 321, 201))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.stackedWidget_3.addWidget(self.page_14)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.stackedWidget_3.addWidget(self.page_15)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.taksit_combo = QtWidgets.QComboBox(self.page_13)
        self.taksit_combo.setGeometry(QtCore.QRect(10, 20, 69, 22))
        self.taksit_combo.setObjectName("taksit_combo")
        self.taksit_combo.addItem("")
        self.taksit_combo.addItem("")
        self.taksit_combo.addItem("")
        self.taksit_combo.addItem("")
        self.taksitler = QtWidgets.QStackedWidget(self.page_13)
        self.taksitler.setGeometry(QtCore.QRect(110, 0, 211, 201))
        self.taksitler.setObjectName("taksitler")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_22 = QtWidgets.QLabel(self.page_8)
        self.label_22.setGeometry(QtCore.QRect(50, 30, 91, 21))
        self.label_22.setObjectName("label_22")
        self.taksitler.addWidget(self.page_8)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.ilk_taksit = QtWidgets.QLineEdit(self.page_5)
        self.ilk_taksit.setGeometry(QtCore.QRect(20, 20, 113, 20))
        self.ilk_taksit.setObjectName("ilk_taksit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.page_5)
        self.dateEdit_2.setGeometry(QtCore.QRect(20, 50, 110, 22))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QtCore.QDate(2021, 1, 1))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.taksitler.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.ilk_taksitt = QtWidgets.QLineEdit(self.page_6)
        self.ilk_taksitt.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.ilk_taksitt.setObjectName("ilk_taksitt")
        self.ilk_taksit_tarih = QtWidgets.QDateEdit(self.page_6)
        self.ilk_taksit_tarih.setGeometry(QtCore.QRect(10, 40, 111, 22))
        self.ilk_taksit_tarih.setCalendarPopup(True)
        self.ilk_taksit_tarih.setDate(QtCore.QDate(2021, 1, 1))
        self.ilk_taksit_tarih.setObjectName("ilk_taksit_tarih")
        self.ilk_taksitt_2 = QtWidgets.QLineEdit(self.page_6)
        self.ilk_taksitt_2.setGeometry(QtCore.QRect(10, 70, 113, 20))
        self.ilk_taksitt_2.setObjectName("ilk_taksitt_2")
        self.ikinci_taksit_tarih = QtWidgets.QDateEdit(self.page_6)
        self.ikinci_taksit_tarih.setGeometry(QtCore.QRect(10, 100, 111, 22))
        self.ikinci_taksit_tarih.setCalendarPopup(True)
        self.ikinci_taksit_tarih.setDate(QtCore.QDate(2021, 1, 1))
        self.ikinci_taksit_tarih.setObjectName("ikinci_taksit_tarih")
        self.taksitler.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.taksit_3_ilk = QtWidgets.QLineEdit(self.page_7)
        self.taksit_3_ilk.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.taksit_3_ilk.setObjectName("taksit_3_ilk")
        self.ilk_3_taksit = QtWidgets.QDateEdit(self.page_7)
        self.ilk_3_taksit.setGeometry(QtCore.QRect(10, 40, 111, 22))
        self.ilk_3_taksit.setCalendarPopup(True)
        self.ilk_3_taksit.setDate(QtCore.QDate(2021, 1, 1))
        self.ilk_3_taksit.setObjectName("ilk_3_taksit")
        self.ilk_3_taksit_2 = QtWidgets.QDateEdit(self.page_7)
        self.ilk_3_taksit_2.setGeometry(QtCore.QRect(10, 100, 111, 22))
        self.ilk_3_taksit_2.setCalendarPopup(True)
        self.ilk_3_taksit_2.setDate(QtCore.QDate(2021, 1, 1))
        self.ilk_3_taksit_2.setObjectName("ilk_3_taksit_2")
        self.taksit_3_ilk_2 = QtWidgets.QLineEdit(self.page_7)
        self.taksit_3_ilk_2.setGeometry(QtCore.QRect(10, 70, 113, 20))
        self.taksit_3_ilk_2.setObjectName("taksit_3_ilk_2")
        self.taksit_3_ilk_3 = QtWidgets.QLineEdit(self.page_7)
        self.taksit_3_ilk_3.setGeometry(QtCore.QRect(10, 130, 113, 20))
        self.taksit_3_ilk_3.setObjectName("taksit_3_ilk_3")
        self.ilk_3_taksit_3 = QtWidgets.QDateEdit(self.page_7)
        self.ilk_3_taksit_3.setGeometry(QtCore.QRect(10, 160, 111, 22))
        self.ilk_3_taksit_3.setCalendarPopup(True)
        self.ilk_3_taksit_3.setDate(QtCore.QDate(2021, 1, 1))
        self.ilk_3_taksit_3.setObjectName("ilk_3_taksit_3")
        self.taksitler.addWidget(self.page_7)
        self.stackedWidget_3.addWidget(self.page_13)
        self.checkBox = QtWidgets.QCheckBox(self.page_4)
        self.checkBox.setGeometry(QtCore.QRect(400, 350, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.page_4)
        self.checkBox_2.setGeometry(QtCore.QRect(500, 350, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.page_4)
        self.checkBox_3.setGeometry(QtCore.QRect(590, 350, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.page_4)
        self.listWidget_2.setGeometry(QtCore.QRect(170, 120, 152, 191))
        self.listWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget_2.setMovement(QtWidgets.QListView.Free)
        self.listWidget_2.setUniformItemSizes(False)
        self.listWidget_2.setWordWrap(False)
        self.listWidget_2.setSelectionRectVisible(False)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.listWidget = QtWidgets.QListWidget(self.page_4)
        self.listWidget.setGeometry(QtCore.QRect(10, 120, 151, 191))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 191, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_33 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout.addWidget(self.label_33)
        self.ogrenci_adi_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.ogrenci_adi_2.setObjectName("ogrenci_adi_2")
        self.horizontalLayout.addWidget(self.ogrenci_adi_2)
        self.bul = QtWidgets.QPushButton(self.page_4)
        self.bul.setGeometry(QtCore.QRect(60, 60, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bul.setFont(font)
        self.bul.setObjectName("bul")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.page_4)
        self.dateEdit_3.setGeometry(QtCore.QRect(500, 400, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setDate(QtCore.QDate(2021, 1, 1))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.stackedWidget.addWidget(self.page_4)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.formLayoutWidget_6 = QtWidgets.QWidget(self.page_9)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(220, 40, 281, 191))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setContentsMargins(6, 6, 6, 6)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_24 = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.sinif_adi = QtWidgets.QLineEdit(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sinif_adi.setFont(font)
        self.sinif_adi.setObjectName("sinif_adi")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sinif_adi)
        self.label_25 = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.egitim_tutari = QtWidgets.QLineEdit(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.egitim_tutari.setFont(font)
        self.egitim_tutari.setObjectName("egitim_tutari")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.egitim_tutari)
        self.label_26 = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.egitim_tarihi = QtWidgets.QDateEdit(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.egitim_tarihi.setFont(font)
        self.egitim_tarihi.setCalendarPopup(True)
        self.egitim_tarihi.setDate(QtCore.QDate(2021, 1, 1))
        self.egitim_tarihi.setObjectName("egitim_tarihi")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.egitim_tarihi)
        self.label_27 = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.egitim_bitis_tarihi = QtWidgets.QDateEdit(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.egitim_bitis_tarihi.setFont(font)
        self.egitim_bitis_tarihi.setCalendarPopup(True)
        self.egitim_bitis_tarihi.setDate(QtCore.QDate(2021, 1, 1))
        self.egitim_bitis_tarihi.setObjectName("egitim_bitis_tarihi")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.egitim_bitis_tarihi)
        self.egitim_kaydet = QtWidgets.QPushButton(self.page_9)
        self.egitim_kaydet.setGeometry(QtCore.QRect(310, 260, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.egitim_kaydet.setFont(font)
        self.egitim_kaydet.setObjectName("egitim_kaydet")
        self.stackedWidget.addWidget(self.page_9)
        self.page_17 = QtWidgets.QWidget()
        self.page_17.setObjectName("page_17")
        self.comboBox_3 = QtWidgets.QComboBox(self.page_17)
        self.comboBox_3.setGeometry(QtCore.QRect(80, 40, 171, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.excel_cikar = QtWidgets.QPushButton(self.page_17)
        self.excel_cikar.setGeometry(QtCore.QRect(360, 40, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.excel_cikar.setFont(font)
        self.excel_cikar.setObjectName("excel_cikar")
        self.stackedWidget.addWidget(self.page_17)
        self.page_16 = QtWidgets.QWidget()
        self.page_16.setObjectName("page_16")
        self.formLayoutWidget_9 = QtWidgets.QWidget(self.page_16)
        self.formLayoutWidget_9.setGeometry(QtCore.QRect(230, 70, 291, 111))
        self.formLayoutWidget_9.setObjectName("formLayoutWidget_9")
        self.formLayout_9 = QtWidgets.QFormLayout(self.formLayoutWidget_9)
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_29 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.kullanici_adi = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kullanici_adi.setFont(font)
        self.kullanici_adi.setObjectName("kullanici_adi")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.kullanici_adi)
        self.label_30 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.parola = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.parola.setFont(font)
        self.parola.setMaxLength(12)
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.parola.setObjectName("parola")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.parola)
        self.label_31 = QtWidgets.QLabel(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.formLayout_9.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.parola_2 = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.parola_2.setFont(font)
        self.parola_2.setMaxLength(12)
        self.parola_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.parola_2.setObjectName("parola_2")
        self.formLayout_9.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.parola_2)
        self.kayit_ol = QtWidgets.QPushButton(self.page_16)
        self.kayit_ol.setGeometry(QtCore.QRect(320, 220, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.kayit_ol.setFont(font)
        self.kayit_ol.setObjectName("kayit_ol")
        self.stackedWidget.addWidget(self.page_16)
        self.page_20 = QtWidgets.QWidget()
        self.page_20.setObjectName("page_20")
        self.formLayoutWidget_10 = QtWidgets.QWidget(self.page_20)
        self.formLayoutWidget_10.setGeometry(QtCore.QRect(110, 50, 221, 61))
        self.formLayoutWidget_10.setObjectName("formLayoutWidget_10")
        self.formLayout_10 = QtWidgets.QFormLayout(self.formLayoutWidget_10)
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_34 = QtWidgets.QLabel(self.formLayoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.kayit_olamama_nedeni = QtWidgets.QLineEdit(self.formLayoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kayit_olamama_nedeni.setFont(font)
        self.kayit_olamama_nedeni.setObjectName("kayit_olamama_nedeni")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.kayit_olamama_nedeni)
        self.kayit_et_2 = QtWidgets.QPushButton(self.page_20)
        self.kayit_et_2.setGeometry(QtCore.QRect(370, 50, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.kayit_et_2.setFont(font)
        self.kayit_et_2.setObjectName("kayit_et_2")
        self.listWidget_4 = QtWidgets.QListWidget(self.page_20)
        self.listWidget_4.setGeometry(QtCore.QRect(110, 150, 256, 192))
        self.listWidget_4.setObjectName("listWidget_4")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget_4.addItem(item)
        self.sebep_sil = QtWidgets.QPushButton(self.page_20)
        self.sebep_sil.setGeometry(QtCore.QRect(400, 160, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sebep_sil.setFont(font)
        self.sebep_sil.setObjectName("sebep_sil")
        self.stackedWidget.addWidget(self.page_20)
        self.page_21 = QtWidgets.QWidget()
        self.page_21.setObjectName("page_21")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page_21)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(150, 70, 160, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ciro_baslangic = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        self.ciro_baslangic.setCalendarPopup(True)
        self.ciro_baslangic.setCurrentSectionIndex(0)
        self.ciro_baslangic.setDate(QtCore.QDate(2021, 1, 1))
        self.ciro_baslangic.setObjectName("ciro_baslangic")
        self.verticalLayout_2.addWidget(self.ciro_baslangic)
        self.cirobitis = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        self.cirobitis.setCalendarPopup(True)
        self.cirobitis.setDate(QtCore.QDate(2021, 1, 1))
        self.cirobitis.setObjectName("cirobitis")
        self.verticalLayout_2.addWidget(self.cirobitis)
        self.pushButton = QtWidgets.QPushButton(self.page_21)
        self.pushButton.setGeometry(QtCore.QRect(370, 100, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formLayoutWidget_11 = QtWidgets.QWidget(self.page_21)
        self.formLayoutWidget_11.setGeometry(QtCore.QRect(370, 190, 261, 80))
        self.formLayoutWidget_11.setObjectName("formLayoutWidget_11")
        self.formLayout_11 = QtWidgets.QFormLayout(self.formLayoutWidget_11)
        self.formLayout_11.setContentsMargins(6, 6, 6, 6)
        self.formLayout_11.setObjectName("formLayout_11")
        self.label_35 = QtWidgets.QLabel(self.formLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.toplam_satis = QtWidgets.QLabel(self.formLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toplam_satis.setFont(font)
        self.toplam_satis.setObjectName("toplam_satis")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.toplam_satis)
        self.label_36 = QtWidgets.QLabel(self.formLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.formLayout_11.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_36)
        self.alinacak_para = QtWidgets.QLabel(self.formLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.alinacak_para.setFont(font)
        self.alinacak_para.setObjectName("alinacak_para")
        self.formLayout_11.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.alinacak_para)
        self.stackedWidget.addWidget(self.page_21)
        self.page_22 = QtWidgets.QWidget()
        self.page_22.setObjectName("page_22")
        self.kayitli_ogrenci_tablosu = QtWidgets.QPushButton(self.page_22)
        self.kayitli_ogrenci_tablosu.setGeometry(QtCore.QRect(230, 60, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.kayitli_ogrenci_tablosu.setFont(font)
        self.kayitli_ogrenci_tablosu.setObjectName("kayitli_ogrenci_tablosu")
        self.kayitli_olmayan_ogrenci = QtWidgets.QPushButton(self.page_22)
        self.kayitli_olmayan_ogrenci.setGeometry(QtCore.QRect(400, 230, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.kayitli_olmayan_ogrenci.setFont(font)
        self.kayitli_olmayan_ogrenci.setObjectName("kayitli_olmayan_ogrenci")
        self.comboBox_4 = QtWidgets.QComboBox(self.page_22)
        self.comboBox_4.setGeometry(QtCore.QRect(150, 240, 181, 41))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.stackedWidget.addWidget(self.page_22)
        self.page_23 = QtWidgets.QWidget()
        self.page_23.setObjectName("page_23")
        self.formLayoutWidget_12 = QtWidgets.QWidget(self.page_23)
        self.formLayoutWidget_12.setGeometry(QtCore.QRect(50, 30, 321, 141))
        self.formLayoutWidget_12.setObjectName("formLayoutWidget_12")
        self.formLayout_12 = QtWidgets.QFormLayout(self.formLayoutWidget_12)
        self.formLayout_12.setContentsMargins(0, 0, 0, 0)
        self.formLayout_12.setObjectName("formLayout_12")
        self.label_37 = QtWidgets.QLabel(self.formLayoutWidget_12)
        self.label_37.setObjectName("label_37")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_37)
        self.adi_soyadi_2 = QtWidgets.QLineEdit(self.formLayoutWidget_12)
        self.adi_soyadi_2.setObjectName("adi_soyadi_2")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.adi_soyadi_2)
        self.label_40 = QtWidgets.QLabel(self.formLayoutWidget_12)
        self.label_40.setObjectName("label_40")
        self.formLayout_12.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_40)
        self.kayit_tarihi_2 = QtWidgets.QDateEdit(self.formLayoutWidget_12)
        self.kayit_tarihi_2.setCalendarPopup(True)
        self.kayit_tarihi_2.setDate(QtCore.QDate(2021, 1, 1))
        self.kayit_tarihi_2.setObjectName("kayit_tarihi_2")
        self.formLayout_12.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kayit_tarihi_2)
        self.label_38 = QtWidgets.QLabel(self.formLayoutWidget_12)
        self.label_38.setObjectName("label_38")
        self.formLayout_12.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_38)
        self.sinif = QtWidgets.QLineEdit(self.formLayoutWidget_12)
        self.sinif.setObjectName("sinif")
        self.formLayout_12.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sinif)
        self.label_39 = QtWidgets.QLabel(self.formLayoutWidget_12)
        self.label_39.setObjectName("label_39")
        self.formLayout_12.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_39)
        self.odeme_tutari = QtWidgets.QLineEdit(self.formLayoutWidget_12)
        self.odeme_tutari.setObjectName("odeme_tutari")
        self.formLayout_12.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.odeme_tutari)
        self.label_41 = QtWidgets.QLabel(self.formLayoutWidget_12)
        self.label_41.setObjectName("label_41")
        self.formLayout_12.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_41)
        self.label_42 = QtWidgets.QLabel(self.formLayoutWidget_12)
        self.label_42.setObjectName("label_42")
        self.formLayout_12.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_42)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.page_23)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(410, 50, 160, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.arama = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.arama.setObjectName("arama")
        self.verticalLayout_3.addWidget(self.arama)
        self.odeme = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.odeme.setObjectName("odeme")
        self.verticalLayout_3.addWidget(self.odeme)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_23)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 270, 771, 261))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(11)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, item)
        self.stackedWidget.addWidget(self.page_23)
        self.page_24 = QtWidgets.QWidget()
        self.page_24.setObjectName("page_24")
        self.stackedWidget.addWidget(self.page_24)
        neos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(neos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menu_renci_lemleri = QtWidgets.QMenu(self.menubar)
        self.menu_renci_lemleri.setObjectName("menu_renci_lemleri")
        self.menuS_n_f = QtWidgets.QMenu(self.menubar)
        self.menuS_n_f.setObjectName("menuS_n_f")
        self.menuAna_Sayfa = QtWidgets.QMenu(self.menubar)
        self.menuAna_Sayfa.setObjectName("menuAna_Sayfa")
        self.menuTablolar = QtWidgets.QMenu(self.menubar)
        self.menuTablolar.setObjectName("menuTablolar")
        self.menuGiri_lemleri = QtWidgets.QMenu(self.menubar)
        self.menuGiri_lemleri.setObjectName("menuGiri_lemleri")
        self.menuSebepeler_ekle = QtWidgets.QMenu(self.menubar)
        self.menuSebepeler_ekle.setObjectName("menuSebepeler_ekle")
        self.menu_deme_islemleri = QtWidgets.QMenu(self.menubar)
        self.menu_deme_islemleri.setObjectName("menu_deme_islemleri")
        neos.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(neos)
        self.statusbar.setObjectName("statusbar")
        neos.setStatusBar(self.statusbar)
        self.action_renci_Kaydet = QtWidgets.QAction(neos)
        self.action_renci_Kaydet.setObjectName("action_renci_Kaydet")
        self.action_renci_Bilgileri = QtWidgets.QAction(neos)
        self.action_renci_Bilgileri.setObjectName("action_renci_Bilgileri")
        self.actionS_n_f_Olu_tur = QtWidgets.QAction(neos)
        self.actionS_n_f_Olu_tur.setObjectName("actionS_n_f_Olu_tur")
        self.actionS_n_fa_renci_Ekle = QtWidgets.QAction(neos)
        self.actionS_n_fa_renci_Ekle.setObjectName("actionS_n_fa_renci_Ekle")
        self.actionAnasayfa_Giri = QtWidgets.QAction(neos)
        self.actionAnasayfa_Giri.setObjectName("actionAnasayfa_Giri")
        self.actionExcel_Tablosu = QtWidgets.QAction(neos)
        self.actionExcel_Tablosu.setObjectName("actionExcel_Tablosu")
        self.actionDurum_Tablosu = QtWidgets.QAction(neos)
        self.actionDurum_Tablosu.setObjectName("actionDurum_Tablosu")
        self.actionCiro_Tablosu = QtWidgets.QAction(neos)
        self.actionCiro_Tablosu.setObjectName("actionCiro_Tablosu")
        self.actionNeos_Yaz_l_m_ye_olu_tur = QtWidgets.QAction(neos)
        self.actionNeos_Yaz_l_m_ye_olu_tur.setObjectName("actionNeos_Yaz_l_m_ye_olu_tur")
        self.action_k = QtWidgets.QAction(neos)
        self.action_k.setObjectName("action_k")
        self.actionKay_t_Olamama_Nedenleri = QtWidgets.QAction(neos)
        self.actionKay_t_Olamama_Nedenleri.setObjectName("actionKay_t_Olamama_Nedenleri")
        self.action_deme_Al = QtWidgets.QAction(neos)
        self.action_deme_Al.setObjectName("action_deme_Al")
        self.menu_renci_lemleri.addAction(self.action_renci_Kaydet)
        self.menu_renci_lemleri.addAction(self.action_renci_Bilgileri)
        self.menuS_n_f.addAction(self.actionS_n_f_Olu_tur)
        self.menuS_n_f.addAction(self.actionS_n_fa_renci_Ekle)
        self.menuAna_Sayfa.addSeparator()
        self.menuAna_Sayfa.addAction(self.actionAnasayfa_Giri)
        self.menuTablolar.addAction(self.actionExcel_Tablosu)
        self.menuTablolar.addAction(self.actionDurum_Tablosu)
        self.menuTablolar.addAction(self.actionCiro_Tablosu)
        self.menuGiri_lemleri.addAction(self.actionNeos_Yaz_l_m_ye_olu_tur)
        self.menuGiri_lemleri.addAction(self.action_k)
        self.menuSebepeler_ekle.addAction(self.actionKay_t_Olamama_Nedenleri)
        self.menu_deme_islemleri.addAction(self.action_deme_Al)
        self.menubar.addAction(self.menuAna_Sayfa.menuAction())
        self.menubar.addAction(self.menu_renci_lemleri.menuAction())
        self.menubar.addAction(self.menuS_n_f.menuAction())
        self.menubar.addAction(self.menuTablolar.menuAction())
        self.menubar.addAction(self.menuGiri_lemleri.menuAction())
        self.menubar.addAction(self.menuSebepeler_ekle.menuAction())
        self.menubar.addAction(self.menu_deme_islemleri.menuAction())

        self.retranslateUi(neos)
        self.stackedWidget.setCurrentIndex(5)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.taksitler.setCurrentIndex(0)
        self.listWidget_2.setCurrentRow(-1)
        self.comboBox.activated['QString'].connect(self.label_19.setText)
        self.taksit_combo.currentIndexChanged['int'].connect(self.taksitler.setCurrentIndex)
        self.comboBox_2.currentIndexChanged['int'].connect(self.stackedWidget_2.setCurrentIndex)
        self.comboBox_2.currentIndexChanged['int'].connect(self.stackedWidget_3.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(neos)

    def retranslateUi(self, neos):
        _translate = QtCore.QCoreApplication.translate
        neos.setWindowTitle(_translate("neos", "Neos Yazılım "))
        self.label.setText(_translate("neos", "Kullanıcı Adı :"))
        self.label_2.setText(_translate("neos", "Şifre : "))
        self.giris_buton.setText(_translate("neos", "Giriş "))
        self.label_3.setText(_translate("neos", "İsim Soyisim : "))
        self.label_4.setText(_translate("neos", "Kayıt Tarihi :"))
        self.label_6.setText(_translate("neos", "Telefon :"))
        self.label_5.setText(_translate("neos", "Email :"))
        self.label_7.setText(_translate("neos", "Not  :"))
        self.kayit_et.setText(_translate("neos", "Kayıt Et"))
        self.comboBox_5.setItemText(0, _translate("neos", "Kayıt Olmama Nedenleri"))
        self.comboBox_5.setItemText(1, _translate("neos", "1"))
        self.comboBox_5.setItemText(2, _translate("neos", "2"))
        self.comboBox_5.setItemText(3, _translate("neos", "3"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("neos", "Kayıt Olamam Nedenleri"))
        item = self.listWidget_3.item(1)
        item.setText(_translate("neos", "1"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.cikar.setText(_translate("neos", "-"))
        self.label_8.setText(_translate("neos", "Adı ve Soyadı :"))
        self.label_9.setText(_translate("neos", "Telefon :"))
        self.label_10.setText(_translate("neos", "Email :"))
        self.label_11.setText(_translate("neos", "Kayıt Tarihi :"))
        self.label_12.setText(_translate("neos", "Not :"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("neos", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("neos", "Adı Soyadı"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("neos", "Telefon"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("neos", "Mail Adresi"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("neos", "Açıklama"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("neos", "Kayıt Tarihi"))
        self.guncelle.setText(_translate("neos", "Güncelle "))
        self.silme.setText(_translate("neos", "Sil"))
        self.comboBox.setItemText(0, _translate("neos", "Hack"))
        self.comboBox.setItemText(1, _translate("neos", "front end"))
        self.comboBox.setItemText(2, _translate("neos", "Web"))
        self.label_13.setText(_translate("neos", "Sınıflar ;)"))
        self.label_14.setText(_translate("neos", "Adı Soyadı :"))
        self.ogrenci_adi.setText(_translate("neos", "Öğrenci Soyadı"))
        self.label_15.setText(_translate("neos", "Telefonı :"))
        self.label_16.setText(_translate("neos", "Telefonı Nuamrası"))
        self.label_17.setText(_translate("neos", "Mail Adresi :"))
        self.label_18.setText(_translate("neos", "Örenek Mail "))
        self.label_19.setText(_translate("neos", "Eğitim Seçmelisiniz !!!"))
        self.label_20.setText(_translate("neos", "Ücret :"))
        self.ucret.setPlaceholderText(_translate("neos", "Talep Edilen Ücret"))
        self.kayit_et_sinif.setText(_translate("neos", "Kayıt Et"))
        self.comboBox_2.setItemText(0, _translate("neos", "Ödeme Yöntemi"))
        self.comboBox_2.setItemText(1, _translate("neos", "Peşin "))
        self.comboBox_2.setItemText(2, _translate("neos", "Taksitli"))
        self.label_28.setText(_translate("neos", "Ödeme Yontemi Seçin"))
        self.label_23.setText(_translate("neos", "Peşin :"))
        self.pesin.setPlaceholderText(_translate("neos", "Peşin İse"))
        self.label_21.setText(_translate("neos", "Ön Ödeme (Var İse) :"))
        self.onodeme.setPlaceholderText(_translate("neos", "Ön Ödeme"))
        self.taksit_combo.setItemText(0, _translate("neos", "0"))
        self.taksit_combo.setItemText(1, _translate("neos", "1"))
        self.taksit_combo.setItemText(2, _translate("neos", "2"))
        self.taksit_combo.setItemText(3, _translate("neos", "3"))
        self.label_22.setText(_translate("neos", "Taksit Seçmelisiniz"))
        self.ilk_taksit.setPlaceholderText(_translate("neos", "Taksit Tutarı"))
        self.ilk_taksitt.setPlaceholderText(_translate("neos", "İlk Taksit"))
        self.ilk_taksitt_2.setPlaceholderText(_translate("neos", "ikinci Taksit"))
        self.taksit_3_ilk.setPlaceholderText(_translate("neos", "İlk Taksit Tutarı"))
        self.taksit_3_ilk_2.setPlaceholderText(_translate("neos", "İkinci Taksit Tutarı"))
        self.taksit_3_ilk_3.setPlaceholderText(_translate("neos", "üçüncü Taksit Tutarı"))
        self.checkBox.setText(_translate("neos", "İCCW"))
        self.checkBox_2.setText(_translate("neos", "Katılım "))
        self.checkBox_3.setText(_translate("neos", "Üniversite"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("neos", "Telefon "))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("neos", "Adı Soyadı"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_33.setText(_translate("neos", "Öğrenci Adı :"))
        self.bul.setText(_translate("neos", "Bul "))
        self.label_24.setText(_translate("neos", "Eğitim Adı :"))
        self.sinif_adi.setPlaceholderText(_translate("neos", "Eğitim Adı"))
        self.label_25.setText(_translate("neos", "Eğitim Fiyatı :"))
        self.egitim_tutari.setPlaceholderText(_translate("neos", "Eğitim Fiyatı"))
        self.label_26.setText(_translate("neos", "Eğitim Tarihi :"))
        self.label_27.setText(_translate("neos", "Eğitim Bitiş Tarihi :"))
        self.egitim_kaydet.setText(_translate("neos", "Sınıfı Kaydet"))
        self.comboBox_3.setItemText(0, _translate("neos", "Sınıf Seçin"))
        self.comboBox_3.setItemText(1, _translate("neos", "Front End"))
        self.comboBox_3.setItemText(2, _translate("neos", "Back End"))
        self.excel_cikar.setText(_translate("neos", "Excel Cıkar"))
        self.label_29.setText(_translate("neos", "Kullanıcı Adı :"))
        self.kullanici_adi.setPlaceholderText(_translate("neos", "Kullanıcı Adı"))
        self.label_30.setText(_translate("neos", "Parola : "))
        self.parola.setPlaceholderText(_translate("neos", "Şifre"))
        self.label_31.setText(_translate("neos", "Parola Tekrar : "))
        self.parola_2.setPlaceholderText(_translate("neos", "Şifre Tekrar "))
        self.kayit_ol.setText(_translate("neos", "Kayıt Ol "))
        self.label_34.setText(_translate("neos", "Sebep Ekle : "))
        self.kayit_et_2.setText(_translate("neos", "Kayıt Et"))
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        item = self.listWidget_4.item(0)
        item.setText(_translate("neos", "Kayıt Olamama Nedenleri "))
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        self.sebep_sil.setText(_translate("neos", "Sil"))
        self.pushButton.setText(_translate("neos", "Excel ve Tablo"))
        self.label_35.setText(_translate("neos", "Toplam Satış :"))
        self.toplam_satis.setText(_translate("neos", "0"))
        self.label_36.setText(_translate("neos", "Alınacak Para :"))
        self.alinacak_para.setText(_translate("neos", "0"))
        self.kayitli_ogrenci_tablosu.setText(_translate("neos", "Kayıtlı Öğrenci Tablosu"))
        self.kayitli_olmayan_ogrenci.setText(_translate("neos", "Kayıtlı Olmayan Öğrenci Tablosu"))
        self.comboBox_4.setItemText(0, _translate("neos", "Kayıt Olamama Nedeni"))
        self.comboBox_4.setItemText(1, _translate("neos", "1"))
        self.comboBox_4.setItemText(2, _translate("neos", "2"))
        self.comboBox_4.setItemText(3, _translate("neos", "3"))
        self.label_37.setText(_translate("neos", "Adı ve Soyadı :"))
        self.label_40.setText(_translate("neos", "Taksit Tarihi :"))
        self.label_38.setText(_translate("neos", "Sınıf  :"))
        self.label_39.setText(_translate("neos", "Ödemesi Gereken taksit :"))
        self.label_41.setText(_translate("neos", "Kalan Tutar :"))
        self.label_42.setText(_translate("neos", "0"))
        self.arama.setText(_translate("neos", "ARA"))
        self.odeme.setText(_translate("neos", "Öde"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("neos", "id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("neos", "Adı Soyadı "))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("neos", "Sınıfı"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("neos", "Toplam Ücret "))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("neos", "Ödenen Ücret"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("neos", "1. Taksit"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("neos", "Taksit Tarihi"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("neos", "2. Taksit"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("neos", "Taksit Tarihi"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("neos", "3. Taksit"))
        item = self.tableWidget_2.horizontalHeaderItem(10)
        item.setText(_translate("neos", "Taksit Tarih"))
        self.menu_renci_lemleri.setTitle(_translate("neos", "Öğrenci İşlemleri"))
        self.menuS_n_f.setTitle(_translate("neos", "Sınıf"))
        self.menuAna_Sayfa.setTitle(_translate("neos", "Ana Sayfa"))
        self.menuTablolar.setTitle(_translate("neos", "Tablolar"))
        self.menuGiri_lemleri.setTitle(_translate("neos", "Giriş İşlemleri"))
        self.menuSebepeler_ekle.setTitle(_translate("neos", "Sebepeler ekle"))
        self.menu_deme_islemleri.setTitle(_translate("neos", "Ödeme İslemleri"))
        self.action_renci_Kaydet.setText(_translate("neos", "Öğrenci Kaydet"))
        self.action_renci_Bilgileri.setText(_translate("neos", "Öğrenci Bilgileri"))
        self.actionS_n_f_Olu_tur.setText(_translate("neos", "Sınıf Oluştur"))
        self.actionS_n_fa_renci_Ekle.setText(_translate("neos", "Sınıfa Öğrenci Ekle"))
        self.actionAnasayfa_Giri.setText(_translate("neos", "Anasayfa Giriş "))
        self.actionExcel_Tablosu.setText(_translate("neos", "Excel Kaydı"))
        self.actionDurum_Tablosu.setText(_translate("neos", "Öğrenci Tablosu "))
        self.actionCiro_Tablosu.setText(_translate("neos", "Ciro Tablosu "))
        self.actionNeos_Yaz_l_m_ye_olu_tur.setText(_translate("neos", "Neos Yazılım Üye oluştur"))
        self.action_k.setText(_translate("neos", "Çıkış "))
        self.actionKay_t_Olamama_Nedenleri.setText(_translate("neos", "Kayıt Olamama Nedenleri "))
        self.action_deme_Al.setText(_translate("neos", "Taksit Ödemesi"))

