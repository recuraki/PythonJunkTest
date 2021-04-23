from typing import List, Tuple
import re


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dat = dict()
        for k,v in knowledge:
            dat[k] = v
        res = ""
        pat = ""
        #print(dat)
        mode = False
        for i in range(len(s)):
            if mode: # キャプチャ
                if s[i] == ")":
                   #print(") find ", pat)
                    if pat in dat:
                        res += dat[pat]
                        pat = ""
                        mode = False
                        continue
                    else:
                        pat = ""
                        res += "?"
                        mode = False
                        continue
                else:
                    pat += s[i]
            else:
                if s[i] == "(":
                    mode = True
                    continue
                res += s[i]

        return res






st = Solution()
print(st.evaluate(s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]))
print(st.evaluate(s = "hi(name)", knowledge = [["a","b"]]))
print(st.evaluate(s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]))
print(st.evaluate(s = "(a)(b)", knowledge = [["a","b"],["b","a"]]))
print(st.evaluate(s = "(z)h", knowledge = [["a","b"],["b","a"]]))
print(st.evaluate(s = "(fy)(kj)(ege)r",
                  knowledge = [["uxhhkpvp","h"],["nriroroa","m"],["wvhiycvo","z"],["qsmfeing","s"],["hbcyqulf","q"],
                               ["xwgfjnrf","b"],["kfipazun","s"],["wnkrtxui","u"],["abwlsese","e"],["iimsmftc","h"],
                               ["pafqkquo","v"],["kj","tzv"],["fwwxotcd","t"],["yzgjjwjr","l"]]))
