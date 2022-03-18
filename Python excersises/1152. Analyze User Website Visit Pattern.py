import collections
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Sort tuples
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

        # ans = [list(k) for k,v in patternCount.items() if v == max(patternCount.values())][0]

        return sorted(patternCount, key=sortKey)[0]