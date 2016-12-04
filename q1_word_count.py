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
    word = ''

    for letter in data:
        if letter == ' ':
            if len(word) == 0:
                continue
            if dictionary.has_key(word) :
                dictionary[word] = dictionary[word] + 1
            else :
                dictionary[word] = 1;
            word = ''
        else :
            word = word+letter

    ordered = sorted(dictionary, key=dictionary.__getitem__, reverse = True)
    for k in ordered:
        print("{}:{}".format(k, dictionary[k]))

    #print sorted(dictionary.values())
    #for key, value in dictionary.iteritems():
        #temp = dictionary[key]
        #print "%s:%i" % (key , value)

if __name__ == '__main__':
    main()
