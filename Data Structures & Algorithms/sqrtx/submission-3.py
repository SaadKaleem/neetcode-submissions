class Solution:
    def mySqrt(self, x: int) -> int:
        def condition(val):
            return val * val > x
        
        # x = 9
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # l = 0, r = 10, mid = 5 -> condition(5): 25 > 9 True
        # l = 0, r = 5, mid = 2 -> condition(2) 4 > 9 False
        # l = 3, r = 5, mid = 4 -> condition(4) 16 > 9 True
        # l = 3, r = 4, mid = 3 -> condition(3) 9 > 9 False
        # l = 4, r = 4 -> ends

        left, right = 0, x + 1

        while left < right:
            mid = left + (right - left) // 2

            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left - 1