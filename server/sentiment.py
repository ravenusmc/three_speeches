#importing supporting libraries
import numpy as np
import pandas as pd
import json
from textblob import TextBlob

#This class will deal with the sentiment Analysis part of this project.
class SentimentAnalysis():

    def __init__(self):
        self.speeches = pd.read_json('./data/speeches.json', typ='series')

    def get_average(self, sentence_sentiment_list):
         return sum(sentence_sentiment_list) / len(sentence_sentiment_list)

    def get_sentiment_of_sentences(self, selected_speech, sentiment_list):
        sentiment_object = SentimentAnalysis()
        speech_text_ready_for_analysis = TextBlob(selected_speech)
        sentence_sentiment_list = []
        for sentence in speech_text_ready_for_analysis.sentences:
            sentence_sentiment = sentence.sentiment[0]
            sentence_sentiment_list.append(sentence_sentiment)
        average = sentiment_object.get_average(sentence_sentiment_list)
        sentiment_list.append(average)
        return sentiment_list

    def get_data_into_chart_format(self, speeches, sentiment_list):
        sentiment_data = []
        columns = ['Speech', 'Sentiment']
        sentiment_data.append(columns)
        count = 0
        while count < 3:
            rows = []
            rows.append(speeches[count])
            rows.append(sentiment_list[count])
            sentiment_data.append(rows)
            count += 1

    #This is the initial method that will start to get the sentiment of each speech.
    def get_sentiment_of_speech(self):
        sentiment_object = SentimentAnalysis()
        #selected_speech = self.speeches[speech]
        speeches = ['Gettysburg Address', 'I have a Dream', 'Military Industrial Complex Speech']
        sentiment_list = []
        for speech in speeches:
            selected_speech = self.speeches[speech]
            sentiment_list = sentiment_object.get_sentiment_of_sentences(selected_speech, sentiment_list)
        sentiment_object.get_data_into_chart_format(speeches, sentiment_list)

    #This method will work on getting the sentence, sentiment and subjectivity from
    #each sentence in a selected speech.
    def get_sentence_and_subjectivity(self, speech, user_sentence):
        selected_speech = self.speeches[speech]
        speech_in_list = selected_speech.split('.')
        count = 0
        while count < len(speech_in_list):
            if user_sentence == speech_in_list[count]:
                print('YAY')
                print(count)
                input()
            count += 1


# Now we are engaged in a great civil war testing whether that nation or any
#   nation so conceived and so dedicated can long endure.
test = SentimentAnalysis()
#'Gettysburg Address', 'I have a Dream', 'Military Industrial Complex Speech'
user_sentence = "Four score and seven years ago our fathers brought forth on this continent a new nation conceived in Liberty and dedicated to the proposition that all men are created equal"
test.get_sentence_and_subjectivity('Gettysburg Address', user_sentence)
