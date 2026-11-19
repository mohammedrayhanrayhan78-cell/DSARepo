class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result: list[list[int]]=[]
        path: list[int]=[]

        def backtrack(start: it ,remaining: int)->None:
            if remaining == 0:
                result.append(path.copy())
                return
            if remaining<0:
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > remaining:
                    break

                path.append(num)
                backtrack(i, remaining - num)
                path.pop()
        backtrack(0, target)
        return result