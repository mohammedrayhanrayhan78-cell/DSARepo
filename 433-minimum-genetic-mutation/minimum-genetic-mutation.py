class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        queue=deque([(startGene, 0)])
        choices = ['A','C','G','T']
        while queue:
            curr_gene, mutations = queue.popleft()
            if curr_gene == endGene:
                return mutations
            for i in range(len(curr_gene)):
                original_char= curr_gene[i]
                for char in choices:
                    if char==original_char:
                        continue
                    next_gene=curr_gene[:i]+char+curr_gene[i+1:]
                    if next_gene in bank_set:
                        bank_set.remove(next_gene)
                        queue.append((next_gene, mutations+1))
        return -1