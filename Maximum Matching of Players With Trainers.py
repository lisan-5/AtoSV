class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        count = 0
        for i in range(len(players)):
            while len(trainers):
                if players[i] <= trainers[0]:
                    trainers.pop(0)
                    count+=1
                    break
                else:
                    trainers.pop(0)
            if len(trainers) == 0:
                return count
        return count
