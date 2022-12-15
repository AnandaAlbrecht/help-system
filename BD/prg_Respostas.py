import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

dbconfig = {
    'user': 'apphelpsystem',
    'password': 'YOngAJXjQANWcTWZPT',
    'host': 'helpsystem2.c05e29wh3fvj.us-east-1.rds.amazonaws.com',
    'database': 'helpsystem',
    'raise_on_warnings': True
}

#Variáveis Globais
UserID = 0;
respostasList = [];

def CadastraResposta(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, config):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("INSERT INTO TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA) "
                "VALUES (%s, %s, %s, %s, %s)")
        data_Uusuario = (ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, datetime.now().date())

        cursor.execute(query, data_Uusuario)
        print(cursor.lastrowid)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.commit()
        cnx.close()


def ConsultaResposta(ID_PERGUNTA, config):
    global UserID;
    global perguntaList;

    UserID = 0;

    try:
        cnx = mysql.connector.connect(**config);
        cursor = cnx.cursor();

        query = ("SELECT ID_RESPOSTA, ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA FROM helpsystem.TB_RESPOSTAS "
                "WHERE ID_PERGUNTA = " + str(ID_PERGUNTA) );

        cursor.execute(query);
        respostasList = cursor.fetchall();
        print("Total number of rows in table: ", cursor.rowcount);
        print(query);
        for (ID_PERGUNTA, ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA) in respostasList:
            UserID = ID_USER;
            print("{}, {}, {}, {}, {} was hired on {:%d %b %Y}".format(ID_PERGUNTA, ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA));
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password");
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist");
        else:
            print(err);
    else:
        cursor.close();
        cnx.commit();
        cnx.close();



def AtualizaResposta(ID_RESPOSTA, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, config):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("UPDATE helpsystem.TB_RESPOSTAS SET " 
                    "FLAG_MELHOR_RESPOSTA = %s," 
                    "STR_RESPOSTA = %s," 
                    "DT_RESPOSTA = %s"
                "WHERE ID_RESPOSTA = %s")
        data_Uusuario = (FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, datetime.now().date(), ID_RESPOSTA)

        cursor.execute(query, data_Uusuario)
        print(cursor.lastrowid)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.commit()
        cnx.close()

def AtualizaRespostaMelhor(ID_RESPOSTA, FLAG_MELHOR_RESPOSTA, config):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("UPDATE helpsystem.TB_RESPOSTAS SET " 
                    "FLAG_MELHOR_RESPOSTA = %s," 
                    "DT_RESPOSTA = %s"
                "WHERE ID_RESPOSTA = %s")
        data_Uusuario = (FLAG_MELHOR_RESPOSTA, datetime.now().date(), ID_RESPOSTA)

        cursor.execute(query, data_Uusuario)
        print(cursor.lastrowid)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.commit()
        cnx.close()


def ConsultaRespostaLista(config):
    global UserID;
    global perguntaList;

    UserID = 0;

    try:
        cnx = mysql.connector.connect(**config);
        cursor = cnx.cursor();

        query = ("SELECT ID_RESPOSTA, ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA FROM helpsystem.TB_RESPOSTAS ");

        cursor.execute(query);
        respostasList = cursor.fetchall();
        print("Total number of rows in table: ", cursor.rowcount);
        for (ID_PERGUNTA, ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA) in respostasList:
            UserID = ID_USER;
            print("{}, {}, {}, {}, {} was hired on {:%d %b %Y}".format(ID_PERGUNTA, ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA));
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password");
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist");
        else:
            print(err);
    else:
        cursor.close();
        cnx.commit();
        cnx.close();


#exemplo de uso

CadastraResposta(2, 2, 0, 'Teste resposta do cadastro', dbconfig);

ConsultaResposta(2, dbconfig);

AtualizaResposta(14, 0, '1Teste resposta do cadastro', dbconfig);

AtualizaRespostaMelhor(14,1, dbconfig);

ConsultaRespostaLista(dbconfig);
  
