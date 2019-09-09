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
    for i in range(0, data_frame.shape[0]):
        #run polarity scoring
        score = SentimentIntensityAnalyzer().polarity_scores(data_frame['text'].iloc[i])
        #assign to sentiment column
        data_frame['sentiment'].iloc[i] = score['compound']
    #return data frame
    return(data_frame)
    