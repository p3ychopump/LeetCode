class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        sum = 0
        idx = 0

        while(idx < len(s)):                                    
                if(s[idx:idx+2] in symbols):                    # When there's a two-digit number
                        print(s[idx:idx+2])                     
                        sum += symbols[s[idx:idx+2]]            # add a value of two digits to the total
                        idx += 2                                # I calculated the first two digits, so I'll find the second digit
                else:
                        sum += symbols[s[idx]]
                        idx += 1

        return sum