# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_editamatricula.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JanelaEditaMatricula(object):
    def setupUi(self, JanelaEditaMatricula):
        JanelaEditaMatricula.setObjectName("JanelaEditaMatricula")
        JanelaEditaMatricula.resize(575, 357)
        self.centralwidget = QtWidgets.QWidget(JanelaEditaMatricula)
        self.centralwidget.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.centralwidget.setObjectName("centralwidget")
        self.input_id = QtWidgets.QLineEdit(self.centralwidget)
        self.input_id.setGeometry(QtCore.QRect(40, 90, 161, 31))
        self.input_id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_id.setObjectName("input_id")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 311, 51))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Bahnschrift SemiLight Condensed\";")
        self.label.setObjectName("label")
        self.button_DeletaMatricula = QtWidgets.QPushButton(self.centralwidget)
        self.button_DeletaMatricula.setGeometry(QtCore.QRect(210, 250, 121, 31))
        self.button_DeletaMatricula.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 12pt \"Bahnschrift SemiLight Condensed\";")
        self.button_DeletaMatricula.setObjectName("button_DeletaMatricula")
        self.button_AddTrinta = QtWidgets.QPushButton(self.centralwidget)
        self.button_AddTrinta.setGeometry(QtCore.QRect(170, 130, 201, 31))
        self.button_AddTrinta.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"font: 12pt \"Bahnschrift SemiLight Condensed\";")
        self.button_AddTrinta.setObjectName("button_AddTrinta")
        self.button_AddNoventa = QtWidgets.QPushButton(self.centralwidget)
        self.button_AddNoventa.setGeometry(QtCore.QRect(170, 170, 201, 31))
        self.button_AddNoventa.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"font: 12pt \"Bahnschrift SemiLight Condensed\";")
        self.button_AddNoventa.setObjectName("button_AddNoventa")
        self.button_AddUmAno = QtWidgets.QPushButton(self.centralwidget)
        self.button_AddUmAno.setGeometry(QtCore.QRect(170, 210, 201, 31))
        self.button_AddUmAno.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"font: 12pt \"Bahnschrift SemiLight Condensed\";")
        self.button_AddUmAno.setObjectName("button_AddUmAno")
        self.label_Erros = QtWidgets.QLabel(self.centralwidget)
        self.label_Erros.setGeometry(QtCore.QRect(120, 310, 331, 31))
        self.label_Erros.setStyleSheet("color: rgb(85, 255, 0);")
        self.label_Erros.setText("")
        self.label_Erros.setObjectName("label_Erros")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 30, 311, 51))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Bahnschrift SemiLight Condensed\";")
        self.label_2.setObjectName("label_2")
        self.input_ContatoEdita = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ContatoEdita.setGeometry(QtCore.QRect(340, 90, 161, 31))
        self.input_ContatoEdita.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_ContatoEdita.setObjectName("input_ContatoEdita")
        JanelaEditaMatricula.setCentralWidget(self.centralwidget)

        self.retranslateUi(JanelaEditaMatricula)
        QtCore.QMetaObject.connectSlotsByName(JanelaEditaMatricula)

    def retranslateUi(self, JanelaEditaMatricula):
        _translate = QtCore.QCoreApplication.translate
        JanelaEditaMatricula.setWindowTitle(_translate("JanelaEditaMatricula", "Editando Matricula"))
        self.label.setText(_translate("JanelaEditaMatricula", "DIGITE O NUMERO DE INSCRIÇÃO DO ALUNO(A):"))
        self.button_DeletaMatricula.setText(_translate("JanelaEditaMatricula", "DELETAR MATRÍCULA"))
        self.button_AddTrinta.setText(_translate("JanelaEditaMatricula", "ADICIONAR (Plano Mensal)30dias"))
        self.button_AddNoventa.setText(_translate("JanelaEditaMatricula", "ADICIONAR (Plano Trimensal)90dias"))
        self.button_AddUmAno.setText(_translate("JanelaEditaMatricula", "ADICIONAR (Plano Anual)1 ano"))
        self.label_2.setText(_translate("JanelaEditaMatricula", "CONTATO ALUNO(A):"))
