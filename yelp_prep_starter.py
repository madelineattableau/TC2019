# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 08:55:56 2019

@author: madlee
"""

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
    for i in range(0, data_frame.shape[0]):
        #run polarity scoring
        score = SentimentIntensityAnalyzer().polarity_scores(data_frame['xxx'].iloc[i])
        #assign desired type of sentiment score to sentiment column
        data_frame['sentiment'].iloc[i] = score['xxx']
    #return data frame
    return(data_frame)
    