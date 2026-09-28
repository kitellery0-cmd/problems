class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort()             # sort based on position
        stack = []
        for p, s in reversed(pair):
            time = (target - p) / s # dist = speed * time
            stack.append(time)
            # add the current car to the fleet if it overtakes the closer car
            if len(stack) > 1 and stack[-1] <= stack[-2]: 
                stack.pop()
        return len(stack)
