/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function (nums) {
    let arr = new Array(nums.length * 2);
    let i = 0;
    let j = nums.length;
    for (let num of nums) {
        arr[i] = nums[i]
        arr[j] = nums[i]
        i++;
        j++
    }
    return arr;
};