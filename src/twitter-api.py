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
Nas variavaies seguintes vamos declaclarar a quantidade de tweets que vamos buscar e vamos criar as listas para armazenar essas informcoes.
Logo apos, criando o cursor que pegara o metedo user_timeline e passaremos o argumento id que se refere a uma conta do twitter.
ja com o tweet_mode passamos o metodo que iremos querer o tweet neste caso vou usar a extended.'''
def buscarTweets(search_for):
    number_of_tweets = 10
    tweets = []
    likes = []
    time_post = []
    cursor = tweepy.Cursor(api.search_tweets, q=search_for.encode('utf-8'), tweet_mode='extended', result_type='mixed', lang='pt').items(number_of_tweets)

    '''Criando um laco de repeticao que ira pegar os tweets, likes e horario do post. Logo depois criamos uma lista com todos esses dados.'''
    for tweet in cursor:
        tweets.append(tweet.full_text)
        likes.append(tweet.favorite_count)
        time_post.append(tweet.created_at)

    #Criando o DataFrame.
    df = pd.DataFrame({'tweet': tweets, 'likes': likes, 'time': time_post})
    
    #Filtrando tweets, removendo os Retweets.
    """df = df[~df['tweet'].str.contains('RT')]
    df = df.reset_index(drop=True)"""


    #Escrevendo tweets em tweets.csv
    df.to_csv('./src/data_tweets.csv', index=False, mode='a' ,header=False)

    #return df

search_for = '#forabolsonaro'
if __name__ == '__main__':
    buscarTweets(search_for)
    #print(buscarTweets(search_for))

