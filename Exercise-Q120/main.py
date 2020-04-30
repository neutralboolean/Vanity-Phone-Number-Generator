import re
import random

dictionary = []
with open("words_alpha.txt") as f:
    dictionary = [line.rstrip() for line in f]


number_regex = r"1?-?\d{3}-?\d{3}-?\d{4}"
numword_regex = r""
numpad = { "2": ["A", "B", "C"], "3": ["D", "E", "F"], "4": ["G", "H", "I"] }
numpad["5"] = ["J", "K", "L"]
numpad["6"] = ["M", "N", "O"]
numpad["7"] = ["P", "Q", "R", "S"]
numpad["8"] = ["T", "U", "V"]
numpad["9"] = ["W", "X", "Y", "Z"]

num_lookup = {"A": "2", "B": "2", "C": "2", "D": "3", "E": "3", "F": "3", "G": "4"}
num_lookup["H"] = "4"
num_lookup["I"] = "4"
num_lookup["J"] = "5"
num_lookup["K"] = "5"
num_lookup["L"] = "5"
num_lookup["M"] = "6"
num_lookup["N"] = "6"
num_lookup["O"] = "6"
num_lookup["P"] = "7"
num_lookup["Q"] = "7"
num_lookup["R"] = "7"
num_lookup["S"] = "7"
num_lookup["T"] = "8"
num_lookup["U"] = "8"
num_lookup["V"] = "8"
num_lookup["W"] = "9"
num_lookup["X"] = "9"
num_lookup["Y"] = "9"
num_lookup["Z"] = "9"

class InvalidNumberException(Exception):
    def __init__(self, reason):
        pass

def number_to_words(number):
    check_numberstring(number)
    peeled = number[4:]
    """
    global dictionary
    new_word = ""
    running, chances, dash_count = (True, 3, 0)
    while running:
        for i in range(len(peeled)):
            digit = peeled[i]
            if digit == "-":
                dash_count += 1
                continue
            random_letter = random.choice(numpad[digit])
            new_word.join(random_letter)
        if new_word is not in dictionary:
            chances -= 1
            if chances == 0: #gives a couple chances to find words of this size
                chances = 3
                peeled = peeled[1:]
            continue
        end = getformat(number, new_word)
    return number[:end].join(new_word)
    """

def words_to_numbers(worded_number):
    number = re.sub("-", "", worded_number)
    number = number.upper()
    replaced = ""
    for i in range(len(number)):
        if number[i].isalpha():
            num = num_lookup[number[i]]
            replaced += num
        else:
            replaced += number[i]
    result = ""
    for i in range(len(replaced)):
        if i == 1 or i == 4 or i == 7:
            result += "-"
        result += replaced[i]

    return result


def all_wordifications(string):
    string = check_numberstring(number)
    pass

def check_numberstring(string):
    """
    Checks if the parameter is valid and returns it with all dashes out
    """
    match = re.search(regex, string)
    if match is None:
        match = re.search(numword_regex, string)
        if match is None:
            raise InvalidNumberException("Wasn't provided a valid number")
    matched_group = match.group()
    return re.sub("-", "", matched_group)

def get_word_format(oldnum, newword):
    length = len(newnum)
    if length >= 5:
        # 0123456789ABCD
        # 1-800-724-6837
        # 1-800-PAI^NTER
        # 1-800-72-INTER
        length += 1
    slice_index = len(oldnum) - length
    oldnum[:slice_index].join("-"+newword)

running = True
while running:
    try:
        inp = input("Which function would you like to use:\n\t(A) Number to Words\n\t(B) Words to Number\n\t(C) All Wordsification\n").lower()
        number = ""
        if inp == "a" or inp == "c":
            #get number
            valid = input("Input a US phone number (format: 1-XXX-XXX-XXXX): ")
            if inp == "a":
                word = number_to_words(valid)
                print(word)
            elif inp == "c":
                all_words = all_wordifications(valid)
                print(all_words)
        elif inp == "b":
            #get numwords
            valid = input("Input a US phone number with numbers replaced with letters (e.g. 1-800-PAINTER): ")
            #valid = check_numwordstring(number)
            numbers = words_to_numbers(valid)
            print(numbers)
        in_input_cycle = True
        while in_input_cycle:
            doContinue = input("Do you wish to continue?(Y/N): ").lower()
            if doContinue == "n" or doContinue == "no":
                in_input_cycle = False
                running = False
            elif doContinue == "y" or doContinue == "yes":
                in_input_cycle = False
    except InvalidNumberException:
        print("That is not a valid number.")
