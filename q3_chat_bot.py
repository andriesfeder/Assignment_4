#!/usr/bin/python

import sys
import string
import random

def main():

    dictionary = {}
    eos = {}

    for word in sys.argv[1:]:

        word1 = ''
        word2 = ''
        spare = ''

        myfile = open( word , "r")
        data = myfile.read().replace('\n', ' ')
        myfile.close();
        data = data.lower()
        data = data.replace('-', ' ')
        data = data.replace('.', ' END ')
        data = data.replace('?', ' END ')
        data = data.replace('!', ' END ')
        data = data.translate(None, string.punctuation)
        data = data.replace(' END ', '.')

        for letter in data:
            if letter == ' ':
                if len(word1) == 0:
                    continue
                else :
                    break
            else :
                word1 = word1 + letter

        for letter in data:
            #if letter is a space and length of word1 or word2 is 0, continues
            #if letter is a space and length of word1 or word2 != 0, checks if
            #dictionary has the word as a key. word = word1+'-'+word2
            if letter == ' ':
                if len(word1) == 0:
                    continue
                elif len(word2) == 0:
                    continue
                if dictionary.has_key(word1) :
                    #needs to be fixed
                    dictionary[word1] = dictionary[word1] + (word2,)
                    spare = word1
                    word1 = word2
                    word2 = ''
                else :
                    dictionary[word1] = (word2,);
                    spare = word1
                    word1 = word2
                    word2 = ''
            elif letter == '.' :
                if eos.has_key(word1) :
                    #needs to be fixed
                    eos[word1] = eos[word1] + (spare,)
                else :
                    eos[word1] = (spare,);
            else :
                word2 = word2+letter
    count = 0
    while count == 0:
        output = ''
        spare = raw_input("Send: ");
        spare = spare.translate(None, string.punctuation)
        spare = spare[::-1]
        word1 = ''
        for letter in spare:
            if letter == ' ':
                if len(word1) == 0:
                    continue
                else :
                    break
            else :
                word1 = letter + word1
        if dictionary.has_key(word1) :
            word2 = random.choice(dictionary[word1])
            word2 = word2.capitalize()
            output = word2
        else :
            word2 = random.choice(dictionary.keys())
            output = word2
            output = output.capitalize()
        counter = 1
        word1 = ''
        while counter < 20 :
            if eos.has_key(word2):
                if word1 in eos[word2] :
                    break
                else :
                    word1 = word2
                    word2 = random.choice(dictionary[word2])
                    output = output + ' ' + word2
                    counter = counter + 1
            elif dictionary.has_key(word2):
                word1 = word2
                word2 = random.choice(dictionary[word2])
                output = output + ' ' + word2
                counter = counter + 1
            else :
                break
        output = output + '.'
        print output

if __name__ == '__main__':
    main()
