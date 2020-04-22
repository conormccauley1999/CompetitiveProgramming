class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int t = 0, n = nums.size();
        for (int i = 0; i < n; i++) {
            int s = 0;
            for (int j = i; j < n; j++) {
                s += nums[j];
                if (s == k) t++;
            }
        }
        return t;
    }
};
