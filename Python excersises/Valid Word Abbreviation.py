# WORK IN POREGRESS

# def validWordAbbreviation(word, abbr):
#     s = ''
#     count = 0
#     for i in range(len(abbr)):
#
#         if abbr[i].isdigit() and abbr[i + 1].isdigit():
#             count += int(abbr[i] + abbr[i + 1])
#         elif abbr[i].isdigit() and not abbr[i + 1].isdigit() and not abbr[i - 1].isdigit():
#             count += int(abbr[i])
#         elif not abbr[i].isdigit():
#             s += abbr[i]
#
#     return True if count + len(s) == len(word) else False

def validWordAbbreviation(word, abbr):
    word_pointer, abbr_pointer = 0, 0
    move = 0
    while word_pointer < len(word) and abbr_pointer < len(abbr):
        print(word[word_pointer])
        if abbr[abbr_pointer].isdigit() and abbr[abbr_pointer + 1].isdigit():
            move = int(abbr[abbr_pointer] + abbr[abbr_pointer + 1])

        elif abbr[abbr_pointer].isdigit() and not abbr[abbr_pointer + 1].isdigit() \
                and not abbr[abbr_pointer - 1].isdigit():

            move = int(abbr[abbr_pointer])

        elif not abbr[abbr_pointer].isdigit():
            move += 1

        word_pointer = word_pointer + move

        abbr_pointer += 1

        move = 0

    return word_pointer, abbr_pointer


# move the pointer to that word
word = "apxle"
abbr = "a3e"

print(validWordAbbreviation(word, abbr))