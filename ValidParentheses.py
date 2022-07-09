class Solution(object):
    def isValid(self, s):
        pairs = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        
        i = 0
        while i < len(s):  
            openings = ""
            for cur in s:
                if cur in pairs:
                    openings += cur
                    i+=1
                else:
                    break
            
            temp = openings[::-1] 
            closings = ""
            for j in range(len(temp)):
                closings += pairs.get(temp[j])

            #print("o: ", openings)
            #print("c: ", closings)
            if closings == s[i:i+len(openings)]:
                i += len(openings)
            else:
                return 'false'
            i += 1
        return 'true'
            


        



if __name__ == "__main__":
    strs = "(]"
    sol = Solution().isValid(strs)
    print ("sol: ", sol)