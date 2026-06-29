class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> ans(nums.size());
        int left = 0;
        int right = nums.size() - 1;
        int idx = nums.size() - 1;
        while(left <= right){
            if(nums[left] * nums[left] > nums[right] * nums[right]){
                ans[idx] = nums[left] * nums[left];
                left++;
            }else{
                ans[idx] = nums[right] * nums[right];
                right--;
            }
            idx--;
        }
        return ans;
    }
};