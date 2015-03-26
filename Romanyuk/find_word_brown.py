#
#
#
#
#
import nltk
from nltk.corpus import brown
def find_word(word):
    """ Функція для пошуку слова в жанрі корпуса Brown
zdfsdfgn cxgfhjdgcgnjdffnxfj
    """
    for ganre in brown.categories():
        if word in brown.words(categories=ganre):
            print word

