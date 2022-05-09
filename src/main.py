# Mesmo importanto o mysql connector no dbConnector precisamos importar aqui também para criar a conexão
import mysql.connector
from twitterSearch import buscarTweets
import dbConnector
# Primeiro é necessário pegar as informações do nosso estimado banco de dados, juntamente de seu usuário credenciado.
with open('./keys/sql_info.txt', 'r') as tfile:
        user = tfile.readline().strip("\n")
        password = tfile.readline().strip("\n")
        host = tfile.readline().strip("\n")
        database = tfile.readline().strip("\n")
        tbname = tfile.readline().strip("\n")
# Também iremos autenticar a nossa API utilizando as nossas keys
# obs: estamos autenticando todas as funções de maneira externa por questões de segurança, as autenticações serão feitas ao chamar a função e não dentro da mesma
with open('./keys/twitter-tokens.txt', 'r') as ttfile:
    access_token = ttfile.readline().strip("\n")
    access_token_secret = ttfile.readline().strip("\n")
    consumer_key = ttfile.readline().strip("\n")
    consumer_secret = ttfile.readline().strip("\n")
# Criando a conexão
cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
# Criando cursor para operação
cursor = cnx.cursor()
# Definindo qual o critério que a API irá utilizar para varrer
search_for="#forabolsonaro"
print(buscarTweets(search_for,15,consumer_key,consumer_secret,access_token,access_token_secret))# Testando
# Sempre fechando a conexão com o BD após as operações
cnx.close()