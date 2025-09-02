"""
Google's mock interview: https://www.youtube.com/watch?v=Ti5vfu9arXQ

Problem in leetcode: https://leetcode.com/problems/maximal-square


"""


class Solution(object):
    def brute_force(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        """
        The idea is that consider every index being the top left corner of the square with only 1s.
        And at each index find the maximum square with 1s.
        """

        def size_of_square(row, col, matrix):
            
            # it is easier to write this way
            # Check if desired size can be formed, assumnig incremental
            def can_form_size(row, col, matrix, size):
                #1. Check elements of next coluumn
                next_col = col + size - 1
                if next_col >= len(matrix[0]):
                    return False
                
                for row_iter in range(row, row+size):
                    if row_iter >= len(matrix):
                        return False
                    if matrix[row_iter][next_col] != "1":
                        return False

                #2. Check elements of next row
                next_row = row + size - 1
                if next_row >= len(matrix):
                    return False
                
                for col_iter in range(col, col+size):
                    if col_iter >= len(matrix[0]):
                        return False
                    if matrix[next_row][col_iter] != "1":
                        return False

                #3. Check diagonal elements
                next_row, next_col = row, col
                for i in range(1, size):
                    if matrix[next_row+i][next_col+i] != "1":
                        return False
                
                return True
            
            # 1 is already checked.
            desired_size = 2
            while can_form_size(row, col, matrix, desired_size):
                desired_size += 1
            return desired_size - 1
        
        max_size = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                element = matrix[row][col]
                if element == "1":
                    can_form_size = size_of_square(row, col, matrix)
                    print(row, col, can_form_size)
                    max_size = max(can_form_size, max_size)
        
        #return max_size
        # return area
        return max_size*max_size


    # also known as tabulation.
    # solve smaller problems first extend the solution for larger problems
    def use_bottom_up(self, matrix):
        table = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                # only if it is 1, it can extend the square
                if matrix[row][col] != "1":
                    #table[row][col] = 0
                    continue
                else:
                    top = left = dia = 0
                    if row > 0: top = table[row-1][col]
                    if col>0: left = table[row][col-1]
                    if row > 0 and col > 0: dia = table[row-1][col-1]
                    
                    table[row][col] = min(top, left, dia) + 1
        # Now we need to pick the max of whole table.
        max_so_far = 0
        for row in table:
            max_so_far = max(max_so_far, max(row))
        return max_so_far**2


        
# recusive or top-down approach with memoization
    def use_recursive_approach_memo(self, matrix):
        memo = [[-1] * len(matrix[0]) for row in range(len(matrix))]
        max_size = 0

        def recursive(row, col, matrix):
            if row >= len(matrix) or col >= len(matrix[0]):
                return 0
            
            if matrix[row][col] != "1":
                return 0

            if memo[row][col] != -1:
                return memo[row][col]
            
            #if matrix[row][col] == 1
            right = recursive(row, col+1, matrix)
            bottom = recursive(row+1, col, matrix)
            dia = recursive(row+1, col+1, matrix)

            # if right == bottom == dia then addition of this 1 will make a bigger square
            # for ex: right == bottom == dia == 2 then it'll be 3
            # otherwise min of the all three gets picked.
            max_size_by_adding_this = min(right, bottom, dia) + 1
            memo[row][col] = max_size_by_adding_this
            return max_size_by_adding_this

        # Run recurssiive solution for each index
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_size_by_adding_this = recursive(i,j,matrix)
                max_size = max(max_size, max_size_by_adding_this)
  
        return max_size * max_size


    # recusive or top-down approach. Which recomputes sub problems several times.
    def use_recursive_approach(self, matrix):
        max_size = 0

        def recursive(row, col, matrix):
            if row >= len(matrix) or col >= len(matrix[0]):
                return 0
            
            if matrix[row][col] != "1":
                return 0
            
            #if matrix[row][col] == 1
            right = recursive(row, col+1, matrix)
            bottom = recursive(row+1, col, matrix)
            dia = recursive(row+1, col+1, matrix)

            # if right == bottom == dia then addition of this 1 will make a bigger square
            # for ex: right == bottom == dia == 2 then it'll be 3
            # otherwise min of the all three gets picked.
            max_size_by_adding_this = min(right, bottom, dia) + 1
            return max_size_by_adding_this

        # Run recurssiive solution for each index
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_size_by_adding_this = recursive(i,j,matrix)
                max_size = max(max_size, max_size_by_adding_this)
  
        return max_size * max_size


    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])
        #return self.brute_force(matrix)
        #return self.use_recursive_approach(matrix)
        #return self.use_recursive_approach_memo(matrix)
        return self.use_bottom_up(matrix)


sol = Solution()
print(sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
