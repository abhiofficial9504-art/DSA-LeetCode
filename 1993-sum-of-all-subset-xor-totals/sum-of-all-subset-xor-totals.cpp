class Solution {
public:
    int solve(vector<int>& nums, int idx, int xr){

        if(idx == nums.size()){
            return xr;
        }

        int take = solve(nums, idx + 1, xr ^ nums[idx]);

        int notTake = solve(nums, idx + 1, xr);

        return take + notTake;
    }

    int subsetXORSum(vector<int>& nums) {
        return solve(nums, 0, 0);
    }
};