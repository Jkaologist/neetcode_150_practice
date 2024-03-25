from typing import List


class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        N = 9
        columns, rows, boxes = [], [], []
        for _ in range(N):
            columns.append(set())
            rows.append(set())
            boxes.append(set())
        for col in range(N):
            for row in range(N):
                current_placed_digit = board[col][row]
                if current_placed_digit == ".":
                    continue

                if current_placed_digit in rows[row]:
                    return False
                rows[row].add(current_placed_digit)

                if current_placed_digit in columns[col]:
                    return False
                columns[col].add(current_placed_digit)

                curr_box = (col // 3) * 3 + row // 3
                if current_placed_digit in boxes[curr_box]:
                    return False
                boxes[curr_box].add(current_placed_digit)
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

sol = Solution()
print(sol.is_valid_sudoku(board))  # True
