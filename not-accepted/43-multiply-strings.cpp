/* https://leetcode.com/problems/multiply-strings/ */
#include <string>
#include <vector>
#include <string.h>
#include <stdio.h>

using namespace std;

class Solution 
{
public:
    string multiply(string num1, string num2) 
    {
        const char *szNum1 = num1.c_str();
        const char *szNum2 = num2.c_str();
        
        int nNum1Len = strlen(szNum1);
        int nNum2Len = strlen(szNum2);
        
        int nFlag = 0;
        int nIndex = 0;
        std::vector<int> result;

        for (int i = 0; i < nNum1Len; i++)
        {
            int nNum1 = num1[nNum1Len - 1 - i] - '0';
            for (int j = 0; j < nNum2Len; j++)
            {
                nIndex = i + j;
                int nNum2 = num2[nNum2Len - 1 - j] - '0';
                if (result.size() - 1 < nIndex)
                    result.push_back(0);
                
                int nCur = result[nIndex] + nFlag + nNum1 * nNum2;
                result[nIndex] = nCur % 10;
                nFlag = nCur / 10;
            }
            
            while (nFlag > 0)
            {
                nIndex++;
                if (result.size() - 1 < nIndex)
                    result.push_back(0);
                
                result[nIndex] = nFlag % 10;
                nFlag /= 10;
            }
        }
        
        bool bMoreThanZero = false;
        std::string ret = "";
        for (int i = result.size() - 1; i >= 0; i--)
            if (result[i] > 0 || bMoreThanZero)
            {
                bMoreThanZero = true;
                ret += (char)(result[i] + '0');
            }
        if (ret == "")
            ret = "0";
        
        return ret;
    }
};

int main()
{
    std::string s1 = "123";
    std::string s2 = "456";
    Solution s;
    printf("%s\n", s.multiply(s1, s2).c_str());
    return 0;
}
