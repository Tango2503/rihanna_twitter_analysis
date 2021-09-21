# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:53:10 2021

@author: tanusha.goswami
"""

import pandas as pd
from datetime import datetime
import random
import demoji 
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize 
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

stop_words = set(stopwords.words('english'))

#demoji.download_codes()

df_tweets = pd.read_excel('Rihanna - Tweet Replies.xlsx')
df_tweets2 = pd.read_excel('Rihanna - Tweet Replies_withID.xlsx')
df_tweets2 = df_tweets2.drop(columns = 'tweet_id')

df_tweets = pd.concat([df_tweets, df_tweets2])
#df_tweets = df_tweets.astype(str)

def convert_time(x):
    try:
        x = datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
        return x
    except:
        return x
df_tweets['tweet_timestamp'] = df_tweets['tweet_timestamp'].apply(convert_time)
df_tweets = df_tweets.drop_duplicates()


# Proxy Tweet IDs
proxy_id = df_tweets[['full_text','user_name']].drop_duplicates()
proxy_id['tweet_id'] = random.sample(range(1000,10000), proxy_id.shape[0])
df_tweets = pd.merge(df_tweets, proxy_id, how = 'inner', on = ['full_text','user_name'])

# Only Text
df_tweets_text = df_tweets[['tweet_id','tweet_timestamp','hashtags','full_text','user_name','user_location']]
df_tweets_text = df_tweets_text.drop_duplicates()


# Only Users 
df_tweets_users = df_tweets.groupby(['user_name','user_location','user_verified'])['user_followers_count'].max().reset_index()

#Tweet ID numerical Stats
df_tweets_stats = df_tweets[['tweet_timestamp','tweet_id','tweet_favourites','tweet_favourited','retweet_count','retweeted']]
df_tweets_stats = df_tweets_stats.drop_duplicates()
df_tweets_stats = df_tweets_stats.sort_values(by = ['tweet_id','retweet_count','tweet_favourites'], ascending = [True,False,False])

df_tweets_stats = df_tweets_stats.groupby(['tweet_id']).first().reset_index()

''' Analysis '''
# Hashtag Analysis

text_stats = pd.merge(df_tweets_text, df_tweets_stats, how = 'inner', on = 'tweet_id')
top_hashtags = text_stats.groupby(['hashtags']).aggregate({'tweet_id': 'count','tweet_favourites': 'mean',
                                 'retweet_count':'mean'}).reset_index()
top_hashtags.columns = ['hashtags','tweet_count','avg_favourites','avg_retweets']
top_hashtags['%age_share'] = top_hashtags['tweet_count']/sum(top_hashtags['tweet_count'])
top_hashtags = top_hashtags.loc[top_hashtags['tweet_count'] > 2]

# Raw Text Analysis
def cleaned_text(row):
    text = row['full_text']
    text = text.replace('@rihanna ','')
    text = text.lower()
    row['emojis'] = list(demoji.findall(text).values())
    text1 = demoji.replace_with_desc(text, sep = ":")
    text = demoji.replace(text, repl = ' ')
    row['clean_full_text'] = text1
    word_tokens = word_tokenize(text) 
    cleaned_text = [w for w in word_tokens if not w in stop_words]
    lem = WordNetLemmatizer()
    cleaned_text_stemmed = []
    for w in cleaned_text:
        root_word = lem.lemmatize(w,"v")
        cleaned_text_stemmed.append(root_word)
    row['cleaned_text'] = list(set(cleaned_text_stemmed))
    return row

def get_sentiment(row):
    text = row['clean_full_text']
    row['tweet_sentiment_tb'] = TextBlob(text).sentiment.polarity
    row['tweet_sentiment_vs'] = analyzer.polarity_scores(text)['compound']
    return row

text = df_tweets_text[['hashtags','full_text','tweet_id']]
text = text.apply(cleaned_text, axis = 1)
text = text.apply(get_sentiment, axis = 1)


text['tokenised_full_text'] = text['cleaned_text'] + text['emojis']

concatenated_text = text[['tokenised_full_text','tweet_sentiment_tb',
                          'tweet_sentiment_vs']].explode('tokenised_full_text')
concatenated_text = concatenated_text.groupby('tokenised_full_text').agg({'tweet_sentiment_tb':['count','mean'],'tweet_sentiment_vs':'mean'}).reset_index()
concatenated_text.columns = ['text','frequency','avg_sentiment_tb','avg_sentiment_vs']
concatenated_text['%age_share'] = concatenated_text['frequency']/len(text)
concatenated_text = concatenated_text.loc[concatenated_text['frequency'] > 20]


def clean_and_get_counts(text):
    dict_ct = pd.DataFrame(text, columns = ['text'])
    dict_ct = pd.DataFrame(dict_ct['text'].value_counts()).reset_index()
    dict_ct.columns = ['text','frequency']
    dict_ct = dict_ct.set_index('text')['frequency'].to_dict()
    
    return dict_ct
    

text_byhashtag = text.groupby(['hashtags'])['tokenised_full_text'].sum().reset_index()
text_byhashtag['text_freq_counts'] = text_byhashtag['tokenised_full_text'].apply(clean_and_get_counts)

top_hashtags = pd.merge(top_hashtags, text_byhashtag, how = 'left', on = 'hashtags')

# User to Tweet Analysis
text_stats = pd.merge(text_stats, text[['tweet_id','tweet_sentiment_tb','tweet_sentiment_vs']], how = 'inner', on = 'tweet_id')

text_users = pd.merge(text_stats[['tweet_id', 'hashtags', 'full_text', 'user_name',
       'user_location', 'tweet_favourites', 'tweet_sentiment_tb','tweet_sentiment_vs']], df_tweets_users, how = 'inner', on = ['user_name','user_location'])
# Most influential users - their views, sentiment, hashtags etc
# Most popular tweets - their views, sentiment, hashtags etc
    
#text_stats.to_csv('text_stats.csv',index = False)
#text_users.to_csv('text_users.csv',index = False)
    
concatenated_text.to_csv('concatenated_text.csv',index = False)

