#functions for analyzing text

def count_words(text): #takes a string and returns the number of words it contains
    words = text.split() #split the string into an array where each index is a word
    return len(words) #return the number of indexes