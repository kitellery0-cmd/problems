class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            courses[c].append(p)
        visiting = set()
        seen = set()

        def valid_course(cur) -> bool:
            if cur in visiting:
                return False
            if cur in seen:
                return True
            visiting.add(cur)
            for p in courses[cur]:
                if not valid_course(p):
                    return False
            vising.remove(cur)
            seen.add(cur)
            return True

        for c in range(numCourses):
            if not valid_course(c):
                return False
        return True
