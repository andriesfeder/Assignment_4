#!/usr/bin/python

import sys
import string

def main():
    myfile = open( sys.argv[1] , "r")
    data = myfile.read().replace('\n', ' ')
    data = data.replace('-', ' ')
    data = data.lower()
    data = data.translate(None, string.punctuation)

    dictionary = {}
    word1 = ''
    word2 = ''

    for letter in data:
        if letter == ' ':
            if len(word1) == 0:
                continue
            else :
                break
        else :
            word1 = word1 + letter

    for letter in data:
        if letter == ' ':

            if len(word1) == 0:
                continue
            elif len(word2) == 0:
                continue
            word = word1+ '-' + word2
            if dictionary.has_key(word) :
                dictionary[word] = dictionary[word] + 1
                word1 = word2
                word2 = ''
            else :
                dictionary[word] = 1;
                word1 = word2
                word2 = ''
        else :
            word2 = word2+letter

    ordered = sorted(dictionary, key=dictionary.__getitem__, reverse = True)
    for k in ordered:
        print("{}:{}".format(k, dictionary[k]))

if __name__ == '__main__':
    main()
