class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        LCP = 0
        while LCP < min(len(word) for word in strs):
            if len(set(word[LCP] for word in strs))== 1:
                LCP+= 1
            else:
                break
        return strs[0][0:LCP] if LCP else ""
        
