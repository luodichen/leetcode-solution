/* https://leetcode.com/submissions/detail/34823364/ */
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        std::vector<std::string> ret;
        int nSize = nums.size();

        if (0 == nSize)
            return ret;

        int nStart = nums[0];
        int nPrev = nums[0];

        for (int i = 1; i <= nSize; i++)
        {
            if (i < nSize && nums[i] == nPrev + 1)
            {
                nPrev++;
            }
            else
            {
                char szTmp[128] = {0};
                if (nStart == nPrev)
                    sprintf(szTmp, "%d", nStart);
                else
                    sprintf(szTmp, "%d->%d", nStart, nPrev);

                ret.push_back(szTmp);

                if (i < nSize)
                    nStart = nPrev = nums[i];
            }
        }

        return ret;
    }
};
