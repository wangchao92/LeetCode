class Solution {
public:
    bool isStrobogrammatic(string num) {
        char mapping[] = {'0', '1', 'x', 'x', 'x', 'x', '9', 'x', '8', '6'};
        int length = num.length();
        if (length == 0) return false;
        int pos = length / 2 + length % 2;
        for (int i = 0; i < pos; i++) {
            if (num[i] != mapping[num[length - i - 1] - '0']) return false;
        }
        return true;
    }
};
