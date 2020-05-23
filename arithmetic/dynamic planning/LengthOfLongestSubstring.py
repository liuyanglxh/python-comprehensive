# 找出字符串中，不重复的最长子串
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.fixed_tail(s)

    '''
    总结：
        从0开始遍历，脚标为i，i代表当前所考虑的字符串的尾部（即：固定尾部）
        如果此时遍历到的字符和之前重复了，则丢弃之前的那个字符
    '''

    def fixed_tail(self, s) -> int:
        if s == "":
            return 0
        max_len, start_index = 1, -1
        d = {}
        for index, char in enumerate(s):
            '''
                例如：当前位置10，字符a：
                    1.a在字典中，d[a]和start_index的关系：
                        d[a] 大于 start_index   start_index更新为d[a]，d[a] = 10
                        d[a] 等于 start_index   start_index更新为d[a]，d[a] = 10
                        d[a] 小于 start_index   d[a] = 10，更新max_len
                    2.a不在字典中：
                        d[a] = 10，更新max_len
            '''
            if char in d and d[char] >= start_index:
                start_index = d[char]
            else:
                max_len = max(max_len, index - start_index)
            d[char] = index

        return max_len

    def best(self, s) -> int:
        if s == "":
            return 0
        count = 0  # 最大长度
        start = -1  # 当前考虑的字符串起始位置
        d = {}  # 与当前字符相同的上一个字符的位置
        for i, c in enumerate(s):
            if c in d and start < d[c]:
                start = d[c]
                d[c] = i
            else:
                d[c] = i
                if count < i - start:
                    count = i - start
        return count

    def sliding_window(self, s) -> int:
        max_len, last_end_index = 0, 0
        exist = set()
        for i in range(0, len(s)):
            for j in range(last_end_index, len(s)):
                if s[j] not in exist:
                    exist.add(s[j])
                else:
                    last_end_index = j
                    break
            max_len = max(max_len, len(exist))
            exist.remove(s[i])

        return max_len

    def use_dict(self, s) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        max_len = 0
        existDic: dict[str: List[int]] = {}
        for i in range(0, len(s)):
            if s[i] in existDic:
                existDic[s[i]].append(i)
            else:
                existDic[s[i]] = [i]

        for start_index in range(0, len(s)):
            end_index = len(s)
            for j in range(start_index, len(s)):
                positions: List[int] = existDic[s[j]]
                next_position = len(s)
                for k in range(0, len(positions)):
                    if positions[k] > j:
                        next_position = positions[k]
                        break
                end_index = min(end_index, next_position)
                if next_position - start_index <= max_len:
                    break
            max_len = max(max_len, end_index - start_index)

        return max_len

    def use_loop(self, s) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        maxLen = 0
        for i in range(0, len(s) - 1):
            exist: set = set()
            for j in range(i, len(s)):
                if s[j] not in exist:
                    exist.add(s[j])
                else:
                    break
            maxLen = max(maxLen, len(exist))
        return maxLen


print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("aa"))
print(Solution().lengthOfLongestSubstring("au"))
print(Solution().lengthOfLongestSubstring("tmmzuxt"))  # 5
