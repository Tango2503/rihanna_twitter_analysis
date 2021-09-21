# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:14:59 2021

@author: tanusha.goswami
"""


from bokeh.plotting import figure, output_file, show
from bokeh.models import Label
import pandas as pd
import os
#from bokeh.io import export_png, export_svgs


print(os.getcwd())
    
''' Analysis + Visualisation '''

text_stats = pd.read_csv('text_stats.csv')
text_users = pd.read_csv('text_users.csv')

top_tweets_favourited = text_stats.sort_values(by = 'tweet_favourites', ascending = False).head(3)
#top_tweets_retweeted = text_stats.sort_values(by = 'retweet_count', ascending = False).head(3)
top_tweets_users = text_users.sort_values(by = 'user_followers_count', ascending = False).head(20)
top_tweets_users_for_img = top_tweets_users.loc[top_tweets_users['tweet_id'].isin([8296, 8884, 3247 ])]

output_file('hbar.html')
colours = ['DC362D']
p = figure(plot_width=600, plot_height=400, title = 'TOP FAVOURITED TWEETS')
p.title.text_color = "#1DA1F2"
p.title.align = 'center'
p.title.text_font = "helvetica"
p.title.text_font_style = "bold"
p.title.text_font_size = '10pt'

#url = "https://static.bokeh.org/logos/logo.png"
image_path = 'D:/non-MiQ/Rihanna_Twitter/static/new_twitter_heart.png'
# #Valentine's Day Theme
#p.background_fill_color = "#FFDEE3"
#p.background_fill_color = "#FFEEE3"
#p.background_fill_color = '#FFC8D3'
#p.background_fill_color = '#FF9DC6'
#p.hbar(y=[1,2,3], height=0.5, left=0,
#       right=sorted(top_tweets_favourited['tweet_favourites'].tolist()), fill_color = '#FF3334', line_color = '#FF3334')

p.background_fill_color = '#E1E8ED'
p.background_fill_alpha = 0.25
p.outline_line_width = 0
p.xaxis.visible = False
p.xgrid.visible = False
p.yaxis.visible = False
p.ygrid.visible = False
p.image_url(url = [image_path], x = 77, y = 3, w= 12, h= 0.5, anchor = 'center')
p.image_url(url = [image_path], x = 77, y = 2, w= 12, h= 0.5, anchor = 'center')
p.image_url(url = [image_path], x = 77, y = 1, w= 12, h= 0.5, anchor = 'center')
p.hbar(y=[1,2,3], height=0.5, left=0,
       right=sorted(top_tweets_favourited['tweet_favourites'].tolist()), fill_color = '#1DA1F2', line_color = '#1DA1F2')
tweet1 = Label(x=0.5, y=2.95, text='"Bas karo ab kya 1 million like kroge kya 🤣"', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet1_fav = Label(x=75.1, y=2.915, text='68', text_font_size = '15pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')


tweet2 = Label(x=0.5, y=2.05, text='"Pop star was paid over Rs.18 crores in dollars by PR firm with', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet2_1 = Label(x=0.5, y=1.85, text= 'Khalistani links to tweet in support of farmer protests"', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet2_fav = Label(x=75.1, y=1.915, text='60', text_font_size = '15pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')

tweet3 = Label(x=0.5, y=1.05, text='"Tera rate bhi aa gaya', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet3_1 = Label(x=0.5, y=0.85, text= '🤣😂 #Rihanna"', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet3_fav = Label(x=75.1, y=0.915, text='19', text_font_size = '15pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')

tweet_likes_text = Label(x=71.2, y=3.3, text='FAVOURITES', text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')

p.add_layout(tweet1)
p.add_layout(tweet1_fav)
p.add_layout(tweet2)
p.add_layout(tweet2_1)
p.add_layout(tweet2_fav)
p.add_layout(tweet3)
p.add_layout(tweet3_1)
p.add_layout(tweet3_fav)
p.add_layout(tweet_likes_text)
show(p)
