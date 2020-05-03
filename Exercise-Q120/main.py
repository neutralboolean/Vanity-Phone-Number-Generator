import re
from random import choices

dictionary = []
with open("words_list.txt") as f:
    dictionary = [line.rstrip() for line in f]


number_regex = r"1?-?\d{3}-?\d{3}-?\d{4}"
numword_regex = r""
#frequencies courtesy of (http://phrontistery.info/ihlstats.html#table2)
#and (https://en.wikipedia.org/wiki/Letter_frequency)
numpad = { "2": [("A", 7.93, 6.31, 8.497), ("B", 3.86, 0.15, 1.492), ("C", 8.50, 5.07, 2.202)]}
numpad["3"] = [("D", 4.13, 3.11, 4.253), ("E", 4.09, 20.03, 11.162), ("F", 2.81, 0.19, 2.228)]
numpad["4"] = [("G", 2.95, 0.90, 2.015), ("H", 3.75, 2.14, 6.094), ("I", 3.38, 0.30, 7.546)]
numpad["5"] = [("J", 0.98, 0, 0.153), ("K", 1.32, 0.91, 1.292), ("L", 3.30, 4.81, 4.025)]
numpad["6"] = [("M", 5.90, 6.95, 2.406), ("N", 2.28, 8.26, 2.406), ("O", 3.38, 0.95, 7.507)]
numpad["7"] = [("P", 11.53, 0.46, 1.929), ("Q", 1.56, 0, 0.095), ("R", 3.43, 6.01, 7.587), ("S", 10.45, 12.51, 6.327)]
numpad["8"] = [("T", 6.14, 7.22, 9.356), ("U", 1.21, 0.22, 2.758), ("V", 2.66, 0, 0.978)]
numpad["9"] = [("W", 1.93, 0.28, 2.560), ("X", 0.61, 0.39, 0.150), ("Y", 0.48, 12.79, 1.994), ("Z", 1.43, 0.03, 0.077)]
numpad["1"] = [("-1-", 1, 1, 1)]
numpad["0"] = [("-0-", 1, 1, 1)]

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
    valid = check_numberstring(number)
    peeled = valid[4:]
    global dictionary
    new_word = ""
    maxchances = 100
    running, chances, dash_count = (True, maxchances, 0)
    while running:
        if len(peeled) == 0:
            print("\tWas unable to find a suitable solution. Please try again.\n")
            return ""
        for i in range(len(peeled)):
            digit = peeled[i]
            if digit == "-":
                dash_count += 1
                continue
            list = numpad[digit]
            result = get_relative_freq(list, i, len(peeled))
            random_letter = result
            #print(*random_letter)
            new_word += random_letter[0]
        #print(new_word)
        if new_word not in dictionary:
            chances -= 1
            new_word = ""
            if chances == 0:
                #gives a couple chances to find words of this size
                chances = maxchances
                peeled = peeled[1:]
            continue
        else:
            end = get_word_format(valid, new_word)
            return end

def get_relative_freq(tuple_list, index, length):
    set = None
    if index == 0:
        set = [(letter, start) for letter, start, end, contain in tuple_list]
    elif index == length-1:
        set = [(letter, end) for letter, start, end, contain in tuple_list]
    else:
        set = [(letter, contain) for letter, start, end, contain in tuple_list]
    letters, freqs = zip(*set)
    return choices(letters, weights=freqs)

def words_to_numbers(worded_number):
    #put check to confirm input is valid
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
    wordifications = set()
    #array of (index, char) tuples
    cleaned = re.sub("-", "", string)
    digit_arr = [ char for char in cleaned ]
    print(digit_arr)
    #iterate through list and
    start = 4
    end = len(digit_arr)
    size = end
    while size > 0:
        rangefinder = end - size + 1
        for i in range(rangefinder):
            permute_words(0, wordifications, digit_arr[start+i:i+size], cleaned[start+i:])
        size -= 1
    results = [ string[:start]+"-"+slice for slice in wordifications ]
    return results

def permute_words(index, wordset, digitslice, base):
    if len(digitslice) == 0:
        return
    for char in numpad[ base[index] ]:
        print(char, index, len(digitslice))
        digitslice[index] = char[0]
        if index >= len(digitslice) - 1:
            testword = "".join(digitslice)
            if testword in dictionary:
                wordset.add(testword)
        else:
            permute_words(index+1, wordset, digitslice, base)



def check_numberstring(string):
    """
    Checks if the parameter is valid and returns it with all dashes out
    """
    match = re.search(number_regex, string)
    if match is None:
        match = re.search(numword_regex, string)
        if match is None:
            raise InvalidNumberException("Wasn't provided a valid number")
    matched_group = match.group()
    return re.sub("-", "", matched_group)

def get_word_format(oldnum, newword):
    length = len(newword)
    #if length >= 5:
        # 0123456789ABCD
        # 1-800-724-6837
        # 1-800-PAI^NTER
        # 1-800-72-INTER
        #length += 1
    slice_index = len(oldnum) - length
    sliced = oldnum[:slice_index]
    result = ""
    for i in range(len(sliced)):
        if i == 1 or i == 4 or i == 7:
            result += "-"
        result += sliced[i]
    return result+"-"+newword

running = True
while running:
    try:
        inp = input("Which function would you like to use:\n\t(A) Number to Words\n\t(B) Words to Number\n\t(C) All Wordsification\n").lower().strip()
        number = ""
        if inp == "a" or inp == "c":
            #get number
            valid = input("Input a US phone number (format: 1-XXX-XXX-XXXX): ").strip()
            if inp == "a":
                word = number_to_words(valid)
                print(word)
            elif inp == "c":
                all_words = all_wordifications(valid)
                print(all_words)
        elif inp == "b":
            #get numwords
            valid = input("Input a US phone number with numbers replaced with letters (e.g. 1-800-PAINTER): ").strip()
            #valid = check_numwordstring(number)
            numbers = words_to_numbers(valid)
            print(numbers)
        in_input_cycle = True
        while in_input_cycle:
            doContinue = input("Do you wish to continue?(Y/N): ").lower().strip()
            if doContinue == "n" or doContinue == "no":
                in_input_cycle = False
                running = False
            elif doContinue == "y" or doContinue == "yes":
                in_input_cycle = False
    except InvalidNumberException:
        print("That is not a valid number.")
