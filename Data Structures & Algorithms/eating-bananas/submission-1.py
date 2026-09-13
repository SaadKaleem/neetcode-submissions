class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed, max_speed = 1, max(piles)
        target_speed = max(piles)
        # [1, 2, 3, 4, 5]

        while min_speed < max_speed:
            mid = min_speed + (max_speed - min_speed) // 2

            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)

            if total_time > h:
                min_speed = mid + 1
            else:
                max_speed = mid
                target_speed = mid
        
        return target_speed

