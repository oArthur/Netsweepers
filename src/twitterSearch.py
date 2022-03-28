from venv import main
import tweepy
import pandas as pd

#Pegando as KEYS do arquivo twitter-keys.py e lendo linha a linha. Logo depois realizamos a autenticação.
with open('./src/twitter-tokens.txt', 'r') as tfile:
    access_token = tfile.readline().strip("\n")
    access_token_secret = tfile.readline().strip("\n")
    consumer_key = tfile.readline().strip("\n")
    consumer_secret = tfile.readline().strip("\n")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

'''
Nas variavaies seguintes vamos declarar a quantidade de tweets que vamos buscar e vamos criar as listas para armazenar essas informacoes.
Logo apos, criando o cursor que pegara o metedo user_timeline e passaremos o argumento id que se refere a uma conta do twitter.
ja com o tweet_mode passamos o metodo que iremos querer o tweet neste caso vou usar a extended.'''
def buscarTweets(search_for):
    number_of_tweets = 15
    tweets = []
    likes = []
    time_post = []
    cursor = tweepy.Cursor(api.search_tweets, q=search_for, tweet_mode='extended', result_type='recent', lang='pt').items(number_of_tweets)

    '''Criando um laco de repeticao que ira pegar os tweets, likes e horario do post. Logo depois criamos uma lista com todos esses dados.'''
    for tweet in cursor:
        tweets.append(tweet.full_text)
        likes.append(tweet.favorite_count)
        time_post.append(tweet.created_at)
    df = pd.DataFrame({'tweet': tweets, 'likes': likes, 'time': time_post})
    return df
    #Filtrando tweets, removendo os Retweets.
    """df = df[~df['tweet'].str.contains('RT')]
    df = df.reset_index(drop=True)"""

    #print(df)

    #Escrevendo os tweets em tweets.txt
    '''with open('./src/tweets.txt', 'a', encoding="utf-8") as f:
        for tweets in df['tweet']:
            f.write('Tweet: "'+tweets +'"'+ '\n'*2)
        f.close()'''


# search_for = '#forabolsonaro' Exemplo de pesquisa
if __name__ == '__main__':
    buscarTweets(search_for)