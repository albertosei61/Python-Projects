import re
with open("miracle_in_the_andes.txt", "r", encoding="utf-8") as file:
    book = file.read()
    # pattern = re.compile("Chapter [0-9]+")
    # pattern = re.compile("[^\n]+love[^\n]+")
    pattern = re.compile("([a-zA-Z ]+)\n\n")
    pattern_match = re.findall(pattern, book)
    print(pattern_match)
