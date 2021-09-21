# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:02:15 2021

@author: tanusha.goswami
"""


import pandas as pd
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, LabelSet, Label, BoxAnnotation
from bokeh.plotting import figure

concatenated_text = pd.read_excel('concatenated_text.xlsx')
concatenated_text['frequency_scaled'] = 50*concatenated_text['frequency']/max(concatenated_text['frequency'])
def bucket_sentiment(s):
    if s == 0:
        return 'Neutral/Undefined'
    elif s < 0:
        return 'Negative'
    else:
        return 'Positive'
    
def clean_text(row):
    sentiment = row['avg_sentiment_tb']
    frequency = row['frequency']
    text = row['text']
    if ((frequency >= 350) and text not in ["n't", 'u','much'] ):
        row['clean_text'] = text      
    else:
        if (((sentiment >= 0.3) or (sentiment <= -0.1)) and (text not in ['wrong', 'nice','work','better'])):
        
            row['clean_text'] = text
        else:
            row['clean_text'] = ''
    return row
    
concatenated_text['bucket'] = concatenated_text['avg_sentiment_tb'].apply(bucket_sentiment)
concatenated_text = concatenated_text.apply(clean_text, axis = 1)
sentiments = concatenated_text['bucket'].unique().tolist()

output_file("texts.html")

source = ColumnDataSource(concatenated_text)

#p = figure(plot_width=800, plot_height=300, x_range = sentiments,
#           title="Overall Themes/Keywords vs Average Sentiment")
p = figure(plot_width=800, plot_height=300,
           title="Overall Themes/Keywords")

p.outline_line_width = 0


p.title.text_color = "#1DA1F2"
p.title.align = 'center'
p.title.text_font = "helvetica"
p.title.text_font_style = "bold"
p.title.text_font_size = '10pt'

#p.circle(x='bucket', y= 'avg_sentiment_tb',  size = 'frequency_scaled', alpha = 0.6, source=source)

p.circle(x='avg_sentiment_tb', y= 'frequency', alpha = 0.6, source=source)
labels = LabelSet(x='avg_sentiment_tb', y='frequency', text='clean_text', level='glyph',x_offset=5, y_offset=5, source=source, render_mode='canvas', text_font_size = '8pt', text_font = 'helvetica',text_font_style = 'bold')
negative_box = BoxAnnotation(top=3000, left=-1,right=0,fill_alpha=0.1, fill_color='red')
positive_box = BoxAnnotation(top=3000, left=0,right=1, fill_alpha=0.1, fill_color='green')
#labels = LabelSet(x='bucket', y='avg_sentiment_tb', text='text', level='glyph',x_offset=5, y_offset=5, source=source, render_mode='canvas')

p.add_layout(labels)
p.add_layout(negative_box)
p.add_layout(positive_box)

commentary = Label(x=0.3, y=2100, text = "The most frequently occuring words express gratitude", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')
commentary1 = Label(x=0.3, y=1950, text="and solidarity ('thanks','support') to Rihanna contrary to", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')
commentary2 = Label(x=0.3, y=1800, text="popular opinion.", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')

commentary3 = Label(x=0.3, y=1400, text="The general trend seems to be that most keywords are on", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')
commentary4 = Label(x=0.3, y=1250, text="the positive sentiment spectrum.", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')
#
#commentary5 = Label(x=3, y=-0.2, text="Although the average sentiment score of the positive and", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')
#commentary6 = Label(x=3, y=-0.25, text="negative tweets are similar,", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'italic')
#commentary7 = Label(x=3.83, y=-0.25, text="only a minute number of Tweets are ", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'bold italic')
#commentary8 = Label(x=3, y=-0.3, text="actually negative while most Tweets are neutral or undefined.", text_font_size = '8pt', text_font = 'helvetica', text_color = '#1DA1F2', text_font_style = 'bold italic')
#
p.add_layout(commentary)
p.add_layout(commentary1)
p.add_layout(commentary2)
p.add_layout(commentary3)
p.add_layout(commentary4)
#p.add_layout(commentary5)
#p.add_layout(commentary6)
#p.add_layout(commentary7)
#p.add_layout(commentary8)



p.x_range.range_padding = 0
p.background_fill_color = '#E1E8ED'
p.background_fill_alpha = 0.25

p.xgrid.grid_line_color = None
p.xaxis.axis_label = "Sentiment Score"

p.xaxis.major_label_text_color = "#1DA1F2"
p.xaxis.major_label_text_font = "helvetica"
p.xaxis.major_label_text_font_style = 'bold'
p.xaxis.major_label_text_font_size = '10pt'

p.xaxis.axis_label_text_font = "helvetica"
p.xaxis.axis_label_text_font_style = None
p.xaxis.axis_label_text_font_size = '10pt'
###
p.ygrid.grid_line_color = None
p.yaxis.axis_label = "Frequency of Word"

p.yaxis.major_label_text_font_size = '10pt'
p.yaxis.major_label_text_color = "#1DA1F2"
p.yaxis.major_label_text_font = "helvetica"
p.yaxis.major_label_text_font_style = 'bold'


p.yaxis.axis_label_text_font = "helvetica"
p.yaxis.axis_label_text_font_style = None
p.yaxis.axis_label_text_font_size = '10pt'
show(p)
