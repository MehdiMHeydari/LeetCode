class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs == "":
            return ("")
        prim = strs[0]
        i = 0
        while i < len(prim):
            check = prim[i]
            for s in strs:
                if i + 1 > len(s) or check not in s[i]:
                    return(prim[0:i])
            i += 1
        return prim


if __name__ == "__main__":
    strs = ["aa","ab"]
    sol = Solution().longestCommonPrefix(strs)
    print ("sol: ", sol)
