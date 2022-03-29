from venv import main
from pandas.core import api
import mysql.connector
from twitterSearch import buscarTweets
# Função para criar database
def createdb(dbname, cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS {};".format(dbname))
    except mysql.connector.Error as err:
            print("Erro ao criar banco de dados: {};".format(err))
# Função para criar tabela
def createTable(tbname, table_structure, cursor):
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS {}({});".format(tbname,table_structure))
    except mysql.connector.Error as err:
            print("Erro ao criar tabela: {}".format(err))
# Função para inserir dados
def insertValues(tbname,data,cursor):
    try:
        cursor.execute("INSERT INTO {} VALUES({});".format(tbname,data))
    except mysql.connector.Error as err:
        print("Erro ao inserir dados: {}".format(err))
# Função ara deletar valores
def deleteValues(tbname,deleting,cursor):
    try:
        print(cursor.execute("SELECT * FROM {} WHERE idt={};".format(tbname,deleting)))
        confirm = int(input("\nVocê confirma a exclusão dos dados acima?\n 1 - Sim | 2 - Não"))
        if confirm==1:
            cursor.execute("DELETE FROM {} WHERE idt={}".format(tbname,deleting))
        elif confirm==2:
            pass
        else:
            print("Opção inválida")
    except mysql.connector.Error as err:
        print("Erro ao deletar dados: {}".format(err))
    except TypeError as err:
        print("Valor inválido digitado.")
# Funçã para buscar dados (NÃO IMPLEMENTADO)
def searchValues(tbname, index, cursor):
    try:
        pass
    except mysql.connector.Error as err:
        print("Erro na operação: {}".format(err))
# Funções 'main' abaixo estão sendo utilizadas para finalidade de testes, serão removidos na versão final
if __name__ == '__main__':
    cnx = mysql.connector.connect(user='****', password='********', host='127.0.0.1', database='twitterdb')
    # Criando banco de dados e cursor para operações
    cursor = cnx.cursor()
    dbname = "twitterdb"
    # Criando db
    table_structure = "'idt' INT NOT NULL AUTO_INCREMENT,'hora-tweet' DATETIME NOT NULL, 'conteudo' VARCHAR(255) NOT NULL, 'opiniao' ENUM('P','N') NOT NULL, 'regiao' VARCHAR(255), PRIMARY KEY(idt)"
    createdb(dbname,cursor)
    # Criando tabela
    tbname="Tweets"
    createTable(tbname, table_structure,cursor)
    # Inserindo dados
    data = "..." # aqui chamaremos a função buscarTweets, após filtrar o conteúdo
    insertValues(tbname,data,cursor)
    cnx.close()