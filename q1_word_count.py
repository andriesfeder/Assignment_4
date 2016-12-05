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

    #declares dictionary and word
    dictionary = {}
    word = ''

    #for loop which goes through data character by character
    for letter in data:
        #if letter is a space and length of word is 0, continues
        #if letter is a space and length of word != 0, checks if
        #dictionary has the word as a key
        if letter == ' ':
            if len(word) == 0:
                continue
            #if dictionary has word as a key, adds 1 to the value and clears word
            if dictionary.has_key(word) :
                dictionary[word] = dictionary[word] + 1
                word = ''
            #if dictionary does not have word as a key,
            #declares word as a key with value 1 and clears word
            else :
                dictionary[word] = 1;
                word = ''
        #if letter isn't a space, word = word+letter
        else :
            word = word+letter

    #creates list ordered of keys in descending order of value of values
    ordered = sorted(dictionary, key=dictionary.__getitem__, reverse = True)
    #for loop goes key by key and prints "key:value" using ordered to decide on
    #order of printing.  Results in print of descending order list of words in file.
    for k in ordered:
        print("{}:{}".format(k, dictionary[k]))

if __name__ == '__main__':
    main()
