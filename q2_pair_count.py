#!/usr/bin/python

import sys
import string

def main():

    #open file using command line argument in read mode
    myfile = open( sys.argv[1] , "r")
    #commit the contents of the opened file to a string
    #removes character returns and replaces them with spaces
    data = myfile.read().replace('\n', ' ')
    #replaces all "-" with spaces
    data = data.replace('-', ' ')
    #makes all data lowercase
    data = data.lower()
    #removes all punctuation from data
    data = data.translate(None, string.punctuation)

    #declares dictionary and word1 and word2
    dictionary = {}
    word1 = ''
    word2 = ''

    #for loop which goes through data character by character
    #used to populate word1
    for letter in data:
        if letter == ' ':
            if len(word1) == 0:
                continue
            else :
                break
        else :
            word1 = word1 + letter

    #for loop which goes through data character by character
    for letter in data:
        #if letter is a space and length of word1 or word2 is 0, continues
        #if letter is a space and length of word1 or word2 != 0, checks if
        #dictionary has the word as a key. word = word1+'-'+word2
        if letter == ' ':

            if len(word1) == 0:
                continue
            elif len(word2) == 0:
                continue
            word = word1+ '-' + word2
            #if dictionary has word as a key, adds 1 to the value
            #sets word1 = word2 and word2 = null
            if dictionary.has_key(word) :
                dictionary[word] = dictionary[word] + 1
                word1 = word2
                word2 = ''
            #if dictionary does not have word as a key,
            #declares word as a key with value 1 and sets word1 = word2 and word2 = null
            else :
                dictionary[word] = 1;
                word1 = word2
                word2 = ''
        #if letter isn't a space, word2 = word2+letter
        else :
            word2 = word2+letter
    #creates list ordered of keys in descending order of value of values
    ordered = sorted(dictionary, key=dictionary.__getitem__, reverse = True)
    #for loop goes key by key and prints "key:value" using ordered to decide on
    #order of printing.  Results in print of descending order list of words in file.
    for k in ordered:
        print("{}:{}".format(k, dictionary[k]))

if __name__ == '__main__':
    main()
