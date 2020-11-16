class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits is None or len(digits) is 0:
            return result
        codes = {'0': ['0'],
                 '1': ['1'],
                 '2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        arr = [None] * len(digits)
        self.findcombinations(codes, 0, digits, result, arr)
        return result

    def findcombinations(self, codes, index, digits, result, arr):
        if index == len(digits):
            result.append(''.join(arr))
            return None

        curr_ = digits[index]
        chars = codes[curr_]

        for i in range(len(chars)):
            arr[index] = chars[i]
            self.findcombinations(codes, index + 1, digits, result, arr)
