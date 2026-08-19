'''
UNDERSTAND:
Given: int array -> prices [price[i]-> price of NeetCoin on ith day]

Note: choose single day to buy one neetcoin and choose diff day in future to sell

Return: max profit you can achieve -> option to not make transaction -> profit 0

MATCH:

probably a sliding window because u can leave out the prices that are greater than the dip and cut out days after the highest amount that you cna get.


'''



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right=0,1
        maxP=0

        while right<len(prices):
            if prices[left]>prices[right]:
                left=right
                right+=1
            else:
                maxP=max(maxP, prices[right]-prices[left])
                right+=1

        
        return maxP


        