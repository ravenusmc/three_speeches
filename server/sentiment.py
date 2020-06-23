#importing supporting libraries
import numpy as np
import pandas as pd
import json
from textblob import TextBlob

#This class will deal with the sentiment Analysis part of this project.
class SentimentAnalysis():

    def __init__(self):
        self.speeches = pd.read_json('./data/speeches.json', typ='series')

    def test(self):
        print(self.speeches)

    def get_sentiment_of_speech(self):
        

test = SentimentAnalysis()
test.test()
