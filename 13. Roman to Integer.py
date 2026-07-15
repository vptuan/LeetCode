class Solution(object):
    def romanToInt(self, s):
        roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        ans = 0 
        for i in range(len(s)-1):
            if roman_numerals[s[i]] < roman_numerals[s[i+1]]:
                ans -= roman_numerals[s[i]]
            else:
                ans += roman_numerals[s[i]]
        return ans + roman_numerals[s[-1]] # last digit in S
        
