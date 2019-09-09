# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:46:49 2019

@author: madlee
"""

#import packages
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def classify_sentiment(data_frame):
    #for loop to go through each line of text in dataframe
    sentiment_list = []
    for i in range(0, data_frame.shape[0]):
        #run polarity scoring
        score = SentimentIntensityAnalyzer().polarity_scores(data_frame['text'].iloc[i])
        #append to sentiment_list
        sentiment_list.append(score['compound'])

    #add back to dataframe
    data_frame['sentiment'] = sentiment_list
    #return data frame
    return(data_frame)
    
