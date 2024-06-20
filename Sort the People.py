class Solution:
    def sortPeople(self, names, heights):
        people = sorted(zip(heights, names), reverse=True)
        return [name for height, name in people]
