# This solution has a time limit issue
def maxProfit(prices):

    maximum_profit = 0
    # 1 Loop through all prices
    for i in range(len(prices)-1):
        # 2 In every price loop through all prices
        for r in (prices[i+1:]):
            print(f'left:{prices[i]}, right:{r}')
            res = r - prices[i]
            # 3 Keep the highest value
            if res > maximum_profit:
                maximum_profit = res

    return maximum_profit

# IF CHECK ALGO MOVE RIGHT ELSE COMPUTE AND FROM LEFT CONTINUE
# IF CHECK ALGO MOVE RIGHT ELSE COMPUTE AND FROM LEFT CONTINUE


def check(l, r):
    if r < l:
        return True
    else:
        return False


def maxProfit(prices):
    maximum_profit = 0

    left, right = 0, 1

    for j in range(len(prices) - 1):
        if check(prices[left], prices[right]):
            left = right
            right += 1
        else:
            res = prices[right] - prices[left]
            if res > maximum_profit:
                maximum_profit = res
            right += 1

    return maximum_profit

prices = [2,1,2,1,0,1,2]
prices = [7,1,5,3,6,4]
print(maxProfit(prices))

