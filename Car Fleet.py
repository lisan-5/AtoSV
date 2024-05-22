class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars]
        
        fleets = 0
        while times:
            lead_time = times.pop(0)
            fleets += 1
            while times and times[0] <= lead_time:
                times.pop(0)
        
        return fleets
