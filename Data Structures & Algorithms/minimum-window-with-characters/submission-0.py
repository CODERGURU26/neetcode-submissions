class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        need = {}
        window = {}

        for c in t:
            need[c] = 1 + need.get(c, 0)

        have = 0
        needCount = len(need)

        res = [-1, -1]
        resLen = float("inf")

        left = 0

        for right in range(len(s)):

            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in need and window[c] == need[c]:
                have += 1

            while have == needCount:

                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        l, r = res

        return s[l:r+1] if resLen != float("inf") else ""