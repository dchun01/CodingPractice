class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        seen = set()


        def dfs(i,j,word):
            if not word:
                return True
            seen.add((i,j))

            if (i-1) >= 0 and (i-1, j) not in seen and board[i-1][j] == word[0]:
                if dfs(i-1,j,word[1:]):
                    return True
            
            if (i+1) < len(board) and (i+1, j) not in seen and board[i+1][j] == word[0]:
                if dfs(i+1,j, word[1:]):
                    return True
            
            if (j-1) >= 0 and (i,j-1) not in seen and board[i][j-1] == word[0]:
                if dfs(i,j-1,word[1:]):
                    return True

            if (j+1) < len(board[0]) and (i,j+1) not in seen and board[i][j+1] == word[0]:
                if dfs(i,j+1,word[1:]):
                    return True

            seen.remove((i,j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i,j,word[1:]):
                    return True
        
        return False