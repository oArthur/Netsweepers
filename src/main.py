# Mesmo importanto o mysql connector no dbConnector precisamos importar aqui também para criar a conexão
import mysql.connector
from twitterSearch import buscarTweets
import dbConnector
# Primeiro é necessário pegar as informações do nosso estimado banco de dados, juntamente de seu usuário credenciado.
with open('keys/sql_info.txt', 'r') as tfile:
        user = tfile.readline().strip("\n")
        password = tfile.readline().strip("\n")
        host = tfile.readline().strip("\n")
        database = tfile.readline().strip("\n")
        tbname = tfile.readline().strip("\n")
# Também iremos autenticar a nossa API utilizando as nossas keys

# Criando a conexão
'''cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)'''
# Definindo qual o critério que a API irá utilizar para varrer
search_for = "#python"
number_of_tweets = 10
buscarTweets(search_for,number_of_tweets)