class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        def get_coordinates(sq):
            r = n - 1 - (sq - 1) // n
            c  =(sq - 1)%n
            if(n-1-r)%2==1:
                c=n-1-c
            return r,c
        queue = deque([(1,0)])
        visited = {1}
        while queue:
            curr, moves = queue.popleft()
            if curr == n*n:
                return moves
            for nxt in range(curr+1, min(curr+6, n*n)+1):
                r,c = get_coordinates(nxt)
                destination = board[r][c] if board[r][c] != -1 else nxt
                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, moves+1))
        return -1