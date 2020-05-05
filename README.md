# Exercise-Q120
Implements the following functions:
- number_to_words(), which takes as an argument a string representing a US phone
number and which outputs a string which has transformed part or all of the phone
number into a single "wordified" phone number that can be typed on a US telephone. For
example, a valid output of number_to_words("18007246837") could be "1800PAINTER".
- words_to_number(), which does the reverse of the above function (for example, the
output of words_to_number("1800PAINTER") should be "1-800-724-6837").
- all_wordifications(), which outputs all possible combinations of numbers and English
words in a given phone number. ("18007246837") could be ("1800PAINTER",
"1800PAIN837", "1800PAINT37", "180072HOT37") and possibly others.
### Notes
- My implementation only converts the final 7 digits/letters in the number provided; the country and area code are stripped before further processing.
- Ones and zeroes (1s and 0s) are left untouched as they don't traditionally have letters associated with them. As such phone numbers with too many ones and zeroes are likely to time out.
- I implemented these functions at different times and although I considered reusing the functionality implemented for all_wordifications in numbers_to_words, I like the possibility of generating larger more recognizable words as it currently implements.

### Makes use of
* an English word dictionary modified from one provided by dwyl: https://github.com/dwyl/english-words
* an English letter frequency data collated from: http://phrontistery.info/ihlstats.html#table2 and https://en.wikipedia.org/wiki/Letter_frequency
