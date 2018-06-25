class Solution {
public:
    string licenseKeyFormatting(string S, int K) {
        reverse(S.begin(), S.end());
        int len = S.length();
        int currentNum = 0;
        string newS = "";
        for (int i = 0; i < len; i++) {
            if (S[i] != '-') {
                if (currentNum == 0 && newS.length() > 0) newS += '-';
                newS += toupper(S[i]);
                currentNum += 1;
                if (currentNum == K) {
                    currentNum = 0;
                }
            }
        }
        reverse(newS.begin(), newS.end());
        return newS;
    }
};
