def twoSum(nums: list, target: int) -> list:
    # 1. Two Sum
    # https://leetcode.com/problems/two-sum/description/
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]


def isPalindrome(x: int) -> bool:
    # 9. Palindrome Number
    # https://leetcode.com/problems/palindrome-number/description/
    """
    :type x: int
    :rtype: bool
    """
    return str(x) == str(x)[::-1]


def longestCommonPrefix(strs: list) -> str:
    # 14. Longest Common Prefix
    # https://leetcode.com/problems/longest-common-prefix/description/
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = strs[0]

    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix


def isValid(s: str) -> bool:
    # 20. Valid Parentheses
    # https://leetcode.com/problems/valid-parentheses/
    """
    :type s: str
    :rtype: bool
    """
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return not s


def lengthOfLastWord(s: str) -> int:
    #58. Length of Last Word
    #https://leetcode.com/problems/length-of-last-word/description/
    """
    :type s: str
    :rtype: int
    """
    length = 0
    word = False

    for char in reversed(s):
        if char != ' ':
            word = True
            length += 1
        elif word:
            break
