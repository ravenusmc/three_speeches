#importing supporting libraries
import numpy as np
import pandas as pd
import json
from textblob import TextBlob

#This class will deal with the sentiment Analysis part of this project.
class SentimentAnalysis():

    def __init__(self):
        self.speeches = pd.read_json('./data/speeches.json', typ='series')

    def get_sentiment_of_sentences(self, selected_speech, sentiment_list):
        speech_text_ready_for_analysis = TextBlob(selected_speech)
        for sentence in speech_text_ready_for_analysis.sentences:
            sentence_sentiment = sentence.sentiment[0]
            

    #This is the initial method that will start to get the sentiment of each speech.
    def get_sentiment_of_speech(self):
        sentiment_object = SentimentAnalysis()
        #selected_speech = self.speeches[speech]
        speeches = ['Gettysburg Address', 'I have a Dream', 'Military Industrial Complex Speech']
        sentiment_list = []
        for speech in speeches:
            selected_speech = self.speeches[speech]
            sentiment_list = sentiment_object.get_sentiment_of_sentences(selected_speech, sentiment_list)


test = SentimentAnalysis()
#'Gettysburg Address', 'I have a Dream', 'Military Industrial Complex Speech'
test.get_sentiment_of_speech()
