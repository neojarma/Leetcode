class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # semi hash
        rows = defaultdict(set)
        cols = defaultdict(set)
        subs = defaultdict(set)
        n = len(board)

        for r in range(n):
            for c in range(n):
                if board[r][c] == '.':
                    continue
                
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in subs[(r//3), c//3]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                subs[(r//3, c//3)].add(board[r][c])

        return True        