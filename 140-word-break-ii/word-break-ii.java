import java.util.*;

class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        List<String> result = new ArrayList<>();
        List<String> words = new ArrayList<>();

        solve(s, 0, wordDict, words, result);

        return result;
    }

    public void solve(String s, int start, List<String> wordDict,
                      List<String> words, List<String> result) {

        if (start == s.length()) {
            result.add(String.join(" ", words));
            return;
        }

        for (String word : wordDict) {
            if (s.startsWith(word, start)) {
                words.add(word);

                solve(s, start + word.length(), wordDict, words, result);

                words.remove(words.size() - 1);
            }
        }
    }
}
        
