def read_book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def word_count():
    count = 0
    contents = read_book()
    # print(len(contents))  # placeholder for future implementation
    count = len(contents.split())
    return(count)

def count_char():
    contents = read_book().lower()
    char_count = {}
    for char in contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return(char_count)

def print_report():
    
    contents = count_char()
    sorted_contents = dict(sorted(contents.items(), key=lambda x: x[1], reverse=True))
    # print(sorted_contents)
    print ("--- Begin report of books/frankenstein.txt ---")
    print (f"{word_count()} words found in the document")
    for char in sorted_contents:
        if char.isalpha():
            print(f"The '{char}' character was found {sorted_contents[char]} times")
    print ("--- End report ---")
    
    # contents = count_char()
    # char_list = []
    # for char in contents:
    #     if char.isalpha():
    #         char_list.append(char)
    # char_list.sort()
    # print(char_list)

    # contents = count_char()
    # char_list = []
    # for char in contents:
    #     if char.isalpha():
    #         char_list.append(char)
    # sorted_contents = sorted(char_list)
    # print(sorted_contents)
    # for char in sorted_contents:
    #     if char.isalpha():
    #         print(char)


            # print(f"The '{char}' character was found {contents[char]} times")
            


def main():
    # read_book()
    # word_count()
    # count_char()
    print_report()
main()

