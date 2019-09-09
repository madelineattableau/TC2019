# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:46:49 2019

@author: madlee
"""

#import packages
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#function to classify sentiment
def classify_sentiment(data_frame):
    #for loop to go through each line of text in dataframe
    sentiment_list = []
    for i in range(0, data_frame.shape[0]):
        #run polarity scoring
        score = SentimentIntensityAnalyzer().polarity_scores(data_frame['xxx'].iloc[i])
        #append desired type of sentiment score to sentiment_list
        sentiment_list.append(score['xxx'])

    #reassign to sentiment column
    data_frame['xxx'] = xxx
    #return data frame
    return(data_frame)
    
