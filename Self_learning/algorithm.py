class solution:
    def findDiagonalOrder(self, matrix:list[list[int]]) ->list:
        if not matrix:
            return []
        row = len(matrix)
        col = len(matrix[0])
        tot = row+col-1
        result = []
        r, c = 0, 0
        for i in range(tot):
            if i % 2 == 0:
                while r >= 0 and c < col:
                    result.append(matrix[r][c])
                    r -= 1
                    c += 1
                
                if c < col:
                    r += 1
                else:
                    r += 2
                    c -= 1
            else:
                while c >= 0 and r < row:
                    result.append(matrix[r][c])
                    r += 1
                    c -= 1
                if r < row:
                    c += 1
                else:
                    c += 2
                    r -= 1
        return result

if __name__ =="__main__":

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    samclass = solution()
    updated_matrix = samclass.findDiagonalOrder(matrix)
    print(updated_matrix)