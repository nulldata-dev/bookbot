from stats import count_words #import the count_words function from stats.py

def get_book_text(file_path): #takes a file path and returns the text contained in the file as a string
    with open(file_path) as file: #use a with block to open the specified file
        file_contents = file.read() #use .read() to write the contents of the file to a string
    return file_contents #return the string containing the file contents

def main():
    frankenstein = get_book_text("./books/frankenstein.txt") #store the complete text of frankenstein in a string
    print(f"{count_words(frankenstein)} words found in the document") #print the number of words contained in frankenstein

main() #run main