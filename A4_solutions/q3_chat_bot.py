#!/usr/bin/python

import sys
import string
import random

def main():

    #two dictionaries declared, one for end of sentence, one for pair recording
    dictionary = {}
    eos = {}

    #for loop to take pairs from each document given in the command line
    #functions similarly to q2
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
        #stores word pairs as key and values as tuples
        for letter in data:
            if letter == ' ':
                if len(word1) == 0:
                    continue
                elif len(word2) == 0:
                    continue
                if dictionary.has_key(word1) :
                    if word2 in dictionary[word1]:
                        spare = word1
                        word1 = word2
                        word2 = ''
                        continue
                    else:
                        dictionary[word1] = dictionary[word1] + (word2,)
                        spare = word1
                        word1 = word2
                        word2 = ''
                else :
                    dictionary[word1] = (word2,);
                    spare = word1
                    word1 = word2
                    word2 = ''
            #if '.', saves to eos dict with the second word of the pair
            #as the key and first words in the tuple used for storage
            elif letter == '.' :
                if eos.has_key(word1) :
                    if spare in eos[word1] :
                        continue
                    else :
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
            output = word2
            output = output.capitalize()
        else :
            word2 = random.choice(dictionary.keys())
            output = word2
            output = output.capitalize()
        counter = 1

        while counter < 20 :

            if dictionary.has_key(word2):
                word1 = word2
                word2 = random.choice(dictionary[word2])
                output = output + ' ' + word2
                counter = counter + 1

            if eos.has_key(word2):

                if word1 in eos[word2] :
                    break
            else :
                break
        output = output + '.'
        print output

if __name__ == '__main__':
    main()
