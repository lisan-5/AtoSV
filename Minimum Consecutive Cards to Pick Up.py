class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_indices = {}
        min_length = float('inf')
        
        for i, card in enumerate(cards):
            if card in card_indices:
                min_length = min(min_length, i - card_indices[card] + 1)
            card_indices[card] = i
        
        return min_length if min_length != float('inf') else -1
