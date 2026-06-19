"""
## 3. Words Containing All Five Vowels  *(Medium)*

=================================================
WORDS WITH ALL VOWELS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every word that contains ALL FIVE vowels
('a', 'e', 'i', 'o', 'u') at least once.
The order of the vowels does NOT matter, and
the check should be case-insensitive.


-------------------------------------------------
Input Example (sowpods.txt sample):
education
sequoia
facetious
hello
audio
unequivocal

Output Example:
education
sequoia
facetious
unequivocal
Total words with all vowels: 4

-------------------------------------------------
Explanation:
- "education" contains a, e, i, o, u -> yes
- "sequoia"   contains a, e, i, o, u -> yes
- "facetious" contains a, e, i, o, u -> yes
- "hello"     missing a, i, o, u     -> no
- "audio"     missing e               -> no
- "unequivocal" contains a,e,i,o,u   -> yes
=================================================

"""
# write your code here

def words_with_all_vowels(filename):

    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

    try:
        with open(filename, "r") as file:

            for word in file:
                word = word.strip().lower()

                word_letters = set(word)

                if vowels.issubset(word_letters):
                    print(word)
                    count += 1

        print("Total words with all vowels:", count)

    except FileNotFoundError:
        print("File not found")


# User input
filename = input("Enter file name: ")

words_with_all_vowels(filename)