"""
## 6. Words in sonnet_words.txt but NOT in sowpods.txt  *(Hard)*

=================================================
WORDS UNIQUE TO THE SONNET
=================================================

Problem Statement:
Read the text files `sowpods.txt` and
`sonnet_words.txt`. PRINT every word that
appears in `sonnet_words.txt` but does NOT
appear in `sowpods.txt`.

This problem is about CHOOSING THE RIGHT DATA
STRUCTURE. If you check each sonnet word
against the SOWPODS list with a nested loop,
the work is O(N*M). Using SETS turns the
membership check into O(1), giving you an
overall O(N + M) algorithm.

-------------------------------------------------
Input Example:
sowpods.txt sample:
   thee
   love
   summer
   day
   eyes
   shall
   more

sonnet_words.txt sample:
   shall
   i
   compare
   thee
   to
   a
   summer
   day

Output Example:
Words in sonnet but not in sowpods:
['a', 'compare', 'i', 'to']
Total: 4

-------------------------------------------------
Explanation:
sonnet words -> {'shall', 'i', 'compare',
                 'thee', 'to', 'a', 'summer',
                 'day'}
sowpods set   -> {'thee', 'love', 'summer',
                  'day', 'eyes', 'shall',
                  'more'}
Difference (sonnet - sowpods)
              -> {'i', 'compare', 'to', 'a'}
After sorting -> ['a', 'compare', 'i', 'to'].
=================================================

"""
#write your code here

def words_unique_to_sonnet(sowpods_file, sonnet_file):

    try:
        # Read words from sowpods.txt
        with open(sowpods_file, "r") as file:
            sowpods_words = set()

            for word in file:
                sowpods_words.add(word.strip().lower())

        # Read words from sonnet_words.txt
        with open(sonnet_file, "r") as file:
            sonnet_words = set()

            for word in file:
                sonnet_words.add(word.strip().lower())

        # Find words in sonnet but not in sowpods
        unique_words = sorted(list(sonnet_words - sowpods_words))

        print("Words in sonnet but not in sowpods:")
        print(unique_words)

        print("Total:", len(unique_words))

    except FileNotFoundError:
        print("One or both files not found")


# User Input
sowpods_file = input("Enter sowpods file name: ")
sonnet_file = input("Enter sonnet file name: ")

words_unique_to_sonnet(sowpods_file, sonnet_file)