import googletrans
import eng_to_ipa as p
from asyncore import read
from googletrans import Translator


def make_output_gloss():
    translator = Translator()
    # translate more than a phrase
    file = open('../../txt/wordList.txt')
    out = open('../../OUTPUT.txt', 'w')
    word_list = file.read()

    sentences = word_list.split('\n')
    translations = translator.translate(sentences, dest="ru")
    for translation in translations:
        print(f"{translation.origin}[{p.convert(translation.origin)}]  {translation.text} ", file=out)

    print('glossary is now written down to txt/OUTPUT.txt')
