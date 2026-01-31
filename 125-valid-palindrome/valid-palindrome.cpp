class Solution {
public:
    bool check(int i, string &s) {
        if(i >= s.size() / 2) return true;
        if (s[i] != s[s.size() - i - 1]) return false;
        return check(i + 1, s);
    }
    bool isPalindrome(string s) {
        string t ="";
        for (char c : s) {
            if (c >= 'a' && c <= 'z')
                t += c;
            else if (c >= 'A' && c <= 'Z')
                t += (c - 'A' + 'a');
            else if (c >= '0' && c <= '9')
                t += c;
        }
        return check(0, t);
    }
};