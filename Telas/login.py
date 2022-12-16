from PyQt5 import QtWidgets, uic
import mysql.connector
from mysql.connector import tabelas

def chama_telaCadastro():
    tela_user.show()


def cadastrar():
    login = tela_user.line_edit_novo_login.text()
    senha = tela_user.line_edit_nova_senha.text()

    if (senha == senha):
        try:
            banco = mysql.connector('TB_USER')
            cursor = banco.cursor()
            cursor.execute("CREAT TABLE IF NOT EXIST cadastro(login text, senha text)")
            cursor.execute("INSERT INTO cadastro VALUES(' "+login+"', '"+senha+"')")

            banco.commit()
            banco.close()
        
        except mysql.error as erro:
            print("Erro ao inserir os dados:", erro)

def chama_telaHome():
     login = tela_user.line_edit_novo_login.text()
     senha = tela_user.line_edit_nova_senha.text()
     banco = mysql.connector('TB_USER')
     cursor = banco.cursor()
     cursor.execute("SELECT senha FROM TB_USER WHERE login ='{}".format(login))
     senha_bd = cursor.fetchall()
     print(senha_bd)

def cancelar():
    tela_user.close()
    tela_login.show

app = QtWidgets.QApplication([])
tela_login = uic.loadUi("login.ui")
tela_user = uic.loadUi("new_user.ui")
tela_home = uic.loadUI("home.ui")

tela_login.button_novo_cadastro.clicked.conected(chama_telaCadastro)
tela_login.button_enviar.clicked.conected(chama_telaHome)
tela_login.line_edit_senha.setEchoMode(QtWidgets.line_edit_senha.Password)
tela_user.button_cadastrar.clicked.conected(cadastrar)
tela_user.button_cancelar.clicked.conected(cancelar)
tela_login.show()
app.exec()