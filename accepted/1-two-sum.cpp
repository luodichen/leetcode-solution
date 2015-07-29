/* https://leetcode.com/problems/two-sum/ */
class Solution
{
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        std::map<int, int> table;
        int nums_len = nums.size();

        for (int i = 0; i < nums_len; i++)
            table[nums[i]] = i;

        for (int i = 0; i < nums_len; i++)
        {
            if (table.count(target - nums[i]) > 0 && table[target - nums[i]] != i)
            {
                std::vector<int> ret;
                ret.push_back(i + 1);
                ret.push_back(table[target - nums[i]] + 1);

                return ret;
            }
        }

        std::vector<int> impossible;
        impossible.push_back(-9999);
        return impossible;
    }
};
