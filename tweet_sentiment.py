# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:02:15 2021

@author: tanusha.goswami
"""


import pandas as pd
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import Label

text_stats = pd.read_csv('text_stats.csv')

def bucket_sentiment(s):
    if s == 0:
        return 'Neutral/Undefined'
    elif s < 0:
        return 'Negative'
    else:
        return 'Positive'
    
text_stats['bucket'] = text_stats['tweet_sentiment_tb'].apply(bucket_sentiment)

grouped_sentiment = text_stats.groupby(['bucket']).agg({'tweet_sentiment_tb':['count','mean','median']}).reset_index()
grouped_sentiment.columns = ['bucket','count','mean','median']
grouped_sentiment['count_scaled'] = 40*(grouped_sentiment['count']/max(grouped_sentiment['count']))
grouped_sentiment['colors'] = ['#e42426','grey','#0a905d']


output_file("bars.html")

sentiments = grouped_sentiment['bucket'].unique().tolist()

source = ColumnDataSource(grouped_sentiment)

p = figure(plot_width=800, plot_height=300, x_range = sentiments,
           title="Sentiment Categorisation of Tweet Replies")
p.title.text_color = "#1DA1F2"
p.title.align = 'center'
p.title.text_font = "helvetica"
p.title.text_font_style = "bold"
p.title.text_font_size = '10pt'
p.outline_line_width = 0


p.circle(x='bucket', y= 'mean',  size = 'count_scaled', color = 'colors', alpha = 0.6, source=source)
commentary = Label(x=3, y=0.4, text="Cumulative lingustic sentiment representation", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')
commentary1 = Label(x=3, y=0.35, text="(i.e. how positive or how negative is a tweet)", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'bold italic')
commentary2 = Label(x=3, y=0.3, text="of all the sample replies to Rihanna's Tweet.", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')

commentary3 = Label(x=3, y=0.1, text="The size of each bubble indicates the proportion of", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')
commentary4 = Label(x=3, y=0.05, text="volume of Tweets having a particular sentiment.", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')

commentary5 = Label(x=3, y=-0.2, text="Although the average sentiment score of the positive and", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')
commentary6 = Label(x=3, y=-0.25, text="negative tweets are similar,", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')
commentary7 = Label(x=3.83, y=-0.25, text="only a minute number of Tweets are ", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'bold italic')
commentary8 = Label(x=3, y=-0.3, text="actually negative while most Tweets are neutral or undefined.", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'bold italic')

p.add_layout(commentary)
p.add_layout(commentary1)
p.add_layout(commentary2)
p.add_layout(commentary3)
p.add_layout(commentary4)
p.add_layout(commentary5)
p.add_layout(commentary6)
p.add_layout(commentary7)
p.add_layout(commentary8)



p.x_range.range_padding = 0
p.background_fill_color = '#E1E8ED'
p.background_fill_alpha = 0.25
p.ygrid.grid_line_color = None
p.xgrid.grid_line_color = None
p.xaxis.major_label_text_color = "#1DA1F2"
p.xaxis.major_label_text_font = "helvetica"
p.xaxis.major_label_text_font_style = "bold"
p.xaxis.major_label_text_font_size = '10pt'
p.yaxis.major_label_text_font_size = '10pt'
p.yaxis.major_label_text_color = "#1DA1F2"
p.yaxis.major_label_text_font = "helvetica"
p.yaxis.major_label_text_font_style = "bold"
p.yaxis.major_label_text_font_size = '10pt'
show(p)