class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            row = []
            result = 1

            for j in range(1, i + 2):
                row.append(result)
                result = result * (i - j + 1) // j

            ans.append(row)

        return ans