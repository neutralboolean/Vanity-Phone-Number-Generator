import re
from random import randint
from main import main


for i in range(10):
    #gen random string of ints between 0-9
    test_array = ["%d"%randint(0, 9) for i in range(7)]
    test_array.insert(0, "1800")
    test_number = "".join(test_array)
    print("Test phone number for iteration %d: %s" %(i, test_number))
    #run wordifications first and save
    all_words = main(option="c", phoneNumber=test_number, isTest=True)
    #run number to words and check if it's in saved
        #run some x times
    print("In `numbers_to_words` test:")
    returned_set = set()
    numpass = 0
    for j in range(50):
        temp = main("a", test_number, True)
        stripped = re.sub("-", "", temp)
        if stripped in all_words:
            print("\tTest %d-%d: PASSED" % (i, j))
            returned_set.add(stripped)
            numpass += 1
        else:
            print("\tTest %d-%d: FAILED" % (i, j))
    #run word to number and see if it still matches
    wordpass = 0
    print("In `words_to_numbers` test:")
    for item in zip([n for n in range(len(returned_set))], returned_set):
        temp = main("b", item[1], True)
        stripped = re.sub("-", "", temp)
        if stripped == test_number:
            print("\tTest %d-%d: PASSED" % (i, item[0]))
            wordpass += 1
        else:
            print("\tTest %d-%d: FAILED" % (i, item[0]))
    #do maybe 10 times
    result = (
        f"Test iteration {i}:\n"
        f"\t`numbers_to_words` test: {numpass}/{50} passed\n"
        f"\t`words_to_numbers` test: {wordpass}/{len(returned_set)} passed"
    )
    print(result)

print("Completed testing without exceptions.")
