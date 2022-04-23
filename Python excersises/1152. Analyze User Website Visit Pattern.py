import collections
from itertools import combinations


def mostVisitedPattern(username, timestamp, website):

    # 1 Zip and sort tuples
    TUW = tuple(zip(timestamp, username, website))
    sortedTUW = sorted(TUW)

    userHistory = collections.defaultdict(list)
    for time, user, website in sortedTUW:
        userHistory[user].append(website)

    patternCount = collections.defaultdict(int)

    for user in userHistory.keys():
        # Return all possible unique combinations
        combs = set(combinations(userHistory[user], 3))
        # count combinations
        for comb in combs:
            patternCount[comb] = patternCount[comb] + 1

    def sortKey(pattern):
        return (-patternCount[pattern], pattern)

    return sorted(patternCount, key=sortKey)[0]



username = ["ua","ua","ua","ub","ub","ub"]
timestamp = [1,2,3,4,5,6]
website = ["a","b","a","a","b","c"]

print(mostVisitedPattern(username, timestamp, website))