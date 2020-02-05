'''Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters 
then it should replace the missing second character of the final pair with an underscore ('_').

Examples:
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']'''

import re
def solution(s):
    a = re.findall('..?', s)
    print(a)
    if a == []: return []
    elif len(a[-1]) == 2: return a
    else: 
        a[-1] = a[-1] + '_'
        return a
