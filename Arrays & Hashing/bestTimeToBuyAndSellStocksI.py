'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

'''

n = 6
maxProfit = 0
buy = 7

i = 1 - 5

i = 1:
7 > 1 = True so,
buy = 1

i = 2:
1 > 5 = False
5 - 1 > 0 = True so,
maxProfit = 4

i = 3
1 > 3 = False
3 - 1 > 4 = False

i = 4
1 > 6 = False
6 - 1 > 4 = True so,
maxProfit = 5

i = 5
1 > 4 = False
4 - 1 > 6 = False
maxProfit = 5

return 5

'''


def bestTimeToBuyAndSellStocks(prices=[]):
    if len(prices) < 2:
        return 0

    n = len(prices)
    maxProfit = 0
    buy = prices[0]

    for i in range(1, n):
        if buy > prices[i]:
            buy = prices[i]
        elif prices[i] - buy > maxProfit:
            maxProfit = prices[i] - buy

    return maxProfit


# set 01
prices = [7, 1, 5, 3, 6, 4]

# set 02
prices = [7, 6, 4, 3, 1]

print(bestTimeToBuyAndSellStocks(prices))
