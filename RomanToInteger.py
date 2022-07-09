class Solution(object):
    def romanToInt(self, s):
        sum = 0

        values = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        subtractions= {
            'I' : ['V','X'],
            'X' : ['L', 'C'],
            'C' : ['D', 'M']
        }
        i = 0
        while i in range(len(s)):
            cur = s[i]
            if i+1 < len(s) and cur in subtractions and s[i+1] in subtractions.get(cur):
                    sum += values.get(s[i+1]) - values.get(cur) 
                    i += 1
            else:
                sum += values.get(cur)
            i += 1
        return sum

if __name__ == "__main__":
    sol = Solution().romanToInt("MCMXCIV")
    print (sol)