class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        heaters = [float('-inf')] + heaters + [float('inf')]  # Adding boundaries
        
        radius = 0
        i = 0
        for house in houses:
            while house >= heaters[i + 1]:  # Move to the next heater
                i += 1
            min_dist = min(house - heaters[i], heaters[i + 1] - house)
            radius = max(radius, min_dist)
        
        return radius
