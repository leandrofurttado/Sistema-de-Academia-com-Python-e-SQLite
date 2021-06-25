from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QFrame
from PyQt5 import QtGui
from cadastro_design import *
from datetime import datetime, date, timedelta
from painel import *
from janela1_login import *
from design_listagem import *
from design_editamatricula import *
import sys
import sqlite3



class CadastroClientes(QMainWindow, Ui_Janela1):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.janela2 = Painel()
        self.label_logo.setPixmap(QtGui.QPixmap('icons/logoacademia1.png'))
        self.button_login.setIcon(QtGui.QIcon('icons/login.png'))
        self.button_login.setIconSize(QtCore.QSize(30,30))
        self.button_login.clicked.connect(self.login)


    def login(self):
        self.conectar = sqlite3.connect('contas_admin.db')
        self.cursor = self.conectar.cursor()
        self.cursor.execute('SELECT * FROM contas')
        for conta in self.cursor.fetchall():
            id, usuario, senha, nome_cliente = conta
            if self.input_usuario.text() == usuario and self.input_Senha.text() == senha:
                self.label_Error.setStyleSheet("color: green ; font: 16pt \"Bahnschrift SemiLight Condensed\";")
                self.label_Error.setText('LOGADO!')
                with open('sv.txt', 'w+') as Arquivo:
                    Arquivo.write(self.input_usuario.text())
                self.janela2.show()
                self.hide()
            else:
                self.label_Error.setStyleSheet("color: red ; font: 16pt \"Bahnschrift SemiLight Condensed\";")
                self.label_Error.setText('ERRO! CONTA ADMIN NÃO ESTÁ NO BANCO DE DADOS.')
        self.cursor.close()
        self.conectar.close()

class Painel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.painel = Ui_Janela2()
        self.painel.setupUi(self)
        self.janela_cadastro = Cadastro()
        self.janela_listagem = Lista()
        self.painel.buttton_verAlunos.setIcon(QtGui.QIcon('icons/verAlunos.png'))
        self.painel.buttton_verAlunos.setIconSize(QtCore.QSize(40, 40))
        self.painel.button_Cadastro.setIcon(QtGui.QIcon('icons/cadastroGym.png'))
        self.painel.button_Cadastro.setIconSize(QtCore.QSize(40, 40))
        self.painel.actionAzul.triggered.connect(self.menu_azul)
        self.painel.actionPreto.triggered.connect(self.menu_preto)
        self.painel.actionAmarelo.triggered.connect(self.menu_amarelo)
        self.painel.actionVermelho.triggered.connect(self.menu_vermelho)
        self.painel.button_Cadastro.clicked.connect(self.novajanela_cadastro)
        self.painel.buttton_verAlunos.clicked.connect(self.novajanela_listagem)

        data = datetime.now()
        self.painel.label_dia1.setText(f'HOJE É: {data.strftime("%d/%m/%Y -->Logou em: %H:%M:%S")}')

        with open('sv.txt', 'r+') as Arquivo:
            conector = sqlite3.connect('contas_admin.db')
            cursor = conector.cursor()
            nome = Arquivo.readline()
            cursor.execute(f'SELECT * FROM contas WHERE usuario=?', (nome,))
            for linha in cursor.fetchall():
                id, usuario, senha, nome_cliente = linha
                self.painel.label_boasVindas.setText(f'BEM-VINDO, {nome_cliente}!')
            cursor.close()
            conector.close()

    #FUNCTIONS:

    #MENU DE CORES:####################################################################
    def menu_preto(self):
        self.painel.centralwidget.setStyleSheet("background-color: rgb(28, 28, 28);")
    def menu_vermelho(self):
        self.painel.centralwidget.setStyleSheet("background-color: rgb(139, 0, 0);")
    def menu_amarelo(self):
        self.painel.centralwidget.setStyleSheet("background-color: rgb(255, 215, 0);")
    def menu_azul(self):
        self.painel.centralwidget.setStyleSheet("background-color: rgb(65, 105, 225);")
    ###################################################################################

    def novajanela_cadastro(self):
        self.janela_cadastro.show()

    def novajanela_listagem(self):
        self.janela_listagem.show()


class Cadastro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cadastro = Ui_Cadastro3()
        self.cadastro.setupUi(self)
        self.cadastro.button_cadastrar.clicked.connect(self.cadastrarFull)


    def cadastrarFull(self):
        self.conectar = sqlite3.connect('clientes.db')
        self.cursor = self.conectar.cursor()

        if self.cadastro.inputbox_Planos.currentText() == 'Plano Anual R$75,00 (365 dias)':
            self.inicio = date.today()
            vencimento = self.inicio + timedelta(days=365)
            self.data_vencimento = vencimento.strftime("%d/%m/%Y")

        elif self.cadastro.inputbox_Planos.currentText() == 'Plano Trimensal R$100,00 (90 dias)':
            self.inicio = date.today()
            vencimento = self.inicio + timedelta(days= 90)
            self.data_vencimento = vencimento.strftime("%d/%m/%Y")

        elif self.cadastro.inputbox_Planos.currentText() == 'Plano Mensal R$125,00  (30 dias)':
            self.inicio = date.today()
            vencimento = self.inicio + timedelta(days=30)
            self.data_vencimento = vencimento.strftime("%d/%m/%Y")
        #ADICIONANDO O NOME

        try:
            self.cursor.execute('INSERT INTO clientes (nome, telefone, plano, data_nascimento, inicio_ativ, endereco, vencimento) '
                                'VALUES (?, ?, ?, ?, ?, ?, ?)',
                                (f"{self.cadastro.input_NomeCompleto.text()}", f"{self.cadastro.input_Telefone.text()}",
                                 f"{self.cadastro.inputbox_Planos.currentText()}", f"{self.cadastro.input_DataNasc.text()}",
                                 f"{self.inicio}", f"{self.cadastro.input_endereco.text()}",
                                 f"{self.data_vencimento}"))
            self.cadastro.label_Erros.setStyleSheet('color: green')
            self.cadastro.label_Erros.setText(f'ALUNO(A) CADASTRADO COM SUCESSO!')
            self.conectar.commit()
            self.cadastro.input_Telefone.clear()
            self.cadastro.input_NomeCompleto.clear()
            self.cadastro.input_endereco.clear()
        except Exception as error:
            self.cadastro.label_Erros.setStyleSheet('color: red')
            self.cadastro.label_Erros.setText(f'ERRO ENCONTRADO! Tente trocar o número de TEL!')

        self.cursor.close()
        self.conectar.close()



class Lista(QMainWindow):
    def __init__(self):
        super().__init__()
        self.listagem = Ui_JanelaListagem()
        self.listagem.setupUi(self)
        self.editaMatricula = Editar()
        self.listagem.button_ShowAll.clicked.connect(self.listagem_alunos)
        self.listagem.button_pesquisaNome.clicked.connect(self.pesquisaAlunoNome)
        self.listagem.button_PesquisaNumero.clicked.connect(self.pesquisaAlunoNumero)
        self.listagem.button_Vencimentos.clicked.connect(self.listagemVencimento)
        self.listagem.button_AdicionarPlano.clicked.connect(self.editaMatricula.show)

    def listagem_alunos(self):
        self.conectar = sqlite3.connect('clientes.db')
        self.cursor = self.conectar.cursor()

        self.cursor.execute('SELECT * FROM clientes')
        lista = self.cursor.fetchall()
        self.listagem.lista_de_alunos.clear()
        for aluno in lista:
            formatacao = f'◄INSCRIÇÃO:{aluno[0]}► •NOME► |{aluno[1]}|,  •PLANO► |{aluno[3]}|,  •TELEFONE► |{aluno[2]}|,  •ENDEREÇO► |{aluno[6]}|' \
                         f',  •DATA VENCIMENTO► |{aluno[7]}|'
            self.listagem.lista_de_alunos.addItem(formatacao)

        self.cursor.close()
        self.conectar.close()

    def pesquisaAlunoNome(self):
        self.conectar = sqlite3.connect('clientes.db')
        self.cursor = self.conectar.cursor()
        pesquisa = self.listagem.input_NomePesquisa.text()
        self.listagem.lista_de_alunos.clear()
        self.cursor.execute(f'SELECT * FROM clientes')
        lista = self.cursor.fetchall()
        for aluno in lista:
            if pesquisa in aluno[1]:
                formatacao = f'◄INSCRIÇÃO:{aluno[0]}► •NOME► |{aluno[1]}|,  •PLANO► |{aluno[3]}|,  •TELEFONE► |{aluno[2]}|,  •ENDEREÇO► |{aluno[6]}|' \
                             f',  •DATA VENCIMENTO► |{aluno[7]}|'
                self.listagem.lista_de_alunos.addItem(formatacao)

        self.listagem.input_NomePesquisa.clear()
        self.cursor.close()
        self.conectar.close()

    def pesquisaAlunoNumero(self):
        self.conectar = sqlite3.connect('clientes.db')
        self.cursor = self.conectar.cursor()
        pesquisa = self.listagem.input_NumeroTelefonepesquisa.text()
        self.listagem.lista_de_alunos.clear()
        self.cursor.execute(f'SELECT * FROM clientes WHERE telefone=?', (pesquisa, ))
        lista = self.cursor.fetchall()
        if lista == []:
            self.listagem.label_Erros.setText('NÃO ENCONTRADO! TENTE PELO NOME COMPLETO E CERTO DO ALUNO!')
        else:
            for aluno in lista:
                formatacao = f'◄INSCRIÇÃO:{aluno[0]}► •NOME► |{aluno[1]}|,  •PLANO► |{aluno[3]}|,  •TELEFONE► |{aluno[2]}|,  •ENDEREÇO► |{aluno[6]}|' \
                             f',  •DATA VENCIMENTO► |{aluno[7]}|'
                self.listagem.lista_de_alunos.addItem(formatacao)
        self.listagem.input_NumeroTelefonepesquisa.clear()
        self.cursor.close()
        self.conectar.close()


    def listagemVencimento(self):
        self.conectar = sqlite3.connect('clientes.db')
        self.cursor = self.conectar.cursor()
        self.listagem.lista_de_alunos.clear()
        hoje = date.today().strftime("%d/%m/%Y")

        self.cursor.execute(f'SELECT * FROM clientes')
        todos_clientes = self.cursor.fetchall()

        for aluno in todos_clientes:
            data_hoje = datetime.strptime(hoje, '%d/%m/%Y')
            data_vencimento = datetime.strptime(aluno[7], '%d/%m/%Y')
            if abs(data_vencimento-data_hoje).days < 10:
                formatacao = f'◄INSCRIÇÃO:{aluno[0]}►•NOME► |{aluno[1]}|,  •PLANO► |{aluno[3]}|,  •TELEFONE► |{aluno[2]}|,  •ENDEREÇO► |{aluno[6]}|' \
                             f',  •DATA VENCIMENTO► |{aluno[7]}|{abs(data_vencimento-data_hoje).days} dias para vencer'
                self.listagem.lista_de_alunos.addItem(formatacao)

        self.cursor.close()
        self.conectar.close()

class Editar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.editagem = Ui_JanelaEditaMatricula()
        self.editagem.setupUi(self)
        self.editagem.button_AddTrinta.clicked.connect(self.add30)
        self.editagem.button_AddNoventa.clicked.connect(self.add90)
        self.editagem.button_AddUmAno.clicked.connect(self.add1year)
        self.editagem.button_DeletaMatricula.clicked.connect(self.removeMatricula)

    def add30(self):
        try:
            self.conectar = sqlite3.connect('clientes.db')
            self.cursor = self.conectar.cursor()
            self.id_matricula = self.editagem.input_id.text()
            self.contato_matricula = self.editagem.input_ContatoEdita.text()
            plano1 = 'Plano Mensal R$125,00  (30 dias)'

            #GERANDO 30 DIAS E ADICIONANDO NA VARIAVEL DATA_VENCIMENTO.

            self.hoje1 = date.today()
            vencimento1 = self.hoje1 + timedelta(days=30)
            self.data_vencimento1 = vencimento1.strftime("%d/%m/%Y")

            self.cursor.execute('UPDATE clientes SET plano=?, telefone=?, vencimento=? WHERE id= ?',
                                (plano1, self.contato_matricula, self.data_vencimento1, self.id_matricula))
            self.conectar.commit()

            self.editagem.label_Erros.setStyleSheet('color: green')
            self.editagem.label_Erros.setText('Telefone e Vencimento adicionado com sucesso!')
            self.cursor.close()
            self.conectar.close()
        except Exception as error:
            self.editagem.label_Erros.setStyleSheet('Color: red')
            self.editagem.label_Erros.setText('OCORREU UM ERRO! PREENCHA CORRETAMENTE OS 2 CAMPOS')


    def add90(self):
        try:
            self.conectar = sqlite3.connect('clientes.db')
            self.cursor = self.conectar.cursor()
            self.id_matricula = self.editagem.input_id.text()
            self.contato_matricula = self.editagem.input_ContatoEdita.text()
            plano2 = 'Plano Trimensal R$100,00 (90 dias)'

            #GERANDO 30 DIAS E ADICIONANDO NA VARIAVEL DATA_VENCIMENTO.

            self.hoje1 = date.today()
            vencimento1 = self.hoje1 + timedelta(days=90)
            self.data_vencimento1 = vencimento1.strftime("%d/%m/%Y")

            self.cursor.execute('UPDATE clientes SET plano=?, telefone=?, vencimento=? WHERE id= ?',
                                (plano2, self.contato_matricula, self.data_vencimento1, self.id_matricula))
            self.conectar.commit()

            self.editagem.label_Erros.setStyleSheet('color: green')
            self.editagem.label_Erros.setText('Telefone e Vencimento adicionado com sucesso!')
            self.cursor.close()
            self.conectar.close()

        except Exception as error:
            self.editagem.label_Erros.setStyleSheet('Color: red')
            self.editagem.label_Erros.setText('OCORREU UM ERRO! PREENCHA CORRETAMENTE OS 2 CAMPOS')


    def add1year(self):
        try:
            self.conectar = sqlite3.connect('clientes.db')
            self.cursor = self.conectar.cursor()
            self.id_matricula = self.editagem.input_id.text()
            self.contato_matricula = self.editagem.input_ContatoEdita.text()
            plano3 = 'Plano Anual R$75,00 (365 dias)'

            #GERANDO 30 DIAS E ADICIONANDO NA VARIAVEL DATA_VENCIMENTO.

            self.hoje1 = date.today()
            vencimento1 = self.hoje1 + timedelta(days=365)
            self.data_vencimento1 = vencimento1.strftime("%d/%m/%Y")

            self.cursor.execute('UPDATE clientes SET plano=?, telefone=?, vencimento=? WHERE id= ?',
                                (plano3, self.contato_matricula, self.data_vencimento1, self.id_matricula))
            self.conectar.commit()

            self.editagem.label_Erros.setStyleSheet('color: green')
            self.editagem.label_Erros.setText('Telefone e Vencimento adicionado com sucesso!')
            self.cursor.close()
            self.conectar.close()

        except Exception as error:
            self.editagem.label_Erros.setStyleSheet('Color: red')
            self.editagem.label_Erros.setText('OCORREU UM ERRO! PREENCHA CORRETAMENTE OS 2 CAMPOS')


    def removeMatricula(self):
        try:
            self.conectar = sqlite3.connect('clientes.db')
            self.cursor = self.conectar.cursor()
            id_cliente_delete = self.editagem.input_id.text()
            self.cursor.execute('DELETE FROM clientes WHERE id=?', (id_cliente_delete,))
            self.conectar.commit()
            self.editagem.label_Erros.setStyleSheet('color: green')
            self.editagem.label_Erros.setText('ALUNO(A) REMOVIDO COM SUCESSO!')


            self.cursor.close()
            self.conectar.close()
        except Exception as errorr:
            self.editagem.label_Erros.setStyleSheet('color: red')
            self.editagem.label_Erros.setText('ERRO! Nº MATRICULA NÃO EXISTE.')

if __name__ == '__main__':
    start = QApplication(sys.argv)
    app = CadastroClientes()
    app.show()
    start.exec_()