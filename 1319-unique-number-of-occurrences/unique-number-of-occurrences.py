class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen={}
        for num in arr:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        for number, things_seen in seen.items():
            values=list(seen.values())
            return len(values) == len(set(values))
arr = [1,2,2,1,1,3]
sol=Solution()
print(sol.uniqueOccurrences(arr))
