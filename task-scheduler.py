# greedy 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # this will process the most urgent job first
        ready = list(count.values())
        heapq.heapify_max(ready)
        cooldown = deque()  # pairs of [count, time left]

        cycles = 0
        while ready or cooldown:
            if ready: # process a job
                num = heapq.heappop_max(ready) - 1
                if num:
                    cooldown.append((num, cycles + n))
            else:               # skip to next job in queue
                cycles = cooldown[0][1]
             # check the cooldown room for jobs that have waited long enough
            if cooldown and cooldown[0][1] <= cycles:
                num = cooldown.popleft()[0]
                heapq.heappush_max(ready, num)
            
            cycles += 1

        return cycles
