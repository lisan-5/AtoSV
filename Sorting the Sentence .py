class Solution:
    def sortSentence(self, s):
        words = s.split()
        sorted_words = sorted(words, key=lambda word: int(word[-1]))
        original_sentence = ' '.join(word[:-1] for word in sorted_words)
        return original_sentence
