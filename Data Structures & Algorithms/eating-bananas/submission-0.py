class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bananas_per_hour = max(piles)

        total_hours_elapsed = []

        for k in range(1, bananas_per_hour + 1):
            # consume all the piles, at a specific banana per hour
            hours_elapsed = 0
            for pile in piles:
                hours_elapsed += self.consumePile(pile, k)
            
            total_hours_elapsed.append(hours_elapsed)
        
        print(total_hours_elapsed)
        # find the minimum total hour elapsed, less than h hours.
        # the index+1 is the k
        for idx, hours in enumerate(total_hours_elapsed):
            if hours <= h:
                return idx + 1
    

    def consumePile(self, pile: int, k: int) -> int:
        # if a pile has 4 bananas, and our rate is 2, it will take us 2 hours.
        # this function will return the hours_elapsed.
        return math.ceil(pile / k)