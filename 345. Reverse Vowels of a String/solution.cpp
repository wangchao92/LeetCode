class Solution {
public:
    string reverseVowels(string s) {
        int len = s.length();
        if (len <= 1) return s;
        int i = 0;
        int j = len - 1;
        while (i < j) {
            char ci = std::tolower(s[i]);
            char cj = std::tolower(s[j]);
            while ((i < len) && (ci != 'a') && (ci != 'e') && (ci != 'i') && (ci != 'o') && (ci != 'u')) {
                i++;
                ci = std::tolower(s[i]);
            }
            while ((j >= 0) && (cj != 'a') && (cj != 'e') && (cj != 'i') && (cj != 'o') && (cj != 'u')) {
                j--;
                cj = std::tolower(s[j]);
            }
            if (i < j && i < len && j >= 0) {
                char temp;
                temp = s[i];
                s[i] = s[j];
                s[j] = temp;
            } else
                break;
            i++;
            j--;
        }
        return s;
    }
};
