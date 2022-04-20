from venv import main
from pandas.core import api
import mysql.connector
from twitterSearch import buscarTweets
# Função para criar database, caso não tenha sido criada ainda
def createdb(dbname, cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS {};".format(dbname))
    except mysql.connector.Error as err:
            print("Erro ao criar banco de dados: {};".format(err))
# Função para criar tabela, caso também não tenha sido criada
def createTable(tbname, table_structure, cursor):
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS {}({});".format(tbname,table_structure))
    except mysql.connector.Error as err:
            print("Erro ao criar tabela: {}".format(err))
# Função para inserir dados
def insertValues(tbname,data,cursor):
    try:
        # colunas: idt (pk, auto_increment, not null)| tweets(not null) | numLikes(not null) | data(not null) | regiao (FK, not null) | favoreceCandidato(not null)
        cursor.execute("INSERT INTO {} VALUES({});".format(tbname,data))
    except mysql.connector.Error as err:
        print("Erro ao inserir dados: {}".format(err))
# Função para deletar valores
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
# Função para buscar dados, a maneira utilizada para pesquisa é uma query padrão do sql, porém exige conhecimento do BD o que invalida a utilização pelo usuário, necessita de aperfeiçoamento
def searchValues(tbname, sqlCondition, cursor):
    try:
        cursor.execute("SELECT * FROM {} WHERE {}".format(tbname, sqlCondition))
        result = cursor.fetchall()
        for i in result:
            print(i)
    except mysql.connector.Error as err:
        print("Erro na operação: {}".format(err))
# Função para testar conexão
def testConnect(tbname,cursor):
    cursor.execute("SELECT * FROM {}".format(tbname))
    result = cursor.fetchall()
    for i in result:
        print(i)