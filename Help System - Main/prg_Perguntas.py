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
perguntaList = [];

def CadastraPergunta(ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, config):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("INSERT INTO helpsystem.TB_PERGUNTAS(ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA) "
                "VALUES (%s, %s, %s, %s, %s)")
        data_Uusuario = (ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, datetime.now().date())

        cursor.execute(query, data_Uusuario)
        #print(cursor.lastrowid)
        #return cursor.lastrowid

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

def CadastraResposta(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, config):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("INSERT INTO helpsystem.TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA) "
                 "VALUES (%s, %s, %s, %s, %s)")
        data_Uusuario = (ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA,
                         STR_RESPOSTA, datetime.now().date())

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

def ConsultaPergunta(ID_PERGUNTA, config):
    global UserID;
    global perguntaList;

    UserID = 0;

    try:
        cnx = mysql.connector.connect(**config);
        cursor = cnx.cursor();

        query = ("SELECT ID_PERGUNTA, ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA FROM helpsystem.TB_PERGUNTAS "
                "WHERE ID_PERGUNTA = " + str(ID_PERGUNTA) );

        cursor.execute(query);
        perguntaList = cursor.fetchall();
        print("Total number of rows in table: ", cursor.rowcount);
        print(query);
        for (ID_PERGUNTA, ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA) in perguntaList:
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

def SelecionaRespostas(ID_PERGUNTA, config):
    global UserID
    global perguntaList

    UserID = 0

    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("SELECT ID_RESPOSTA, ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA FROM helpsystem.TB_RESPOSTAS "
                 "WHERE ID_PERGUNTA = " + str(ID_PERGUNTA))

        cursor.execute(query)
        perguntaList = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        lista_str = []
        print(query)
        for (ID_RESPOSTA, ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA) in perguntaList:
            UserID = ID_USER
            #print("{}, {}, {}, {}, {} date {:%d %b %Y}".format(
                #ID_RESPOSTA, ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA))
            lista_str.append("*{}* \n{}".format(ID_RESPOSTA, STR_RESPOSTA))

        return lista_str

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor.close()
        cnx.commit()
        cnx.close()

def AtualizaPergunta(ID_PERGUNTA, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, config):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("UPDATE helpsystem.TB_PERGUNTAS SET " 
                    "STR_TITULO = %s," 
                    "STR_PERGUNTA = %s," 
                    "FLAG_RESOLVIDO = %s, "
                    "DT_PERGUNTA = %s"
                "WHERE ID_PERGUNTA = %s")
        data_Uusuario = (STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, datetime.now().date(), ID_PERGUNTA)

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

def AtualizaPerguntaResolvido(ID_PERGUNTA, FLAG_RESOLVIDO, config):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("UPDATE helpsystem.TB_PERGUNTAS SET " 
                    "FLAG_RESOLVIDO = %s, "
                    "DT_PERGUNTA = %s"
                "WHERE ID_PERGUNTA = %s")
        data_Uusuario = (FLAG_RESOLVIDO, datetime.now().date(), ID_PERGUNTA)

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

def ListaPerguntas(config):
    global QuestionID
    global perguntaList;

    QuestionID = 0
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("SELECT ID_PERGUNTA, ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA FROM helpsystem.TB_PERGUNTAS ")

        cursor.execute(query)
        records = cursor.fetchall()
        perguntaList = records
        lista_str = []
        print("Total number of rows in table: ", cursor.rowcount)
        for (ID_PERGUNTA, ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA) in records:
            QuestionID = ID_PERGUNTA;
            #print("{}, {}, {}, {}, {} data {:%d %b %Y}".format(
                #ID_PERGUNTA, ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA))
            lista_str.append("*{}* \n{}".format(ID_PERGUNTA, STR_PERGUNTA))

        return lista_str
            
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor.close()
        cnx.commit()
        cnx.close()


"""
#Execu~coes
ConsultaPergunta(2, dbconfig);


AtualizaPergunta(2, "De quem é a famosa frase “Penso, logo existo”?", 
"a) Platão"
"b) Galileu Galilei"
"c) Descartes"
"d) Sócrates"
"e) Francis Bacon, None was hired on 12 Dec 2022)",False, dbconfig);


AtualizaPerguntaResolvido(2,0, dbconfig);


ListaPerguntas(dbconfig);
"""
#CadastraPergunta(1, "", "Pergunta Teste 2", False, dbconfig);

