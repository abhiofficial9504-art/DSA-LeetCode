class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int maxT = k * threshold;
        int sum = 0;

        for(int i = 0; i < k; i++){
            sum = sum + arr[i];
        }

        int count = 0;
        
        if (sum >= maxT){
            count += 1;
        }

        for(int i = k; i < arr.size(); i++){
            sum = sum + arr[i];
            sum = sum - arr[i - k];

            if (sum >= maxT){
            count += 1;
            }
        }

        return count;
    }
};