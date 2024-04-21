basic solution in big O(26 n)
in worst case we need to scan all aphabet, which is 26
main idea is we use sliding window to maintain the length of the input, and check wether that window is valid or not
​
how?
if the curr length window - the most freq element in curr window stil <= k
that means is valid window and we can append that to the result. Otherwise, we can move our left pointer and decrement the value in our map frequency
​
basic
```
class Solution:
def characterReplacement(self, s: str, k: int) -> int:
res = 0
freq = {}
l = 0
for r in range(len(s)):
freq[s[r]] = freq.get(s[r], 0) + 1
isValid = (r - l + 1) - max(freq.values()) <= k
if isValid:
res = max(res, (r-l+1))
continue
freq[s[l]] -= 1
l += 1
return res
```
​
improve
```
class Solution:
def characterReplacement(self, s: str, k: int) -> int:
res = 0
freq = {}
l = 0
maxF =  0
for r in range(len(s)):
freq[s[r]] = freq.get(s[r], 0) + 1
maxF = max(maxF, freq[s[r]])
isValid = (r - l + 1) - maxF <= k
if isValid:
res = max(res, (r-l+1))
continue
freq[s[l]] -= 1
l += 1
return res
```
​
​