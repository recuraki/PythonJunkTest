# CのNextPermutationだが、

# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
def next_permutation(case):
    for index in range(1, len(case)):
        Px_index = len(case) - 1 - index
        # Start travelling from the end of the Data Structure
        Px = case[-index - 1]
        Px_1 = case[-index]

        # Search for a pair where latter the is greater than prior
        if Px < Px_1:
            suffix = case[-index:]
            pivot = Px
            minimum_greater_than_pivot_suffix_index = -1
            suffix_index = 0

            # Find the index inside the suffix where ::: [minimum value is greater than the pivot]
            for Py in suffix:
                if pivot < Py:
                    if minimum_greater_than_pivot_suffix_index == -1 or \
                            suffix[minimum_greater_than_pivot_suffix_index] >= Py:
                        minimum_greater_than_pivot_suffix_index = suffix_index
                suffix_index += 1
            # index in the main array
            minimum_greater_than_pivot_index = minimum_greater_than_pivot_suffix_index + Px_index + 1

            # SWAP
            temp = case[minimum_greater_than_pivot_index]
            case[minimum_greater_than_pivot_index] = case[Px_index]
            case[Px_index] = temp

            # Sort suffix
            new_suffix = case[Px_index + 1:]
            new_suffix.sort()

            # Build final Version
            new_prefix = case[:Px_index + 1]
            next_permutation = new_prefix + new_suffix
            return next_permutation
        elif index == (len(case) - 1):
            # This means that this is at the highest possible lexicographic order
            return False


# EXAMPLE EXECUTIONS
print("===INT===")
# INT LIST
case = [0, 1, 2, 5, 3, 3, 0]
case = [1,2,4,3]
print(case)
print(next_permutation(case))

print("===CHAR===")
# STRING
case_char = list("1234")
case = [ord(c) for c in case_char]
print(case)
case = next_permutation(case)
print(case)
case_char = [str(chr(c)) for c in case]
print(case_char)
print(''.join(case_char))