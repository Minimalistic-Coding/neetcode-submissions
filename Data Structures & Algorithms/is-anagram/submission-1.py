class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencyOfs = {}

        for alpha in s:
            if alpha in frequencyOfs:
                frequencyOfs[alpha] += 1
            else:
                frequencyOfs[alpha] = 1

        frequencyOft = {}

        for alpha in t:
            if alpha in frequencyOft:
                frequencyOft[alpha] += 1
            else:
                frequencyOft[alpha] = 1

        return True if frequencyOfs == frequencyOft else False 