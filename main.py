from stats import count_words
from stats import count_char
from stats import sort_dict

def get_book_text(file_path): #takes a file path and returns the text contained in the file as a string
    with open(file_path) as file: #use a with block to open the specified file
        file_contents = file.read() #use .read() to write the contents of the file to a string
    return file_contents #return the string containing the file contents

def char_count_format(book): #takes the entire text of a book as a string and returns a string with a formated output of all alpha char's and their counts in the book, in order of highest count
    output = f""
    dict_list = sort_dict(count_char(book))
    for i, dict in enumerate(dict_list): #enumerate is so sick
        output += f"{dict["char"]}: {dict["count"]}"
        if i < len(dict_list) - 1: #add a \n on all but the last entry
            output += '\n'
    return output

def main():
    path = "./books/frankenstein.txt" #store the path to the current book
    book = get_book_text(path) #store the complete text of the book in a string
    #BOOKBOT main program
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book)} total words")
    print("--------- Character Count -------")
    print(char_count_format(book))
    print("============= END ===============")

main()