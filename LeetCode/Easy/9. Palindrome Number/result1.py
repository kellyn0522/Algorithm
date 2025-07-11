# 문자열 뒤집어서 계산
# 시간 복잡도 : O(log X)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]