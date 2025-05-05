class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        dependency_flow = defaultdict(list)

        for b,a in prerequisites:
            dependency_flow[b].append(a)

        completed = set()


        def dfs(a, seen):
            seen.add(a)

            for b in dependency_flow[a]:
                if b in completed:
                    continue
                elif b in seen:
                    return False
                elif not dfs(b, seen):
                    return False

            completed.add(a)

            return True



        for i in range(numCourses):
            if i in completed:
                continue
            elif not dfs(i, set()):
                return False


        return True
