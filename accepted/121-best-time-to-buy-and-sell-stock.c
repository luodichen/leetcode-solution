/* https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ */
int maxProfit(int* prices, int pricesSize) 
{
    if (NULL == prices || 0 == pricesSize)
        return 0;
    
    int ret = 0;
    int min = prices[0];
    int max = prices[0];
    
    for (int i = 1; i < pricesSize; i++)
    {
        if (prices[i] < min)
            min = max = prices[i];
        else if (prices[i] > max)
            max = prices[i];
        
        if (max - min > ret)
            ret = max - min;
    }
    
    return ret;
}
