class Solution:
    def minProcessingTime(self, processorTime, tasks):
        processorTime.sort()
        tasks.sort(reverse=True)
        n = len(processorTime)
        max_time = 0
        for i in range(n):
            max_time = max(max_time, max(processorTime[i] + tasks[j] for j in range(4 * i, 4 * i + 4)))
        
        return max_time
