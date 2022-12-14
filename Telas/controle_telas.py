from PyQt5 import QtWidgets, uic

def fecha_tela(id_tela_anterior):
    if(id_tela_anterior == 1):
        tela_login.close()
    elif(id_tela_anterior == 2):
        tela_home.close()
    elif(id_tela_anterior == 3):
        tela_new_user.close()
    elif(id_tela_anterior == 4):
        tela_question.close()
    elif(id_tela_anterior == 5):
        tela_answers.close()

def chama_telaQuestion(id_tela_anterior):
    fecha_tela(id_tela_anterior)
    tela_question.show()


def chama_telaAnswers(id_tela_anterior):
    fecha_tela(id_tela_anterior)
    tela_answers.show()


def chama_telaLogin(id_tela_anterior):
    fecha_tela(id_tela_anterior)
    tela_login.show()


def chama_telaHome(id_tela_anterior):
    fecha_tela(id_tela_anterior)
    tela_home.show()


def chama_telaNewUser(id_tela_anterior):
    fecha_tela(id_tela_anterior)
    tela_new_user.show()


# id telas:
# login: 1
# home: 2
# new user: 3
# question: 4
# answers: 5

app = QtWidgets.QApplication([])

#tela login - primeira tela
tela_login = uic.loadUi("login.ui")

#tela home só aparece depois do login
tela_home = uic.loadUi("home.ui")

#tela new user
tela_new_user = uic.loadUi("new_user.ui")

#tela question
tela_question = uic.loadUi("question.ui")

#tela answers
tela_answers = uic.loadUi("answers.ui")

tela_login.button_enviar.clicked.connect(chama_telaHome(1))
tela_login.button_novo_cadastro.connect(chama_telaNewUser(1))

tela_home.button_nova_pergunta.clicked.connect(chama_telaQuestion(2))
tela_home.button_sair.clicked.connect(chama_telaLogin(2))

tela_new_user.button_cadastrar.clicked.connect(chama_telaLogin(3))
tela_new_user.button_cancelar.clicked.connect(chama_telaLogin(3))

tela_question.button_voltar.clicked.connect(chama_telaHome(4))
tela_question.button_perguntar.clicked.connect(chama_telaAnswers(4))

tela_answers.button_voltar.clicked.connect(chama_telaQuestion(5))
tela_answers.button_responder.clicked.connect(chama_telaAnswers(5))

tela_login.show()
app.exec()