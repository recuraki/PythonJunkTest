# https://stackoverflow.com/questions/15155165/count-all-numbers-with-unique-digits-in-a-given-range
from typing import List, Tuple
from pprint import pprint


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        import math
        def count_num_with_DupDigits(n: int) -> int:
            # Fill in your code for the function. Do not change the function name
            # The function should return an integer.
            n_str = str(n)
            n_len = len(n_str)
            n_unique = 0

            # get the all the x000 unique digits
            if n > 10:
                for i in range(n_len - 1):
                    n_unique = n_unique + 9 * int(math.factorial(9) / math.factorial(10 - n_len + i + 1))
                m = 0
                if m == 0:
                    n_first = (int(n_str[m]) - 1) * int(math.factorial(9) / math.factorial(10 - n_len))
                m = m + 1
                count_last = 0
                n_sec = 0

                for k in range(n_len - 1):
                    if m == n_len - 1:
                        count_last = int(n_str[m]) + 1
                        for l in range(int(n_str[m]) + 1):
                            if n_str[0:n_len - 1].count(str(l)) > 0:
                                count_last = count_last - 1

                    else:
                        for s in range(int(n_str[k + 1])):
                            if n_str[0:k + 1].count(str(s)) > 0:
                                n_sec = n_sec
                            else:
                                n_sec = int(math.factorial(9 - m) / math.factorial(10 - n_len)) + n_sec
                        if n_str[0:k + 1].count(n_str[k + 1]) > 0:
                            break
                        m = m + 1
                value = n - (n_sec + n_first + n_unique + count_last)
            else:
                value = 0
            return value

        return (n - count_num_with_DupDigits(n))

st = Solution()

print(st.countSpecialNumbers(20)==19)
print(st.countSpecialNumbers(5)==5)
print(st.countSpecialNumbers(135)==110)

