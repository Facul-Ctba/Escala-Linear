# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1036, 844)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_principal = QFrame(self.centralwidget)
        self.fr_principal.setObjectName(u"fr_principal")
        self.fr_principal.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fr_principal.sizePolicy().hasHeightForWidth())
        self.fr_principal.setSizePolicy(sizePolicy1)
        self.fr_principal.setAutoFillBackground(False)
        self.fr_principal.setStyleSheet(u"")
        self.fr_principal.setFrameShape(QFrame.StyledPanel)
        self.fr_principal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_principal)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.fr_esquerda = QFrame(self.fr_principal)
        self.fr_esquerda.setObjectName(u"fr_esquerda")
        sizePolicy1.setHeightForWidth(self.fr_esquerda.sizePolicy().hasHeightForWidth())
        self.fr_esquerda.setSizePolicy(sizePolicy1)
        self.fr_esquerda.setMinimumSize(QSize(319, 484))
        self.fr_esquerda.setStyleSheet(u"")
        self.fr_esquerda.setFrameShape(QFrame.StyledPanel)
        self.fr_esquerda.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.fr_esquerda)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.lb_autor = QLabel(self.fr_esquerda)
        self.lb_autor.setObjectName(u"lb_autor")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.lb_autor.sizePolicy().hasHeightForWidth())
        self.lb_autor.setSizePolicy(sizePolicy2)
        self.lb_autor.setMaximumSize(QSize(450, 30))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(6)
        font.setBold(True)
        self.lb_autor.setFont(font)
        self.lb_autor.setScaledContents(True)
        self.lb_autor.setAlignment(Qt.AlignCenter)
        self.lb_autor.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.lb_autor)

        self.hs_input = QSlider(self.fr_esquerda)
        self.hs_input.setObjectName(u"hs_input")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.hs_input.sizePolicy().hasHeightForWidth())
        self.hs_input.setSizePolicy(sizePolicy3)
        self.hs_input.setMinimumSize(QSize(0, 50))
        self.hs_input.setCursor(QCursor(Qt.PointingHandCursor))
        self.hs_input.setStyleSheet(u"")
        self.hs_input.setMaximum(100)
        self.hs_input.setPageStep(1)
        self.hs_input.setOrientation(Qt.Horizontal)
        self.hs_input.setTickPosition(QSlider.TicksBelow)
        self.hs_input.setTickInterval(5)

        self.verticalLayout_4.addWidget(self.hs_input)

        self.gl_esquerda = QGridLayout()
        self.gl_esquerda.setObjectName(u"gl_esquerda")
        self.gl_esquerda.setSizeConstraint(QLayout.SetNoConstraint)
        self.gl_esquerda.setHorizontalSpacing(10)
        self.gl_esquerda.setVerticalSpacing(0)
        self.gl_esquerda.setContentsMargins(10, -1, 10, -1)
        self.lb_input = QLabel(self.fr_esquerda)
        self.lb_input.setObjectName(u"lb_input")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.lb_input.setFont(font1)
        self.lb_input.setStyleSheet(u"")
        self.lb_input.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gl_esquerda.addWidget(self.lb_input, 0, 0, 1, 1)

        self.lb_X0 = QLabel(self.fr_esquerda)
        self.lb_X0.setObjectName(u"lb_X0")
        self.lb_X0.setFont(font1)
        self.lb_X0.setStyleSheet(u"")
        self.lb_X0.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gl_esquerda.addWidget(self.lb_X0, 2, 0, 1, 1)

        self.le_input = QLineEdit(self.fr_esquerda)
        self.le_input.setObjectName(u"le_input")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.le_input.sizePolicy().hasHeightForWidth())
        self.le_input.setSizePolicy(sizePolicy4)
        self.le_input.setFont(font1)
        self.le_input.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gl_esquerda.addWidget(self.le_input, 0, 1, 1, 1)

        self.le_X1 = QLineEdit(self.fr_esquerda)
        self.le_X1.setObjectName(u"le_X1")
        sizePolicy4.setHeightForWidth(self.le_X1.sizePolicy().hasHeightForWidth())
        self.le_X1.setSizePolicy(sizePolicy4)
        self.le_X1.setFont(font1)
        self.le_X1.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gl_esquerda.addWidget(self.le_X1, 3, 1, 1, 1)

        self.cb_limite = QCheckBox(self.fr_esquerda)
        self.cb_limite.setObjectName(u"cb_limite")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.cb_limite.setFont(font2)
        self.cb_limite.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_limite.setStyleSheet(u"")
        self.cb_limite.setIconSize(QSize(20, 20))

        self.gl_esquerda.addWidget(self.cb_limite, 7, 1, 1, 1)

        self.lb_Y0 = QLabel(self.fr_esquerda)
        self.lb_Y0.setObjectName(u"lb_Y0")
        self.lb_Y0.setFont(font1)
        self.lb_Y0.setStyleSheet(u"")
        self.lb_Y0.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gl_esquerda.addWidget(self.lb_Y0, 4, 0, 1, 1)

        self.lb_Y1 = QLabel(self.fr_esquerda)
        self.lb_Y1.setObjectName(u"lb_Y1")
        self.lb_Y1.setFont(font1)
        self.lb_Y1.setStyleSheet(u"")
        self.lb_Y1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gl_esquerda.addWidget(self.lb_Y1, 5, 0, 1, 1)

        self.le_Y1 = QLineEdit(self.fr_esquerda)
        self.le_Y1.setObjectName(u"le_Y1")
        sizePolicy4.setHeightForWidth(self.le_Y1.sizePolicy().hasHeightForWidth())
        self.le_Y1.setSizePolicy(sizePolicy4)
        self.le_Y1.setFont(font1)
        self.le_Y1.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gl_esquerda.addWidget(self.le_Y1, 5, 1, 1, 1)

        self.lb_X1 = QLabel(self.fr_esquerda)
        self.lb_X1.setObjectName(u"lb_X1")
        self.lb_X1.setFont(font1)
        self.lb_X1.setStyleSheet(u"")
        self.lb_X1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gl_esquerda.addWidget(self.lb_X1, 3, 0, 1, 1)

        self.le_X0 = QLineEdit(self.fr_esquerda)
        self.le_X0.setObjectName(u"le_X0")
        sizePolicy4.setHeightForWidth(self.le_X0.sizePolicy().hasHeightForWidth())
        self.le_X0.setSizePolicy(sizePolicy4)
        self.le_X0.setFont(font1)
        self.le_X0.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gl_esquerda.addWidget(self.le_X0, 2, 1, 1, 1)

        self.le_Y0 = QLineEdit(self.fr_esquerda)
        self.le_Y0.setObjectName(u"le_Y0")
        sizePolicy4.setHeightForWidth(self.le_Y0.sizePolicy().hasHeightForWidth())
        self.le_Y0.setSizePolicy(sizePolicy4)
        self.le_Y0.setFont(font1)
        self.le_Y0.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gl_esquerda.addWidget(self.le_Y0, 4, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gl_esquerda)

        self.bt_calculate = QPushButton(self.fr_esquerda)
        self.bt_calculate.setObjectName(u"bt_calculate")
        self.bt_calculate.setMinimumSize(QSize(0, 60))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(18)
        self.bt_calculate.setFont(font3)
        self.bt_calculate.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_calculate.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"Icones/calculator_22694.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_calculate.setIcon(icon)
        self.bt_calculate.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.bt_calculate)

        self.bt_load = QPushButton(self.fr_esquerda)
        self.bt_load.setObjectName(u"bt_load")
        self.bt_load.setMinimumSize(QSize(0, 60))
        self.bt_load.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"Icones/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_load.setIcon(icon1)
        self.bt_load.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.bt_load)

        self.bt_save = QPushButton(self.fr_esquerda)
        self.bt_save.setObjectName(u"bt_save")
        self.bt_save.setMinimumSize(QSize(0, 60))
        self.bt_save.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"Icones/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_save.setIcon(icon2)
        self.bt_save.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.bt_save)


        self.horizontalLayout.addWidget(self.fr_esquerda)

        self.fr_direita = QFrame(self.fr_principal)
        self.fr_direita.setObjectName(u"fr_direita")
        sizePolicy1.setHeightForWidth(self.fr_direita.sizePolicy().hasHeightForWidth())
        self.fr_direita.setSizePolicy(sizePolicy1)
        self.fr_direita.setMinimumSize(QSize(318, 484))
        self.fr_direita.setStyleSheet(u"")
        self.fr_direita.setFrameShape(QFrame.StyledPanel)
        self.fr_direita.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.fr_direita)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.gl_direita = QGridLayout()
        self.gl_direita.setObjectName(u"gl_direita")
        self.gl_direita.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gl_direita.setHorizontalSpacing(10)
        self.gl_direita.setVerticalSpacing(0)
        self.gl_direita.setContentsMargins(10, -1, 10, -1)
        self.lb_out = QLabel(self.fr_direita)
        self.lb_out.setObjectName(u"lb_out")
        self.lb_out.setFont(font1)
        self.lb_out.setStyleSheet(u"")
        self.lb_out.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gl_direita.addWidget(self.lb_out, 0, 0, 1, 1)

        self.le_output = QLineEdit(self.fr_direita)
        self.le_output.setObjectName(u"le_output")
        sizePolicy4.setHeightForWidth(self.le_output.sizePolicy().hasHeightForWidth())
        self.le_output.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.le_output.setFont(font4)
        self.le_output.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gl_direita.addWidget(self.le_output, 0, 1, 1, 1)

        self.lb_m = QLabel(self.fr_direita)
        self.lb_m.setObjectName(u"lb_m")
        self.lb_m.setFont(font1)
        self.lb_m.setStyleSheet(u"")
        self.lb_m.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gl_direita.addWidget(self.lb_m, 1, 0, 1, 1)

        self.le_m = QLineEdit(self.fr_direita)
        self.le_m.setObjectName(u"le_m")
        sizePolicy4.setHeightForWidth(self.le_m.sizePolicy().hasHeightForWidth())
        self.le_m.setSizePolicy(sizePolicy4)
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(12)
        font5.setItalic(True)
        self.le_m.setFont(font5)
        self.le_m.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gl_direita.addWidget(self.le_m, 1, 1, 1, 1)

        self.lb_b = QLabel(self.fr_direita)
        self.lb_b.setObjectName(u"lb_b")
        self.lb_b.setFont(font1)
        self.lb_b.setStyleSheet(u"")
        self.lb_b.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gl_direita.addWidget(self.lb_b, 2, 0, 1, 1)

        self.le_b = QLineEdit(self.fr_direita)
        self.le_b.setObjectName(u"le_b")
        sizePolicy4.setHeightForWidth(self.le_b.sizePolicy().hasHeightForWidth())
        self.le_b.setSizePolicy(sizePolicy4)
        self.le_b.setFont(font5)
        self.le_b.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gl_direita.addWidget(self.le_b, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gl_direita)

        self.fr_grafico = QWidget(self.fr_direita)
        self.fr_grafico.setObjectName(u"fr_grafico")
        sizePolicy1.setHeightForWidth(self.fr_grafico.sizePolicy().hasHeightForWidth())
        self.fr_grafico.setSizePolicy(sizePolicy1)
        self.fr_grafico.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.fr_grafico)


        self.horizontalLayout.addWidget(self.fr_direita)


        self.verticalLayout.addWidget(self.fr_principal)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.le_input, self.le_X0)
        QWidget.setTabOrder(self.le_X0, self.le_X1)
        QWidget.setTabOrder(self.le_X1, self.le_Y0)
        QWidget.setTabOrder(self.le_Y0, self.le_Y1)
        QWidget.setTabOrder(self.le_Y1, self.cb_limite)
        QWidget.setTabOrder(self.cb_limite, self.le_output)
        QWidget.setTabOrder(self.le_output, self.le_m)
        QWidget.setTabOrder(self.le_m, self.le_b)
        QWidget.setTabOrder(self.le_b, self.bt_calculate)
        QWidget.setTabOrder(self.bt_calculate, self.bt_load)
        QWidget.setTabOrder(self.bt_load, self.bt_save)
        QWidget.setTabOrder(self.bt_save, self.hs_input)

        self.retranslateUi(MainWindow)
        self.bt_calculate.clicked.connect(MainWindow.calculo)
        self.hs_input.valueChanged.connect(MainWindow.inc_dec)
        self.le_input.returnPressed.connect(MainWindow.calculo)
        self.bt_load.clicked.connect(MainWindow.load_arquivo)
        self.bt_save.clicked.connect(MainWindow.save_arquivo)
        self.le_input.textChanged.connect(MainWindow.calculo)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"C\u00e1lculo de Escala Linear", None))
        self.lb_autor.setText(QCoreApplication.translate("MainWindow", u"Alexandre de \u00c1vila @ Todos os Direitos Reservados", None))
        self.lb_input.setText(QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.lb_X0.setText(QCoreApplication.translate("MainWindow", u"X0", None))
        self.le_input.setText("")
        self.cb_limite.setText(QCoreApplication.translate("MainWindow", u"Limite", None))
        self.lb_Y0.setText(QCoreApplication.translate("MainWindow", u"Y0", None))
        self.lb_Y1.setText(QCoreApplication.translate("MainWindow", u"Y1", None))
        self.lb_X1.setText(QCoreApplication.translate("MainWindow", u"X1", None))
        self.bt_calculate.setText(QCoreApplication.translate("MainWindow", u"Calcule", None))
        self.bt_load.setText(QCoreApplication.translate("MainWindow", u"Carregar Arquivo", None))
        self.bt_save.setText(QCoreApplication.translate("MainWindow", u"Salvar em Arquivo", None))
        self.lb_out.setText(QCoreApplication.translate("MainWindow", u"Sa\u00edda", None))
        self.lb_m.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.lb_b.setText(QCoreApplication.translate("MainWindow", u"b", None))
    # retranslateUi

