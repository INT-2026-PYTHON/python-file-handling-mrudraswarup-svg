"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""
#write your code here

def is_palindrome(word):

    word = word.lower()

    return word == word[::-1]


def longest_palindrome(filename):

    longest_length = 0
    longest_words = []

    try:
        with open(filename, "r") as file:

            for word in file:

                word = word.strip()

                if is_palindrome(word):

                    if len(word) > longest_length:
                        longest_length = len(word)
                        longest_words = [word]

                    elif len(word) == longest_length:
                        longest_words.append(word)

        if longest_length > 0:
            print("Longest palindrome length:", longest_length)

            for word in longest_words:
                print(word)

        else:
            print("No palindrome found")

    except FileNotFoundError:
        print("File not found")


# User input
filename = input("Enter file name: ")

longest_palindrome(filename)