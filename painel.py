# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'painel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Janela2(object):
    def setupUi(self, Janela2):
        Janela2.setObjectName("Janela2")
        Janela2.resize(774, 558)
        self.centralwidget = QtWidgets.QWidget(Janela2)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.label_boasVindas = QtWidgets.QLabel(self.centralwidget)
        self.label_boasVindas.setGeometry(QtCore.QRect(210, 10, 371, 51))
        self.label_boasVindas.setStyleSheet("font: 18pt \"Bahnschrift SemiLight Condensed\";\n"
"border-top-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 170, 0);\n"
"gridline-color: rgb(255, 0, 0);")
        self.label_boasVindas.setText("")
        self.label_boasVindas.setObjectName("label_boasVindas")
        self.label_dia1 = QtWidgets.QLabel(self.centralwidget)
        self.label_dia1.setGeometry(QtCore.QRect(250, 60, 291, 31))
        self.label_dia1.setStyleSheet("font: 14pt \"Bahnschrift SemiLight Condensed\";")
        self.label_dia1.setText("")
        self.label_dia1.setObjectName("label_dia1")
        self.buttton_verAlunos = QtWidgets.QPushButton(self.centralwidget)
        self.buttton_verAlunos.setGeometry(QtCore.QRect(90, 210, 161, 81))
        self.buttton_verAlunos.setStyleSheet("font: 11pt \"Bahnschrift SemiLight Condensed\";\n"
"background-color: rgb(85, 170, 255);")
        self.buttton_verAlunos.setObjectName("buttton_verAlunos")
        self.button_Cadastro = QtWidgets.QPushButton(self.centralwidget)
        self.button_Cadastro.setGeometry(QtCore.QRect(320, 210, 171, 81))
        self.button_Cadastro.setStyleSheet("font: 12pt \"Bahnschrift SemiLight Condensed\";\n"
"background-color: rgb(85, 255, 127);")
        self.button_Cadastro.setObjectName("button_Cadastro")
        Janela2.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(Janela2)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 774, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuMudar_cor = QtWidgets.QMenu(self.menuBar)
        self.menuMudar_cor.setObjectName("menuMudar_cor")
        self.menuCr_ditos = QtWidgets.QMenu(self.menuBar)
        self.menuCr_ditos.setObjectName("menuCr_ditos")
        Janela2.setMenuBar(self.menuBar)
        self.actionPreto = QtWidgets.QAction(Janela2)
        self.actionPreto.setObjectName("actionPreto")
        self.actionVermelho = QtWidgets.QAction(Janela2)
        self.actionVermelho.setObjectName("actionVermelho")
        self.actionAzul = QtWidgets.QAction(Janela2)
        self.actionAzul.setObjectName("actionAzul")
        self.actionAmarelo = QtWidgets.QAction(Janela2)
        self.actionAmarelo.setObjectName("actionAmarelo")
        self.actionAuthor_Leandro_Furtado_de_Sousa = QtWidgets.QAction(Janela2)
        self.actionAuthor_Leandro_Furtado_de_Sousa.setObjectName("actionAuthor_Leandro_Furtado_de_Sousa")
        self.menuMudar_cor.addAction(self.actionPreto)
        self.menuMudar_cor.addAction(self.actionVermelho)
        self.menuMudar_cor.addAction(self.actionAzul)
        self.menuMudar_cor.addAction(self.actionAmarelo)
        self.menuCr_ditos.addAction(self.actionAuthor_Leandro_Furtado_de_Sousa)
        self.menuBar.addAction(self.menuMudar_cor.menuAction())
        self.menuBar.addAction(self.menuCr_ditos.menuAction())

        self.retranslateUi(Janela2)
        QtCore.QMetaObject.connectSlotsByName(Janela2)

    def retranslateUi(self, Janela2):
        _translate = QtCore.QCoreApplication.translate
        Janela2.setWindowTitle(_translate("Janela2", "Painel Academia"))
        self.buttton_verAlunos.setText(_translate("Janela2", "ALUNOS E PLANOS"))
        self.button_Cadastro.setText(_translate("Janela2", "CADASTRAR NOVO ALUNO"))
        self.menuMudar_cor.setTitle(_translate("Janela2", "Mudar cor de fundo"))
        self.menuCr_ditos.setTitle(_translate("Janela2", "Créditos"))
        self.actionPreto.setText(_translate("Janela2", "Preto"))
        self.actionVermelho.setText(_translate("Janela2", "Vermelho"))
        self.actionAzul.setText(_translate("Janela2", "Azul"))
        self.actionAmarelo.setText(_translate("Janela2", "Amarelo"))
        self.actionAuthor_Leandro_Furtado_de_Sousa.setText(_translate("Janela2", "Dev: Leandro Furtado de Sousa"))