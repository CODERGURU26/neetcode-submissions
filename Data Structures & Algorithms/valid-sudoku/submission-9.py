class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9 
        cols = [0] * 9
        boxes = [0] * 9

        for i in range(9):
            for j in range(9):

                cell = board[i][j]

                if cell == ".":
                    continue
                
                num = ord(cell) - ord("0")
                mask = 1 << (num - 1)
                box = (i // 3) * 3 + (j // 3)

                if rows[i] & mask: 
                    return False
                
                if cols[j] & mask:
                    return False

                if boxes[box]& mask:
                    return False

                rows[i] |= mask
                cols[j] |= mask
                boxes[box] |= mask

        return True



