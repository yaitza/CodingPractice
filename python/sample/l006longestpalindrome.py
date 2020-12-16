#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-11 16:04"

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
'''


def longestPalindrome(s):
    max = 0
    result_str = None
    for i in range(len(s)):
        for j in range(len(s)):
            item = s[i:j + 1]
            if judgepalindrome(item) and len(item) > max:
                result_str = item
                max = len(result_str)
    return result_str


def judgepalindrome(input_str):
    for i in range(int(len(input_str) / 2)):
        if not input_str[i].__eq__(input_str[-(i + 1)]):
            return False
    return True


def longestPalindromeEx(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    result = ""
    for k in range(n):
        for i in range(n):
            j = i + k
            if j >= len(s):
                break
            if k == 0:
                dp[i][j] = True
            elif k == 1:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
            if dp[i][j] and k + 1 > len(result):
                result = s[i:j + 1]
    return result


def longestPalindromwEx2(s):
    result = ""
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            k = i + j

            if k >= n:
                break

            if i == 0:
                dp[j][k] = True
            elif i == 1:
                dp[j][k] = (s[j] == s[k])
            else:
                dp[j][k] = (dp[j+1][k-1] and s[j] == s[k])

            if dp[j][k] and i + 1 > len(result):
                result = s[j:k+1]
    return result










# print(longestPalindrome("babad"))
print(longestPalindromwEx2("babad"))
# print(longestPalindrome("cbbd"))
print(longestPalindromwEx2("cbbdefedb"))
# print(longestPalindrome("abcdcba"))
print(longestPalindromwEx2("abcdcba"))
# print(longestPalindromwEx2("flsuqzhtcahnyickkgtfnlyzwjuiwqiexthpzvcweqzeqpmqwkydhsfipcdrsjkefehhesubkirhalgnevjugfohwnlhbj"
#                         "fewiunlgmomxkafuuokesvfmcnvseixkkzekuinmcbmttzgsqeqbrtlwyqgiquyylaswlgfflrezaxtjobltcnpjsaslyv"
#                         "iviosxorjsfncqirsjpkgajkfpoxxmvsyynbbovieoothpjgncfwcvpkvjcmrcuoronrfjcppbisqbzkgpnycqljpjlgec"
#                         "iaqrnqyxzedzkqpqsszovkgtcgxqgkflpmrikksaupukdvkzbltvefitdegnlmzeirotrfeaueqpzppnsjpspgomyezrlx"
#                         "sqlfcjrkglyvzvqakhtvfmeootbtbwfhqucbnuwznigoyatvkocqmbtqghybwrhmyvvuchjpvjckiryvjfxabezchynfxn"
#                         "pqaeampvaapgmvoylyutymdhvhqfmrlmzkhuhupizqiujpwzarnszrexpvgdmtoxvjygjpmiadzdcxtggwamkbwrkeples"
#                         "upagievwsaaletcuxtpsxmbmeztcylsjxvhzrqizdmgjfyftpzpgxateopwvynljzffszkzzqgofdlwyknqfruhdkvmvrr"
#                         "jpijcjomnrjjubfccaypkpfokohvkqndptciqqiscvmpozlyyrwobeuazsawtimnawquogrohcrnmexiwvjxgwhmtpykql"
#                         "cfacuadyhaotmmxevqwarppknoxthsmrrknu"))
print(longestPalindromeEx("flsuqzhtcahnyickkgtfnlyzwjuiwqiexthpzvcweqzeqpmqwkydhsfipcdrsjkefehhesubkirhalgnevjugfohwnlh"
                          "bjfewiunlgmomxkafuuokesvfmcnvseixkkzekuinmcbmttzgsqeqbrtlwyqgiquyylaswlgfflrezaxtjobltcnpjsa"
                          "slyviviosxorjsfncqirsjpkgajkfpoxxmvsyynbbovieoothpjgncfwcvpkvjcmrcuoronrfjcppbisqbzkgpnycqlj"
                          "pjlgeciaqrnqyxzedzkqpqsszovkgtcgxqgkflpmrikksaupukdvkzbltvefitdegnlmzeirotrfeaueqpzppnsjpspg"
                          "omyezrlxsqlfcjrkglyvzvqakhtvfmeootbtbwfhqucbnuwznigoyatvkocqmbtqghybwrhmyvvuchjpvjckiryvjfxa"
                          "bezchynfxnpqaeampvaapgmvoylyutymdhvhqfmrlmzkhuhupizqiujpwzarnszrexpvgdmtoxvjygjpmiadzdcxtggw"
                          "amkbwrkeplesupagievwsaaletcuxtpsxmbmeztcylsjxvhzrqizdmgjfyftpzpgxateopwvynljzffszkzzqgofdlwy"
                          "knqfruhdkvmvrrjpijcjomnrjjubfccaypkpfokohvkqndptciqqiscvmpozlyyrwobeuazsawtimnawquogrohcrnme"
                          "xiwvjxgwhmtpykqlcfacuadyhaotmmxevqwarppknoxthsmrrknu"))
