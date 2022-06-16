"""
Este script foi feito para ler e analizar os tweets que o twitterSearch.py vai retornar
-------------------------------------------------------------------------------------------------------------------------------
This script will read and analyze info that twitterSearch.py will return
"""
import re

import pandas as pd
 # Caminho para o csv
# print(dataFrame) para testes
'''
embaixo temos analyzedTweets que serve para armazenar os tweets que foram filtrados, um filtro customizado será adicionado mais a frente, likes que armazena o número de likes de CADA tweet, ap
'''
analyzedTweets=[]
likes = []
relevance=[]
def sortData(dataFrame):
    print("filtering...")
    for i in range(len(dataFrame)):
        current = dataFrame.loc[i,"tweet"]
        currentLike = dataFrame.loc[i,"likes"]
        pattern = r'(\blula)'
        pattern = re.compile(pattern, re.IGNORECASE)
        matches = re.search(pattern, current)
        if(matches!=None):
            analyzedTweets.append(current)
            likes.append(currentLike)
    print("done, filtered {} tweets".format(len(analyzedTweets)))
    favoredTweets=len(analyzedTweets)
    return favoredTweets
def calculateRelevance(analyzed):
    try:
        for i in range(len(analyzed)):
            relevance.append(analyzedTweets[i]*likes[i])  
    except len(analyzedTweets)!=len(likes) or IndexError:
        print("Error during sorting process, please run again")