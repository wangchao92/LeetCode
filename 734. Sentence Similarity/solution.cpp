class Solution {
public:
    bool areSentencesSimilar(vector<string>& words1, vector<string>& words2, vector<pair<string, string>> pairs) {
        int l1 = words1.size();
        int l2 = words2.size();
        if (l1 != l2) return false;
        set<string> pairSet;
        for (auto pair : pairs) {
            pairSet.insert(pair.first + "#" + pair.second);
            pairSet.insert(pair.second + "#" + pair.first);
        }
        for (int i = 0; i < l1; i++) {
            if (!(words1[i] == words2[i] || pairSet.find(words1[i] + "#" + words2[i]) != pairSet.end() || pairSet.find(words2[i] + "#" + words1[i]) != pairSet.end())) {
                return false;
            }
        }
        return true;
    }
};
