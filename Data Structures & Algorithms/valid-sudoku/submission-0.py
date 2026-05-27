class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row=[set()for i in range(9)]
        col=[set()for i in range(9)]
        box={}   

        for r in range(9):
            for c in range(9):
                v=board[r][c]

                if v=='.':
                    continue
                
                box_id=(r//3,c//3)

                if box_id not in box:
                    box[box_id]=set()

                if v in row[r] or v in col[c] or v in box[box_id]:
                    return False
                
                else:
                    (row[r]).add(v)
                    (col[c]).add(v)
                    box[box_id].add(v)
                
        return True
