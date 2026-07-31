from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts=defaultdict(int)
        for entry in cpdomains:
            num, domain=entry.split()
            num=int(num)
            parts=domain.split(".")
            for i in range(len(parts)):
                subdomain=".".join(parts[i:])
                counts[subdomain]+=num
        return [f"{cnt} {dom}" for dom, cnt in counts.items()]