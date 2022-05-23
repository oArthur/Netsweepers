from twitterSearch import buscarTweets
from ..database.connection import Connection
from dotenv import load_dotenv
import os

# Obter cursor
cursor = Connection().getCursor()

# ENV load
load_dotenv('../.env')

# Também iremos autenticar a nossa API utilizando as nossas keys
# obs: estamos autenticando todas as funções de maneira externa por questões de segurança, as autenticações serão feitas ao chamar a função e não dentro da mesma
access_token = os.environ.get('TT_TOKEN')
access_token_secret = os.environ.get('TT_TOKEN_SECRET')
consumer_key = os.environ.get('TT_CONSUME_KEY')
consumer_secret = os.environ.get('TT_CONSUME_SECRET')
# Definindo qual o critério que a API irá utilizar para varrer
search_for="#LulaPresidente"
print(buscarTweets(search_for,15,consumer_key,consumer_secret,access_token,access_token_secret))# Testando