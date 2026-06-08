class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        box={(i,j): set() for i in range(3) for j in range(3)}

        for r in range(9):
            for c in range(9):
                v=board[r][c]
                bid=(r//3,c//3)
                
                if v=='.':
                    continue
                if v in row[r] or v in col[c] or v in box[bid]:
                    return False
                else:
                    row[r].add(v)
                    col[c].add(v)
                    box[bid].add(v)
        return True