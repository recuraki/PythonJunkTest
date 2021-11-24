class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ss = set()
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for st in words:
            ans = ""
            for x in st:
                ans += m[ord(x) - ord("a")]
            ss.add(ans)
        return len(ss)