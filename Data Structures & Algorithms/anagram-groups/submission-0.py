class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_anagram = {}

        for s in strs:
            s_sorted = "".join(sorted(s))

            if s_sorted in h_anagram:
                h_anagram[s_sorted].append(s)
            else:
                h_anagram[s_sorted] = [s]

        return list(h_anagram.values())