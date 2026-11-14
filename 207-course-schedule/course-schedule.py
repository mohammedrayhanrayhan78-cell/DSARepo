class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            pre_map[course].append(pre)
        visit_status = [0] * numCourses
        def dfs(course):
            if visit_status[course] == 1:
                return False
            if visit_status[course] == 2:
                return True
            visit_status[course]=1
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            visit_status[course] = 2
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True