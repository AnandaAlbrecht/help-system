from PyQt5 import QtWidgets, uic


def chama_telaQuestion():
    tela_question.show()


def chama_telaLogin():
    tela_login.show()


def chama_telaHome():
    tela_home.show()


app = QtWidgets.QApplication([])

#tela login - primeira tela
tela_login = uic.loadUi("login.ui")
tela_login.button_enviar.clicked.connect(chama_telaHome)

#tela Home só aparece depois do login
tela_home = uic.loadUi("home.ui")
tela_home.button_nova_pergunta.clicked.connect(chama_telaQuestion)
tela_home.button_sair.clicked.connect(chama_telaLogin)

tela_question = uic.loadUi("question.ui")

tela_login.show()
app.exec()
