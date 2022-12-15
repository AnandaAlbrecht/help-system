from PyQt5 import QtWidgets, uic
from prg_Users import *
from prg_Perguntas import *

def fecha_tela(id_tela_anterior):
    if (id_tela_anterior == 1):
        tela_login.line_edit_login.clear()
        tela_login.line_edit_senha.clear()
        tela_login.close()
    elif (id_tela_anterior == 2):
        tela_home.line_edit_busca.clear()
        tela_home.close()
    elif (id_tela_anterior == 3):
        tela_new_user.line_edit_novo_login.clear()
        tela_new_user.line_edit_nova_senha.clear()
        tela_new_user.close()
    elif (id_tela_anterior == 4):
        tela_question.text_edit_pergunta.clear()
        tela_question.close()
    elif (id_tela_anterior == 5):
        tela_answers.text_edit_resposta.clear()
        tela_answers.close()


def chama_telaQuestion(id_tela_anterior):
    fecha_tela(id_tela_anterior)
    tela_question.show()


def chama_telaAnswers(id_tela_anterior):
    if(id_tela_anterior == 4):
        envia_pergunta()
    elif(id_tela_anterior == 5):
        envia_resposta()

    pergunta = seleciona_pergunta(tela_home)

    fecha_tela(id_tela_anterior)

    tela_answers.label_pergunta.setText(pergunta)

    tela_answers.show()


def chama_telaLogin(id_tela_anterior, id_acao):
    if(id_acao == 0):
        envia_dados_telaNewUser(tela_new_user)
    fecha_tela(id_tela_anterior)
    tela_login.show()
# id_acao: identifica qual acao foi feita para chegar nessa tela

def chama_telaHome(id_tela_anterior):
    if(id_tela_anterior == 1):
        envia_dados_telaLogin(tela_login)
    
    tela_home.list_view_perguntas.clear()
    # Recuperação dos dados do BD
    entries = ListaPerguntas(dbconfig)
    tela_home.list_view_perguntas.addItems(entries)

    fecha_tela(id_tela_anterior)
    tela_home.show()


def chama_telaNewUser(id_tela_anterior):
    fecha_tela(id_tela_anterior)
    tela_new_user.show()


#funcoes para enviar e armazenar os dados das telas

def envia_dados_telaLogin(self):
    login = self.line_edit_login.text()
    senha = self.line_edit_senha.text()
    print("Login: ", login)
    print("Senha: ", senha)

def envia_dados_telaNewUser(self):
    novo_login = self.line_edit_novo_login.text()
    nova_senha = self.line_edit_nova_senha.text()
    print("Novo login: ", novo_login)
    print("Nova senha: ", nova_senha)

def busca_pergunta(self):
    pergunta = self.line_edit_busca.text()
    print(pergunta)
    self.line_edit_busca.clear()

def envia_pergunta():
    pergunta = tela_question.text_edit_pergunta.toPlainText()
    print(pergunta)

def envia_resposta():
    resposta = tela_answers.text_edit_resposta.toPlainText()
    print(resposta)

def seleciona_pergunta(self):
    pergunta = self.list_view_perguntas.currentItem().text()
    print(pergunta)
    return pergunta

# id telas:
# login: 1
# home: 2
# new user: 3
# question: 4
# answers: 5

app = QtWidgets.QApplication([])

#tela login - primeira tela
tela_login = uic.loadUi("login.ui")
tela_login.setFixedSize(1024, 800)

#tela home só aparece depois do login
tela_home = uic.loadUi("home.ui")
tela_home.setFixedSize(1024, 800)

#tela new user
tela_new_user = uic.loadUi("new_user.ui")
tela_new_user.setFixedSize(1024, 800)

#tela question
tela_question = uic.loadUi("question.ui")
tela_question.setFixedSize(1024, 800)

#tela answers
tela_answers = uic.loadUi("answers.ui")
tela_answers.setFixedSize(1024, 800)


tela_login.line_edit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
tela_login.button_enviar.clicked.connect(lambda: chama_telaHome(1))
tela_login.button_novo_cadastro.clicked.connect(lambda: chama_telaNewUser(1))

tela_home.button_nova_pergunta.clicked.connect(lambda: chama_telaQuestion(2))
tela_home.button_sair.clicked.connect(lambda: chama_telaLogin(2, 1))
#id_acao == 1 para o botao de voltar
tela_home.line_edit_busca.returnPressed.connect(lambda: busca_pergunta(tela_home))
tela_home.list_view_perguntas.itemDoubleClicked.connect(lambda: chama_telaAnswers(2))


tela_new_user.button_cadastrar.clicked.connect(lambda: chama_telaLogin(3, 0))
#id_acao == 0 para o botao de cadastrar
tela_new_user.button_cancelar.clicked.connect(lambda: chama_telaLogin(3, 1))
#id_acao == 1 para o botao de voltar

tela_question.button_voltar.clicked.connect(lambda: chama_telaHome(4))
tela_question.button_perguntar.clicked.connect(lambda: chama_telaAnswers(4))

tela_answers.button_voltar.clicked.connect(lambda: chama_telaHome(5))
tela_answers.button_responder.clicked.connect(lambda: chama_telaAnswers(5))

tela_login.show()
app.exec()