class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
def buildTrie(words):
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.word = word
    return root

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = buildTrie(words)
        res = []
        rows, cols = len(board), len(board[0])
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            nxt = node.children[char]
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None
            board[r][c] = "#"
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc, nxt)
            board[r][c] = char
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return res