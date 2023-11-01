# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def GetPalendrom(s):
    palendrom=''
    b=2
    i=0
    j=i+b
    while b<=len(s):
        while j<=len(s):
            word=s[i:j]
            if word== word[::-1] and len(word)>len(palendrom):
                palendrom=word
            i+=1
            j+=1
        i=0
        b+=1
        j=i+b
    return palendrom
       

print(GetPalendrom('HHHHeeololololo WWWowrlld'))
def longestPalindrome( s: str) -> str:
        palendrom=''
        b=2
        i=0
        j=i+b
        while b<len(s):
            while j<len(s):
                word=s[i:j]
                if word==word[::-1] and len(word)>len(palendrom):
                    print(palendrom)
                    palenrom=word
                i+=1
                j+=1
            i=0
            b+=1
            j=i+b
        return palendrom
print(longestPalindrome('HHHHeeololololo WWWowrlld'))