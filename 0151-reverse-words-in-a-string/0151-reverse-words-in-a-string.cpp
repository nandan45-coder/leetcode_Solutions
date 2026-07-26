class Solution {
public:
    string reverseWords(string s) {
        string result = "";
        int i = s.length() - 1;

        while (i >= 0) {

            // Skip spaces
            while (i >= 0 && s[i] == ' ')
                i--;

            if (i < 0)
                break;

            int j = i;

            // Find the beginning of the word
            while (j >= 0 && s[j] != ' ')
                j--;

            // Add space between words
            if (!result.empty())
                result += " ";

            // Append the word
            result += s.substr(j + 1, i - j);

            i = j - 1;
        }

        return result;
    }
};