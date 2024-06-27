class Solution:
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        index = list(range(n))
        result = [0] * n
        
        for card in sorted(deck):
            result[index.pop(0)] = card
            if index:
                index.append(index.pop(0))
        
        return result
