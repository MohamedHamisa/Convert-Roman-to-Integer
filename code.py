class Solution:
    def romanToInt(self, s):
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res, p = 0, 'I'
        for c in s[::-1]: # reverse the string, numerals in increasing order
            res, p = res - d[c] if d[c] < d[p] else res + d[c], c 
        return res

'''
         result -= d[c]
        else:
            result += d[c]
        prev = c
we need to recognise one pattern. Which is that roman numerals are placed in decreasing order, 
eg. LVI -> L=50 >= V=5 >= I=1, except when the numeral is to be subtracted from the total value, 
eg. IV -> I=1 <= 5. So, to get the final value, we can go through every character in the string, 
and compare it to the next. If the next value is bigger, we subtract the current value, else we add. 
the string is reversed so the numerals are in increasing order.
'''
