class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        std::reverse(digits.begin(), digits.end());
        int size = digits.size();
        digits[0] += 1;
        for (int i = 0; i < size; i++) {
            if (digits[i] < 10)
                break;
            else {
                digits[i] = 0;
                if (i + 1 == size) digits.push_back(0);
                digits[i + 1] += 1;
            }
        }
        std::reverse(digits.begin(), digits.end());
        return digits;
    }
};
