# This file will handle a lot of the data processing for this app.


class Words():

    def __init__(self):
        self.GettysburgAddress = 'gettysburg.txt'
        self.dreamSpeech = 'dream.txt'
        self.military = 'military.txt'

    def build_word_list(self):
      words = []
      with open(self.military ,'r') as text:
          for line in text:
              for word in line.split():
                  words.append(word)
      return words

    def clean_word_list(self, word_list):
        word_and_count = {}
        len_count = 0
        #looping through the list
        while len_count < len(word_list):
            word_count = 0
            #I assign the current_word to the current position of the word_count counter
            current_word = word_list[len_count].lower()
            #I then loop through the words again seeing is certain conditions are met.
            for word in word_list:
                word = word.lower()
                if (current_word == word and current_word != 'and' and current_word != 'the' and current_word != 'The'
                and current_word != 'on' and current_word != 'of' and current_word != 'But' and current_word != 'from' and current_word != 'any'
                and current_word != 'nor' and current_word != 'this' and current_word != 'is' and current_word != 'by' and current_word != 'it'
                and current_word != 'take' and current_word != 'that' and current_word != 'but' and current_word != 'for'
                and current_word != 'these' and current_word != 'can' and current_word != 'or' and current_word != 'are'
                and current_word != 'did' and current_word != 'who' and current_word != 'say' and current_word != 'It'
                and current_word != 'rather' and current_word != 'in' and current_word != 'thus' and current_word != 'as'
                and current_word != 'do' and current_word != 'so' and current_word != 'will' and current_word != 'a'
                and current_word != 'not' and current_word != 'here' and current_word != 'whether' and current_word != 'Now'
                and current_word != 'altogether' and current_word != 'which' and current_word != 'to' and current_word != 'met'
                and current_word != 'what' and current_word != 'those' and current_word != 'always' and current_word != 'So'
                and current_word != 'Again' and current_word != 'And' and current_word != 'As' and current_word != 'Go'
                and current_word != 'well' and current_word != 'have' and current_word != 'has' and current_word != 'all'
                and current_word != 'must' and current_word != 'i' and current_word != 'my' and current_word != 'like'
                and current_word != 'me' and current_word != 'now' and current_word != 'shall' and current_word != 'with'
                and current_word != 'ever' and current_word != 'also' and current_word != 'be' and current_word != 'more'
                and current_word != 'upon' and current_word != 'no' and current_word != 'most' and current_word != 'could'):
                    word_count += 1
                    if word_count > 2:
                        word_and_count[current_word] = word_count
            len_count += 1
        return word_and_count


    def build_word_chart(self):
         speech_data = Words()
         word_list = speech_data.build_word_list()
         word_and_count = speech_data.clean_word_list(word_list)
         print(word_and_count)

test = Words()
test.build_word_chart()
