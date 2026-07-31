class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        for c in s1:
            need[c] = 1 + need.get(c , 0)

        for i in range(len(s1)):
            window[s2[i]] = 1 + window.get(s2[i] , 0)

        if need == window:
           return True 

        left = 0

        for right in range(len(s1) , len(s2)):

            window[s2[right]] = 1 + window.get(s2[right] , 0)

            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

            if need == window:
                return True
        
        return False