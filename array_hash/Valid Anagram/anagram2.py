class Solution:
  #One line solution for Anagram
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
