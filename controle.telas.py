from PyQt5 import QtWidgets, uic

def chama_telaQuestion():
    tela_question.show()

def chama_telaLogin():
    tela_login.show()

app = QtWidgets.QApplication([])
home = uic.loadUi("home.ui")
home.button_nova_pergunta.clicked.connect(chama_telaQuestion)
tela_question = uic.loadUi("question.ui")
home.button_sair.clicked.connect(chama_telaLogin)
tela_login = uic.loadUi("login.ui")


home.show()
app.exec()