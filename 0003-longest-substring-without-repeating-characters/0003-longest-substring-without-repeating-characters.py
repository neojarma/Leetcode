class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        ptr = 1
        seen = set()
        for i, v in enumerate(s):
            if v not in seen:
                seen.add(v)

                while ptr < len(s):
                    if s[ptr] not in seen:
                        seen.add(s[ptr])
                        ptr += 1
                    else:
                        result = max(result, len(seen))
                        ptr = i + 2
                        seen.clear()
                        break

        return max(result, len(seen))
