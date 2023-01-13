import string


def groupStrings(strings):
    hash1 = {letter: idx for idx, letter in enumerate(string.ascii_lowercase)}
    hash2 = {idx: letter for idx, letter in enumerate(string.ascii_lowercase)}

    splitted = dict()
    for param in strings:
        for i in param:
            splitted.setdefault(param, []).append(i)

    splitted = list(splitted.values())
    # get combinations
    cont = dict()
    for param in splitted:
        cont.setdefault(len(param), []).append(param)

    return cont

    # second_letter_idx = hash1[param[0]] + 1
    # shifted_seq = [hash2[second_letter_idx + i] for i in range(len(param))]
    # print(shifted_seq)


# abd 1,2 bce 1,2
# [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

def groupStrings(strings):
    cont = dict()
    for param in strings:
        key = ''
        for ch in range(1, len(param)):
            key += str((((ord(param[ch]) - ord(param[ch - 1])) + 26) % 26))
        cont.setdefault(key, []).append(param)
    return cont.values()


strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

print(groupStrings(strings))
