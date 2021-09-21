# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:14:59 2021

@author: tanusha.goswami
"""


from bokeh.plotting import figure, output_file, show
from bokeh.models import Label
import pandas as pd
import os
from bokeh.io import export_png, export_svgs


print(os.getcwd())
    
''' Analysis + Visualisation '''

text_users = pd.read_csv('text_users.csv')
top_tweets_users = text_users.sort_values(by = 'user_followers_count', ascending = False).head(20)
top_tweets_users_for_img = top_tweets_users.loc[top_tweets_users['tweet_id'].isin([8296, 8884, 3247 ])]

top_tweets_users_for_img['scaled_followers'] = top_tweets_users_for_img['user_followers_count']/max((top_tweets_users_for_img['user_followers_count']))
output_file('hbar2.html')
colours = ['DC362D']
p = figure(plot_width=800, plot_height=400, title = 'MOST INFLUENTIAL TWEETS')
p.title.text_color = "#1DA1F2"
p.title.align = 'center'
p.title.text_font = "helvetica"
p.title.text_font_style = "bold"
p.title.text_font_size = '10pt'

image_path_unverified = 'D:/non-MiQ/Rihanna_Twitter/static/followers_unverified.png'
image_path_verified = 'D:/non-MiQ/Rihanna_Twitter/static/followers_verified.png'
p.background_fill_color = '#E1E8ED'
p.background_fill_alpha = 0.25
p.outline_line_width = 0
p.xaxis.visible = False
p.xgrid.visible = False
p.yaxis.visible = False
p.ygrid.visible = False
p.image_url(url = [image_path_verified], x= 1.1, y= 3, w= 0.1, h= 0.5, anchor = 'center')
p.image_url(url = [image_path_unverified], x = 1.1, y = 2, w= 0.1, h= 0.5, anchor = 'center')
p.image_url(url = [image_path_unverified], x = 1.1, y = 1, w= 0.1, h= 0.5, anchor = 'center')
p.hbar(y=[1,2,3], height=0.5, left=0,
       right=sorted(top_tweets_users_for_img['scaled_followers'].tolist()), fill_color = '#1DA1F2', line_color = '#1DA1F2')

tweet1 = Label(x=0.01, y=3.15, text='"U tried to Malign d Image of Our Country , India. But Our govt,under PM @narendramodi dispatched ', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet1_1 = Label(x = 0.01 , y = 2.95, text = '#CoronaVaccine to ur Motherland, Barbados. This is Humanity. Think the gesture shown by us despite ur ', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet1_2 = Label(x = 0.01 , y = 2.75, text = 'reckless behavior"', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet1_fav = Label(x=1.068, y=2.78, text='12k', text_font_size = '15pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')

tweet_verified_text = Label(x=1.04, y=2.65, text='User Verified', text_font_size = '8pt', text_font = 'helvetica', text_color = '#657786', text_font_style = 'italic')


tweet2 = Label(x=0.01, y=2.05, text='"He! You rehana,Foreign breeds commenting on the affairs of India,Why do you get scared over the', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet2_1 = Label(x=0.01, y=1.85, text= 'rape of Uygar Muslims in China, ever raised a voice? Dragan is danzer🤔🤔👹👹👹"', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet2_fav = Label(x=1.068, y=1.8, text='10k', text_font_size = '15pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')

tweet3 = Label(x=0.01, y=1.15, text='"could you believe this?.. For this one paid ', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet3_1 = Label(x=0.01, y=1.05, text= 'tweet @rihanna got 18 crore indian rs equal to', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet3_2 = Label(x=0.01, y=0.95, text= '1.5 million US dollars... that even paid by', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet3_3 = Label(x=0.01, y=0.85, text= 'Terr0rist organisation PR company..its on', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet3_4 = Label(x=0.01, y=0.75, text= 'indian agencies radar. 👇"', text_font_size = '8pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')
tweet3_fav = Label(x=1.078, y=0.8, text='5k', text_font_size = '15pt', text_font = 'helvetica', text_color = 'white', text_font_style = 'bold')

tweet_likes_text = Label(x=1.04, y=3.3, text='FOLLOWERS', text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')

p.add_layout(tweet1)
p.add_layout(tweet1_1)
p.add_layout(tweet1_2)
p.add_layout(tweet1_fav)
p.add_layout(tweet_verified_text)
p.add_layout(tweet2)
p.add_layout(tweet2_1)
p.add_layout(tweet2_fav)
p.add_layout(tweet3)
p.add_layout(tweet3_1)
p.add_layout(tweet3_2)
p.add_layout(tweet3_3)
p.add_layout(tweet3_4)
p.add_layout(tweet3_fav)
p.add_layout(tweet_likes_text)
show(p)

