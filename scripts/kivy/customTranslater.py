from __future__ import print_function
import collections
from nltk.stem import WordNetLemmatizer
import main
lemmatizer = WordNetLemmatizer()
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


def make_word_list():
    ps = PorterStemmer()

    file = input('write your text here: \n')


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
    n_print = int(input("How many most common words to print: "))
    print("\nOK. The {} most common words are in: \n".format(n_print), out.name)
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(n_print):
        print(lemmatizer.lemmatize(word, pos='a'), file=out)


