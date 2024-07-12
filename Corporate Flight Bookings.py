class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] * (n + 1)
        for start, end, seat in bookings:
            seats[start - 1] += seat
            if end < n:
                seats[end] -= seat
        for i in range(1, n):
            seats[i] += seats[i - 1]
        return seats[:-1]
