from __future__ import print_function
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.core.text import Label as CoreLabel
import collections
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import googletrans
import eng_to_ipa as p
from asyncore import read
from googletrans import Translator

lemmatizer = WordNetLemmatizer()
Window.clearcolor = (0, 33 / 255, 71 / 255, 1)



class TranslatorApp(App):
    def build(self):
        layout = GridLayout(cols=2,
                            row_force_default=True,
                            row_default_height=400,
                            spacing=10,
                            padding=10
                            )
        self.INPUT = TextInput(
            text='put your text here: example\nIn summary, our results reveal robust neuronal and high-gamma auditory responses during sleep in Heschl’s gyrus and also in the anterior Superior Temporal Gyrus (STG), planum polare and middle temporal gyrus—well beyond early auditory cortex.')
        self.OUTPUT = TextInput(text='list to learn ')
        submit = Button(text='Translate', on_press=self.submit)
        layout.add_widget(self.INPUT)
        layout.add_widget(self.OUTPUT)
        layout.add_widget(submit)
        return layout

    def submit(self, obj):
        print(self.INPUT.text)

        def make_word_list():
            file = self.INPUT.text
            ps = PorterStemmer()
            out = open('../../txt/wordList.txt', 'w')

            # https://towardsdatascience.com/very-simple-python-script-for-extracting-most-common-words-from-a-story-1e3570d0b9d0

            # Stopwords
            stopwords = set(line.strip() for line in open('../../txt/stopwords.txt'))
            # stopwords = stopwords.union(set(['mr','mrs','one','two','said']))
            # Instantiate a dictionary, and for every word in the file,
            # Add to the dictionary if it doesn't exist. If it does, increase the count.
            wordcount = {}
            # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
            for word in file.lower().split():
                word = word.replace(".", "")
                word = word.replace(",", "")
                word = word.replace(":", "")
                word = word.replace("\"", "")
                word = word.replace("!", "")
                word = word.replace("*", "")
                word = word.replace("`", "")
                word = word.replace("'", " ")
                word = word.replace("?", " ")

                if word not in stopwords:
                    if word not in wordcount:
                        wordcount[word] = 1
                    else:
                        wordcount[word] += 1
            # Print most common word
            n_print = 4
            print("\nOK. The {} most common words are in: \n".format(n_print), out.name)
            word_counter = collections.Counter(wordcount)
            for word, count in word_counter.most_common(n_print):
                lems = lemmatizer.lemmatize(word, pos='a')
                print(lems)
                print(lemmatizer.lemmatize(word, pos='a'), file=out)

        make_word_list()

        def make_output_gloss():
            translator = Translator()
            # translate more than a phrase
            outputs = open('../../txt/wordList.txt')
            out = open('../../OUTPUT.txt', 'w')
            word_list = outputs.read()

            sentences = word_list.split('\n')
            translations = translator.translate(sentences, dest="ru")
            for translation in translations:
                print(f"{translation.origin}[{p.convert(translation.origin)}]  {translation.text} ", file=out)
                self.OUTPUT.text += f"{translation.origin}[{p.convert(translation.origin)}]  {translation.text}\n "

        make_output_gloss()


TranslatorApp().run()
