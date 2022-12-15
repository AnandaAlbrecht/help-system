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
userList = [];

#Parte do cadastro de user
def CadastraUsuario(STR_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, config):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("INSERT INTO helpsystem.TB_USER(STR_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, DT_ULTIMA_ALTERACAO) "
                "VALUES (%s, %s, %s, %s, %s)")
        data_Uusuario = (STR_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, datetime.now().date())

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

def AtualizaUsuario(ID_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, config):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("UPDATE helpsystem.TB_USER SET " 
                    "STR_NOME_PESSOA = %s," 
                    "STR_EMAIL = %s," 
                    "STR_SENHA = %s, "
                    "DT_ULTIMA_ALTERACAO = %s"
                "WHERE ID_USER = %s")
        data_Uusuario = (STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, datetime.now().date(), ID_USER)

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

def ConsultaUsuario(STR_USER, STR_SENHA, config):
    global UserID;

    UserID = 0;
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("SELECT ID_USER, STR_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, DT_ULTIMA_ALTERACAO FROM helpsystem.TB_USER "
                "WHERE STR_USER = %s AND STR_SENHA = %s")
        data_Uusuario = (STR_USER, STR_SENHA)

        cursor.execute(query, data_Uusuario)
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        for (ID_USER, STR_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, DT_ULTIMA_ALTERACAO) in records:
            UserID = ID_USER;
            print("{}, {}, {}, {} was hired on {:%d %b %Y}".format(STR_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, DT_ULTIMA_ALTERACAO))
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

def ListaUsuario(config):
    global UserID;
    global userList;

    UserID = 0;
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = ("SELECT ID_USER, STR_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, DT_ULTIMA_ALTERACAO FROM helpsystem.TB_USER ")

        cursor.execute(query)
        records = cursor.fetchall()
        userList = records;
        lista_str = []
        print("Total number of rows in table: ", cursor.rowcount)
        for (ID_USER, STR_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, DT_ULTIMA_ALTERACAO) in records:
            UserID = ID_USER;
            print("{}, {}, {}, {} was hired on {:%d %b %Y}".format(STR_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, DT_ULTIMA_ALTERACAO))
            lista_str.append("{}, {}, {}, {} was hired on {:%d %b %Y}".format(STR_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, DT_ULTIMA_ALTERACAO))

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

#CadastraUsuario('user5', 'Nome Pessoa5', 'email4', 'Senha-M4', dbconfig)

ConsultaUsuario('user', 'Senha-M1', dbconfig);
print(UserID);

ListaUsuario(dbconfig)
print(userList)

#AtualizaUsuario(UserID, 'Nome Pessoa1', 'email1', 'Senha-M1', dbconfig)
#

"""