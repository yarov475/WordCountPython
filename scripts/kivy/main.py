from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import collections
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import eng_to_ipa as p
from googletrans import Translator
import datetime
import re

time = f"{datetime.datetime.now()}.csv"
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
            text='In summary, our results reveal robust neuronal and high-gamma auditory responses during sleep in Heschl’s gyrus and also in the anterior Superior Temporal Gyrus (STG), planum polare and middle temporal gyrus—well beyond early auditory cortex.')

        self.OUTPUT = TextInput(text=f"list to learn,{time} \n " + chr(2200))
        submit = Button(text='Translate', on_press=self.submit)
        printCSV = Button(text='Скачать список CSV', on_press=self.printCSV)
        layout.add_widget(self.INPUT)
        layout.add_widget(self.OUTPUT)
        layout.add_widget(submit)
        layout.add_widget(printCSV)
        return layout

    def submit(self, obj):
        file = self.INPUT.text

        ps = PorterStemmer()
        stopwords = set(line.strip() for line in open('../../txt/stopwords.txt'))
        # stopwords = stopwords.union(set(['mr','mrs','one','two','said']))
        # Instantiate a dictionary, and for every word in the file,
        # Add to the dictionary if it doesn't exist. If it does, increase the count.
        wordcount = {}
        # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
        for word in file.lower().split():
            regex = re.compile('[^a-zA-Z\'\s-]')
            word = regex.sub('', word)


        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
        # Print most common word
        n_print = 10
        word_counter = collections.Counter(wordcount)
        for word, count in word_counter.most_common(n_print):
            translator = Translator()
            lems = lemmatizer.lemmatize(word, pos='a')
            more_lines = ['', 'Append text files', 'The End']
            with open('../../txt/stopwords.txt', 'a') as f:
                f.writelines('\n' + lems)

            print(lems)
            translation = translator.translate(lems, dest="ru")
            csv = ''
            csv_translated = f"{translation.origin}[{p.convert(translation.origin)}],{translation.text},\n "
            self.OUTPUT.text += csv_translated

    def printCSV(self, obj):

        out = open(time, 'w')
        print(self.OUTPUT.text, file=out)


TranslatorApp().run()
