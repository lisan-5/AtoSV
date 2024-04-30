class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        ptr1 = 0
        ptr2 = len(people) -1

        count = 0

        while True:
            if people[ptr1] + people[ptr2]<= limit:
                count+=1
                ptr1+= 1
                ptr2-=1

            else:
                ptr2-=1
                count+=1

            if ptr1> ptr2:
                break
        return count

        
