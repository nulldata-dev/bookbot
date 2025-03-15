#functions for analyzing text

def count_words(text): #takes a string and returns the number of words it contains
    words = text.split() #split the string into an array where each index is a word
    return len(words) #return the number of indexes

def count_char(text): #takes a string and returns a dictionary with each char and the number of times it appears in the string 
    char_count = {} #create an empty dictionary to hold the data
    text_lower = text.lower() #convert the text into lowercase
    for char in text_lower: #iterate across all char in text_lower
        if char in char_count: #if current char is in the dictionary already
            char_count[char] += 1 #add one to the count for that char
        else: #if the current char is not in the dictionary
            char_count[char] = 1 #add it to the dictionary with the initial count of 1
    return char_count #return the dictionary

def sort_on(dict):
    return dict["count"]

def sort_dict(dict): #takes a dict of char : count(int) and returns a list of dicts {"char": char, "count": int} that are alpha char only, and sorted by "count"
    dict_list = []
    for char in dict:
        if char.isalpha() == True:
            dict_list.append({"char" : char, "count" : dict[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list